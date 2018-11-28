#include<cstdio>
#include<queue>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;

int main ()
{
	//freopen("in_A.txt", "r", stdin);
	//freopen("out_A.txt", "w", stdout);
	
	char robot[105];
	int i, Case, n, button[105], count, Opos, Bpos, temp, set = 0;
	scanf("%d", &Case);
	
	queue <int> OQ;
	queue <int> BQ;
	
	while(Case--)
	{
		scanf("%d", &n);
		count = 0;
		Opos = Bpos = 1;		
		
		for(i=0; i<n; i++)
		{
			scanf(" %c %d", &robot[i], &button[i]);
			if(robot[i] == 'O')			OQ.push(button[i]);
			else if(robot[i] == 'B')	BQ.push(button[i]);
		}
		robot[i] = '\0';
		
		for(i=0; robot[i]; i++)
		{
			if(robot[i] == 'O')
			{
				while(1)
				{
					if(Opos == button[i])
					{
						count ++;
						OQ.pop();
						if(!BQ.empty())
						{
							temp = BQ.front();
							if(Bpos > temp) Bpos --;
							else if(Bpos < temp) Bpos ++;
						}
						break;
					}
					else if(Opos < button[i])
					{
						Opos ++;
						count ++;
						if(!BQ.empty())
						{
							temp = BQ.front();
							if(Bpos > temp) Bpos --;
							else if(Bpos < temp) Bpos ++;
						}
					}
					else if(Opos > button[i])
					{
						Opos --;
						count ++;
						if(!BQ.empty())
						{
							temp = BQ.front();
							if(Bpos > temp) Bpos --;
							else if(Bpos < temp) Bpos ++;
						}						
					}
				}
			}
			else if(robot[i] == 'B')
			{
				while(1)
				{
					if(Bpos == button[i])
					{
						count ++;
						BQ.pop();
						if(!OQ.empty())
						{
							temp = OQ.front();
							if(Opos > temp) Opos --;
							else if(Opos < temp) Opos ++;
						}						
						break;
					}
					else if(Bpos < button[i])
					{
						Bpos ++;
						count ++;
						if(!OQ.empty())
						{
							temp = OQ.front();
							if(Opos > temp) Opos --;
							else if(Opos < temp) Opos ++;
						}						
					}
					else if(Bpos > button[i])
					{
						Bpos --;
						count ++;
						if(!OQ.empty())
						{
							temp = OQ.front();
							if(Opos > temp) Opos --;
							else if(Opos < temp) Opos ++;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", ++set, count);
	}
	return 0;
}