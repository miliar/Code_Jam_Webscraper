#include "stdio.h"

bool fun(char map[][55],int r,int c);
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	char map[55][55];
	int t,id = 1,r,c,i,j,k;

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&r,&c);
		for(i = 0; i < r; i++)
			scanf("%s",map[i]);
		bool res = fun(map,r,c);

		printf("Case #%d:\n",id++);
		if(res == true)
			for(i = 0;i < r;i ++)
			{
				for(j = 0;j < c; j++)
					printf("%c",map[i][j]);
				printf("\n");
			}
		else
			printf("Impossible\n");
	}
}

bool fun(char map[][55],int r,int c)
{
	int i,j,k;

	for(i = 0;i < r; i++)
		for(j = 0;j < c ;j++)
			if(map[i][j] == '#')
			{
				if(i < r - 1 && j < c - 1)
				{
					if(map[i+1][j] == '#' && map[i+1][j+1] == '#' && map[i][j+1] == '#')
					{
						map[i][j] = '/';
						map[i][j+1] = '\\';
						map[i+1][j] = '\\';
						map[i+1][j+1] = '/';
					}
					else 
						return false;
				}
				else
					return false;
				
			}
	return true;
}