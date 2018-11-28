#include <stdio.h>

int ans[15] = {0};
int flag[15] = {0};
int n, m;
int min;
int re[15];

struct Like{
	int num;
	int fa[15][2];
}like[105];

void dfs(int step)
{
	int i, j;
	if ( step==n )
	{
		int total = 0;
		for ( i=0; i<n; i++ )
			total += flag[i];
		for ( i=0; i<m; i++ )
		{
			int sum = 0;
			for ( j=0; j<like[i].num; j++ )
			{
				if ( flag[like[i].fa[j][0]-1]==like[i].fa[j][1] )
					sum ++;
			}
			if ( sum==0 )
				break;
		}
		if ( i==m )
		{
			if ( total<min )
			{
				min = total;
				for (int i=0; i<n; i++ )
					re[i] = flag[i];
			}
		}
		return ;
	}
	flag[step] = 0;
	dfs(step+1);
	flag[step] = 1;
	dfs(step+1);
}
int main ()
{
	int T, t;
	int i, j;
	freopen("gb.in", "r", stdin);
	freopen("gb.out", "w", stdout);
	scanf("%d", &T);
	for ( t=1; t<=T; t++ )
	{
		min = 200000;
		scanf("%d %d", &n, &m );
		for ( i=0; i<m; i++ )
		{
			scanf("%d", &like[i].num);
			for ( j=0; j<like[i].num; j++ )
				scanf("%d %d", &like[i].fa[j][0], &like[i].fa[j][1] );
		}
		dfs(0);
		printf("Case #%d: ", t);
		if ( min<=n )
		{
			for ( i=0; i<n-1; i++ )
				printf("%d ", re[i] );
			printf("%d\n", re[i] );
		}
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}