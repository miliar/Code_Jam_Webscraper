#include <iostream>
#include <fstream>

using namespace std;

int x = 0, y = 0;

char lsearchCom(char com[][3], char ch, char ch2)
{
	for(int i = 0; i < x; i ++)
	{
		for(int j = 0; j <= 1; j ++)
		{
			if(com[i][j] == ch)
			{
				if(com[i][1-j] == ch2)
					return com[i][2];
			}
		}
	}
	return ' ';
}

int main () 
{
	int T, cs = 1;
	cin>>T;
	
	while(T--)
	{
		x = 0; y = 0;
                char combine[75][3];
		char oppose[80][2];
		char list[150];
		
		int C;
		cin>>C;
		
		while(C --)
		{
			cin>>combine[x][0];
			cin>>combine[x][1];
			cin>>combine[x][2];
			
			x++;
			
//			cout<<combine[x][0];
//			cout<<combine[x][1];
//			cout<<combine[x][2];
		}
		
		int D;
		cin>>D;
		
		while(D--)
		{
			cin>>oppose[y][0];
			cin>>oppose[y][1];
			
			y++;
			
			oppose[y][0] = oppose[y-1][1];
			oppose[y][1] = oppose[y-1][0];
			
			y++;
		}
		
		int N;
		cin>>N;
		
		int count = 0;
		char combi;
		while(N--)
		{
			int flag = 1;
			cin>>list[count];
			
			if(count > 0)
			{
				combi = lsearchCom(combine, list[count], list[count-1]);
				if(combi != ' ')
				{
					list[--count] = combi;
				}
				
				else
				{
					for(int i = 0; i < y; i ++)
					{
						if(oppose[i][0] == list[count])
						{
							char toDes = oppose[i][1];
							for(int j = 0; j < count; j ++)
							{
								if(list[j] == toDes)
								{
									count = 0;
									flag = 0;
									break;
								}
							}
						}
					}
				}
			}
			if(flag != 0)
				count++;
			
		}
		
		cout<<"Case #"<<cs<<": [";
		for(int x = 0; x < count; x ++)
		{
			cout<<list[x];
			if(x < (count-1))
			{
                                cout<<", ";
			}
		}
		cout<<"]"<<endl;
		cs++;
	}
    return 0;
}
