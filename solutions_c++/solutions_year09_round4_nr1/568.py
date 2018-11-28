#include <stdio.h>
#include <string.h>
#include<stdlib.h>

int tab[50][50];
int q[50];
struct P
{
	int n;
	int val;
}p[50];

void swapp( int a,int b)
{
	int t = q[a];
	q[a] = q[b];
	q[b] = t;
}

int main()
{
	freopen("A-large(1).in", "r", stdin);
	freopen("12.out","w", stdout);
	int T;
	scanf("%d", &T);
	int ca;
	int n;
	int i,j,k;
	for( ca = 1; ca <= T; ca ++ )
	{
		scanf("%d", &n);
		for( i = 0; i< n; i ++ )
		{
			q[i] = 0;
			for( j = 0; j < n; j++ )
			{
				scanf("%1d", &tab[i][j]);
				if( tab[i][j] == 1 )
				{
					q[i] = j+1;
				}
			}
		}
		int re = 0;
		for( i = 0; i < n; i ++ )
		{
			for( j = i; j < n; j ++ )
			{
				if( q[j] <= i + 1 )
					break;
			}
			for( k = j; k > i; k -- )
			{
				swapp(k,k-1);
				re ++;
			}
		}
		printf("Case #%d: %d\n", ca, re);
	}
	return 0;
}