#include <stdio.h>
#include <stdlib.h>

int train[2][1000];

struct Trip{
	int start;
	int end;
	int flag;
}trip[205];

int cmp ( const void *a, const void * b)
{
	return ((Trip*)a)->start-((Trip*)b)->start;
}
int main ()
{
	freopen("a.in","r", stdin);
	freopen("a.out","w", stdout);
	int T;
	int time;
	int na, nb;
	int i, j, k;
	scanf("%d",&T);
	for (int t = 1; t<=T; t++ )
	{
		scanf("%d", &time );
		scanf("%d %d", &na, &nb );
		for ( i=0; i<na+nb; i++ )
		{
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d );
			trip[i].start = a*100+b;
			trip[i].end	 = c*100+d;
			if ( i<na )
				trip[i].flag = 0;
			else
				trip[i].flag = 1;
		}
		qsort( trip, na+nb, sizeof(trip[0]), cmp );
		int num[2]={0};
		int ans[2]={0};
		for ( i=0; i<na+nb; i++ )
		{
			int p = 0;
			int temp = trip[i].flag;
			for ( j=0; j<num[temp]; j++ )
			{
				
				if ( train[ temp ][j]<=trip[i].start )
				{
					train[ 1-temp][ num[1-temp]++] = trip[i].end+time ;
					for (k=j; k<num[temp]-1; k++ )
						train[temp][k] = train[temp][k+1];
					num[temp]--;
					p = 1;
					break;
				}
			}
			if ( p==0 )
			{
				train[ 1-temp][ num[1-temp]++] = trip[i].end+time ;
				ans[temp]++;
			}
		}
		printf("Case #%d: %d %d\n",t,ans[0],ans[1]);
	}
	return 0;
}