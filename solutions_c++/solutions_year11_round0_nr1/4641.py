#include<stdio.h>
#include<map>

using namespace std;

typedef struct BotInfo
{
	int n;
	short O_Current;
	short B_Current;
	int TimeElapsed;
	map<int,int> BList;
	map<int,int> OList;
};
int MODU(int a, int b)
{
	if ( a > b)
	{
		return a-b;
	}
	else
		return b-a;
}

int TimeNeeded(BotInfo Data)
{
	int i = 1;
	int oCnt = 1;
	int bCnt = 1;
	Data.B_Current = 1;
	Data.O_Current = 1;
	Data.TimeElapsed = 0;
	int pos ;
	int waittime;
	map<int,int>::iterator Oit = Data.OList.begin();
	map<int,int>::iterator Bit = Data.BList.begin();
	while( i <= Data.n)
	{
		if( Bit == Data.BList.end() ||(Oit != Data.OList.end() && (*Oit).first < (*Bit).first))
		{
			pos = Data.OList[i];
			waittime = MODU(pos,Data.O_Current);
			Data.TimeElapsed += waittime;
			Data.TimeElapsed ++; // for pressing the button
			Data.O_Current = pos;
			if( Bit != Data.BList.end())
			{
				if( MODU(Data.B_Current,(*Bit).second) <= waittime+1 )
					Data.B_Current = (*Bit).second;
				else
				{
					if(Data.B_Current < (*Bit).second)
					{
						Data.B_Current += (waittime+1);
					}
					else
					{
						Data.B_Current -= (waittime+1);
					}
				}
			}
			Oit++;
		}
		else
		{
			if( Bit != Data.BList.end())
			{
				pos = Data.BList[i];
				waittime = MODU(pos,Data.B_Current);
				Data.TimeElapsed += waittime;
				Data.TimeElapsed ++; // for pressing the button
				Data.B_Current = pos;
				if( Oit != Data.OList.end() )
				{
					if( MODU(Data.O_Current,(*Oit).second) <= waittime+1 )
						Data.O_Current = (*Oit).second;
					else 
						if(Data.O_Current < (*Oit).second)
						{
							Data.O_Current += (waittime+1);
						}
						else
						{
							Data.O_Current -= (waittime+1);
						}	
				}
				Bit++;
			}
		}
		i++;
	}
	return Data.TimeElapsed;
}


int main()
{
	int t,n,j,but;
	char letter; 
	scanf("%d",&t);
	BotInfo* BotArray = new BotInfo[t];
	int i = 0;
	while( i < t)
	{
		scanf("%d",&n);
		BotArray[i].n = n;
		j = 0;
		while(j < n)
		{
			scanf("  %c", &letter );
			switch(letter)
			{
			case 'B':
				{
					scanf("%d",&but);
					BotArray[i].BList.insert(pair<int,int>(j+1,but));
					break;
				}
			case 'O':
				{
					scanf("%d",&but);
					BotArray[i].OList.insert(pair<int,int>(j+1,but));
					break;
				}
			}
			j++;
		}
		i++;
	}
    // Process the time needed
	i = 0;
	while( i < t)
	{
		printf("Case #%d: %d\n",i+1,TimeNeeded(BotArray[i]));
		i++;
	}
}