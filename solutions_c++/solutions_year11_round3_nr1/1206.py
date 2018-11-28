#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int TC = 1, T, NC = 1, N, R, RC, C, CC;
char ch;
int map[50][50], flag;



int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	memset(map, 0 , 2500*sizeof(int));
	for (cin>>T; TC <= T; TC++)
    {
		cin>>R>>C;flag = 1;
		int count = 0;
		for (RC = 0; RC < R; RC++)
		{
			for (CC = 0; CC < C; CC++)
			{
				cin>>ch;
				if (ch == '#') {map[RC][CC] = 0; count++;}
				else map[RC][CC] = 1;
			}
		}
		if (count % 4 != 0)
		{	cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
			continue;
		}
		while (count && flag)
		{
			for (RC = 0; RC < R && flag; RC++)
			{
				for (CC = 0; CC < C && flag; CC++)
				{
					if (map[RC][CC] == 0 && (RC==0|| map[RC-1][CC]) && (CC==0|| map[RC][CC-1]))
					{	
						if (RC == R || CC == C)
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						else if (map[RC+1][CC] || map[RC][CC+1] || map[RC+1][CC+1])
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						map[RC][CC] = 2;map[RC][CC+1] = 3;map[RC+1][CC] = 4;map[RC+1][CC+1] = 5;
						count -= 4;
						if (count == 0 )break;
					}
					else if (map[RC][CC] == 0 && (RC==0|| map[RC-1][CC]) && (CC==C|| map[RC][CC+1]))
					{	
						if (RC == R || CC == 0)
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						else if (map[RC+1][CC] || map[RC][CC-1] || map[RC+1][CC-1])
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						map[RC][CC] = 3;map[RC][CC-1] = 2;map[RC+1][CC] = 5;map[RC+1][CC-1] = 4;
						count -= 4;
						if (count == 0 )break;
					}
					else if (map[RC][CC] == 0 && (RC==R|| map[RC+1][CC]) && (CC==C|| map[RC][CC+1]))
					{	
						if (RC == 0 || CC == 0)
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						else if (map[RC-1][CC] || map[RC][CC-1] || map[RC-1][CC-1])
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						map[RC][CC] = 5;map[RC][CC-1] = 4;map[RC-1][CC] = 3;map[RC-1][CC-1] = 2;
						count -= 4;
						if (count == 0 )break;
					}
					else if (map[RC][CC] == 0 && (RC==R|| map[RC+1][CC]) && (CC==0|| map[RC][CC-1]))
					{	
						if (RC == 0 || CC == C)
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						else if (map[RC-1][CC] || map[RC][CC+1] || map[RC-1][CC+1])
						{	
							cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
							flag = 0;break;			
						}
						map[RC][CC] = 4;map[RC][CC+1] = 5;map[RC-1][CC] = 2;map[RC-1][CC+1] = 3;
						count -= 4;
						if (count == 0 )break;
					}
				}
			}
		}
		if (flag)
		{
			cout<<"Case #"<<TC<<": "<<endl;
			for (RC = 0; RC < R; RC++)
			{
				for (CC = 0; CC < C; CC++)
				{
					char tmp = 92;//cout<<map[RC][CC];
					if (map[RC][CC] == 1) cout<<'.';
					else if (map[RC][CC] == 2) cout<<('/');
					else if (map[RC][CC] == 3) cout<<tmp;
					else if (map[RC][CC] == 4) cout<<tmp;
					else if (map[RC][CC] == 5) cout<<'/';
				}
				cout<<endl;
			}
		}
		//else cout<<"Case #"<<TC<<": "<<endl<<"Impossible"<<endl;
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}

