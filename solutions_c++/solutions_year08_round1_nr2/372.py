#include<stdio.h>

struct
{
	int t;
	int x[100];
	int y[100];
}peo[100];
int n,m;

int flag[100];
int ans;
int out[100];

int judge( int cur)
{
	int i, j, k;
	for( i=1; i<=n; i++ )
	{
		flag[i] = cur%2;
		cur /= 2;
	}
	for( i=0; i<m; i++ )
	{
		for( j=0; j<peo[i].t; j++ )
		{
			if( flag[ peo[i].x[j] ] == peo[i].y[j] )
				break;
		}
		if( j == peo[i].t )
			break;
	}
	if( i < m )
		return 0;
	return 1;
}

void fans( int cur )
{
	int temp[100];
	int i;
	int k = 0;
	for( i=1; i<=n; i++ )
	{
		temp[i] = cur%2;
		cur /= 2;
		k += temp[i];
	}
	if( k < ans )
	{
		for( i=1; i<=n; i++ )
			out[i] = temp[i];
		ans = k;
	}
}

int main()
{
	freopen( "temp.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int ca;
	for( ca=1; ca<=T; ca++ )
	{
		scanf("%d%d",&n,&m);
		ans = 100;
		int i, j;
		for( i=0; i<m; i++ )
		{
			scanf("%d", &peo[i].t);
			for( j=0; j<peo[i].t; j++ )
			{
				scanf("%d%d", &peo[i].x[j], &peo[i].y[j]);
			}
		}
		int cur;
		for( cur = 0; cur<1024; cur ++ )
		{
			if( judge(cur) == 1 )
			{
				fans(cur);
			}
		}
		if( ans == 100 )
			printf("Case #%d: IMPOSSIBLE\n", ca);
		else
		{
			printf("Case #%d: %d", ca, out[1]);
			for( i=2; i<=n; i++ )
				printf(" %d", out[i]);
			printf("\n");
		}
	}
	return 0;
}