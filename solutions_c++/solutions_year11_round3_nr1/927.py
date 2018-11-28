#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>

using namespace std;
int ca = 1,t,R,C;
char gra[55][55];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin>>t;
	while(t--)
	{
		cout<<"Case #"<<ca++<<": \n";

		cin>>R>>C;

		for(int i = 0;i < 55;++i)
		{
			for(int j = 0;j < 55;++j) gra[i][j] = '.';
		}
		for(int i = 0;i < R;++i) scanf("%s",&gra[i]);

		for(int i = 0;i < R;++i)
		{
			for(int j = 0;j < C;++j)
			{
				if(gra[i][j] == '#' && gra[i][j+1] == '#' && gra[i+1][j] == '#' && gra[i+1][j+1] == '#')
				{
					gra[i][j] = gra[i+1][j+1] = '/';
					gra[i][j+1] = gra[i+1][j] = '\\';
				}
			}
		}

		bool flag = true;

		for(int i = 0;i < R;++i)
		{
			for(int j = 0;j < C;++j)
			{
				if(gra[i][j] == '#') 
				{
					flag = false;
					break;
				}
			}
		}
		if(!flag)
		{
			cout<<"Impossible"<<endl;
		}
		else
		{
			for(int i=  0; i<R;++i)
			{
				printf("%s\n",gra[i]);
			}
		}

	}
	return 0;
}