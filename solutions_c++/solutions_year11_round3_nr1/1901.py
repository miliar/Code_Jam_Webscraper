#include <stdio.h>
#define MAXN 51

char G[MAXN][MAXN];
int r,c;
int cnt;
int change(void);

int main()
{
	int t;
	int i,j,k;
	int cond;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	
	scanf("%d",&t);
	for(k = 1; k <= t; k++)
	{
		scanf("%d%d",&r,&c);
		getchar();
		cnt = 0;
		for(i = 0; i < r; i++)
		{
			for(j = 0; j < c; j++)
			{
				G[i][j] = getchar();
				if(G[i][j] == '#')
					cnt++;
			}
			getchar();
		}
	
		printf("Case #%d:\n",k);
		if(cnt == 0)
			for(i = 0; i < r; i++)
			{
				for(j = 0; j < c; j++)
					putchar(G[i][j]);
				putchar('\n');
			}
		if(cnt < 4 || cnt % 4 != 0)
		{
			printf("Impossible\n");
			continue;
		}
		cond = change();
		if(!cond)
			printf("Impossible\n");
		else 	
			for(i = 0; i < r; i++)
			{
				for(j = 0; j < c; j++)
					putchar(G[i][j]);
				putchar('\n');
			}	
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

int change(void)
{
	int i,j;
	for(i = 0; i < r; i++)
	{
		for(j = 0; j < c; j++)
		{
			if(G[i][j] == '#' && j+1 < c && i + 1 < r)
			{
				if(G[i][j+1] == '#' && G[i+1][j] == '#'
					&& G[i+1][j+1] == '#')
					{
						G[i][j] = G[i+1][j+1] ='/';
						G[i][j+1] = G[i+1][j] = '\\';
						cnt -=4;
					}
				else
					return 0;
			}
		}
	}
	if(cnt == 0)
		return 1;
	else 
		return 0;
}