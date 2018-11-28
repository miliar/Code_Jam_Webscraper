#include <stdio.h>
#include <algorithm>

using namespace std;

int g[2000];
long long sg[2000];
long long sum[2001];
int used[1000];

int main()
{
	freopen( "C.in", "r", stdin );
	freopen( "C.out", "w", stdout );

	int t, r, k, n;
	int i, j;
	int st, nst;
	int period;
	long long euro, amount;

	scanf( "%d", &t );
	for( i = 1; i <= t; ++i )
		{
		scanf( "%d%d%d", &r, &k, &n );
		for( j = 0; j < n; ++j )
			{
			scanf( "%d", &g[j] );
			g[j+n] = g[j];
			}//end for

		sg[0] = g[0];
		for( j = 1; j < (n<<1); ++j )
			{
			sg[j] = sg[j-1] + g[j];
			}//end for

		for( j = 0; j < n; ++j )
			{
			used[j] = -1;
			}//end for
		st = 0;
		sum[0] = 0;
		for( j = 1; used[st] < 0; st = nst, ++j )
			{
			used[st] = j;
			nst = upper_bound( sg + st, sg + (n<<1), sg[st] - g[st] + k ) - sg;
			if( nst > st + n )
				{
				nst = st + n;
				}//end if
			sum[j] = sum[j-1] + sg[nst-1] - sg[st] + g[st];
			if( nst >= n )
				{
				nst -= n;
				}//end if
			}//end for
		period = j - used[st];
		euro = sum[j-1] - sum[used[st]-1];
		amount = ( (r - used[st] + 1) / period ) * euro + sum[used[st] - 1 + (r - used[st] + 1) % period];
		printf( "Case #%d: %lld\n", i, amount );
		}//end for

	return 0;
}
