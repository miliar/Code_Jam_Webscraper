#include<stdio.h>
#include <string.h>

char map[100][100];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, Case=1;
	scanf("%d", &T);
	while(T--)
	{
		int n,m,i,j,nook=0;
		scanf("%d%d", &n, &m);
		getchar();
		memset(map,0,sizeof(map));
		for (i=0; i<n; i++)
		{
			gets(map[i]);
		}
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if(map[i][j]=='#')
				{
					if(map[i][j+1]!='#' || map[i+1][j]!='#' || map[i+1][j+1]!='#') { nook=1; goto FIN; }
					else
					{
						map[i][j]='/';
						map[i][j+1]='\\';
						map[i+1][j]='\\';
						map[i+1][j+1]='/';
					}
				}
			}
		}
FIN:
		printf("Case #%d:\n", Case++);
		if(nook==1)
		{
			printf("Impossible\n");
		}
		else
		{
			for(i=0;i<n;i++)
				printf("%s\n", map[i]);
		}
	}
	return 0;
}