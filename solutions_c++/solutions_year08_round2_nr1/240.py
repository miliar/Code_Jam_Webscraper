#include <iostream>
#define MAXN 128

using namespace std;

struct Point 
{
	long long x, y;
};

Point p[MAXN];

int main (void)
{
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("1.out","w",stdout);
	int T;
	int Case = 0;
	long long n, A, B, C, D, x0, y0, M;
	int i, j, k;
	scanf ("%d",&T);
	while ( T -- )
	{
		Case ++;
		scanf ("%lld%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		p[0].x = x0;
		p[0].y = y0;
		for ( i = 1; i < n; i ++ )
		{
			x0 = (A*x0+B)%M;
			y0 = (C*y0+D)%M;
			p[i].x = x0;
			p[i].y = y0;
		}
		int ans = 0;
		for ( i = 0; i < n; i ++ )
		{
			for ( j = i+1; j < n; j ++ )
			{
				for ( k = j+1; k < n; k ++ )
				{
					if ( (p[i].x+p[j].x+p[k].x)%3 == 0 
						&& (p[i].y+p[j].y+p[k].y)%3 == 0 )
						ans ++;
				}
			}
		}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}