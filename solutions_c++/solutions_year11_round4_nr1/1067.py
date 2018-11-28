#include <stdlib.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

double b[1000];
double e[1000];
double w[1000];
int o[1000];

bool compare( int a, int b )
{
	return w[a] < w[b];
}//end compare

int main()
{
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int t, i;
	double x, s, r, rt;
	int n;
	double nw;
	double ert;
	double time;
	int j;

	for( scanf( "%d", &t ), i = 1; i <= t; ++i )
		{
		scanf( "%lf%lf%lf%lf%d", &x, &s, &r, &rt, &n );
		nw = x;
		for( j = 0; j < n; ++j )
			{
			scanf( "%lf%lf%lf", &b[j], &e[j], &w[j] );
			o[j] = j;
			nw -= e[j] - b[j];
			}//end for
		sort( o, o + n, compare );
		time = 0;
		if( nw > 0 )
			{
			ert = nw / r;
			if( ert > rt )
				{
				time += rt;
				nw *= 1 - rt / ert;
				rt = 0;
				}
			else{
				time += ert;
				nw = 0;
				rt -= ert;
				}//end if
			}//end if
		if( nw > 0 )
			{
			time += nw / s;
			}//end if
		for( j = 0; j < n; ++j )
			{
			nw = e[o[j]] - b[o[j]];
			if( rt > 0 )
				{
				ert = nw / (r + w[o[j]]);
				if( ert > rt )
					{
					time += rt;
					nw *= 1 - rt / ert;
					rt = 0;
					}
				else{
					time += ert;
					nw = 0;
					rt -= ert;
					}//end if
				if( nw > 0 )
					{
					time += nw / (s + w[o[j]]);
					}//end if
				}
			else{
				time += nw / (s + w[o[j]]);
				}//end if
			}//end for

		printf( "Case #%d: %.08lf\n", i, time );
		}//end for

	return 0;
}
