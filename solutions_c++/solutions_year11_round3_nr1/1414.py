#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;
char mat[55][55];
void solve()
{
	int r,c;
	scanf("%d %d",&r,&c);
	int sum = 0;
	for(int i = 1;i <= r;i++)
	{
		for(int j = 1;j <= c;j++)
		{
			char opt;
			scanf(" %c",&opt);
			mat[i][j] = opt;
			if(opt == '#')
				sum++;
		}
	}
	if(sum % 4 != 0)
	{
		printf("Impossible\n");
		return ;
	}
	else
	{
		bool mark = true;
		for(int i = 1;i <= r;i ++ )
		{
			for(int j = 1;j <= c;j++)
			{
				if(mat[i][j] == '#')
				{
					mat[i][j] = '/';
					if(i + 1 <= r)
						mat[i + 1][j] = '\\';
					else 
						mark = false;
					if(j + 1 <= c)
						mat[i][j + 1] = '\\';
					else
						mark = false;
					if(i + 1 <= r && j + 1 <= c)
						mat[i + 1][j + 1] = '/';
					else
						mark = false;
				}
				if(!mark)
					break;
			}
			if(!mark)
				break;
		}
		if(!mark)
			printf("Impossible\n");
		else
		{
			for(int i = 1;i <= r;i++)
			{
				for(int j = 1;j <= c;j++)
					printf("%c",mat[i][j]);
				printf("\n");
			}
		}
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d: \n",i);
		solve();
	}
}
