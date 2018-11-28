#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

char table[55][55];
int main()
{
	freopen("e:\\A-large.in", "r", stdin);	freopen("e:\\A-large.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int r,c;
		scanf("%d %d",&r,&c);
		memset(table,0,sizeof(table));
		getchar();
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				scanf("%c",&table[j][k]);
			}
			getchar();
		}
		int flag=0;
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				if(table[j][k] == '#')
				{
					if(((j+1) >= r)||((k+1) >= c))
					{
						flag=1;
						break;
					}
					if((table[j+1][k] == '#')&&(table[j][k+1] == '#')&&(table[j+1][k+1] == '#'))
					{
						table[j][k]='/';
						table[j+1][k]='\\';
						table[j][k+1]='\\';
						table[j+1][k+1]='/';
						continue;
					}
					flag=1;
					break;
				}
				if(flag == 1)
					break;
			}
		}
		printf("Case #%d:\n",i+1);
		if(flag == 1)
			printf("Impossible\n");
		else
		{
			for(int j=0;j<r;j++)
			{
				for(int k=0;k<c;k++)
				{
					printf("%c",table[j][k]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}