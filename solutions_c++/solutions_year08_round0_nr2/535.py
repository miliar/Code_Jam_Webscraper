#include<stdio.h>
#include<stdlib.h>

const int M = 210;

struct P
{
	int s;
	int t;
	int flag;
}q[M];

int cmp( const void *a, const void *b )
{
	return (*(P *)a).s - (*(P *)b).s;
}

int main()
{
	freopen( "temp.txt", "r", stdin);
	freopen( "out.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	int casenum = 0;
	while( N -- )
	{
		casenum ++;
		int t;
		int na,nb;
		scanf("%d%d%d", &t, &na, &nb);
		int n = na + nb;
		int i, j;
		for( i=0; i<na; i++ )
		{
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			q[i].s = a*60 + b;
			q[i].t = c*60 + d;
			q[i].flag = 0;
		}
		for( i = na; i<na+nb; i++ )
		{
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			q[i].s = a*60 + b;
			q[i].t = c*60 + d;
			q[i].flag = 1;
		}
		qsort( q, n, sizeof(q[0]), cmp);
		int queuea[M];
		int queueb[M];
		int la = 0;
		int lb = 0;
		int rea = 0;
		int reb = 0;
		for( i=0; i<n; i++ )
		{
			if( q[i].flag == 0 )
			{
				for( j=0; j<la; j++ )
				{
					if( queuea[j] <= q[i].s )
					{
						queuea[j] = 9999999;
						break;
					}
				}
				if( j >= la )
				{
					rea ++;
				}
				queueb[ lb++ ] = q[i].t + t;
			}
			else
			{
				for( j=0; j<lb; j++ )
				{
					if( queueb[j] <= q[i].s )
					{
						queueb[j] = 9999999;
						break;
					}
				}
				if( j >= lb )
				{
					reb ++;
				}
				queuea[ la++ ] = q[i].t + t;
			}
		}
		printf("Case #%d: %d %d\n", casenum, rea, reb);
	}
	return 0;
}