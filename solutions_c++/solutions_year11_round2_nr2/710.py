#include <stdlib.h>
#include <stdio.h>
#include <stack>

using namespace std;

typedef struct
{
	double begin;
	double end;
} BE;

int p[200];
int v[200];
BE be[200];
stack<int> stb;

int main()
{
	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );

	int t, i;
	int n, d;
	int j;
	double htd;
	double avd;
	double maxd;
	int begin;

	for( scanf( "%d", &t ), i = 1; i <= t; ++i )
		{
		while( !stb.empty() ) stb.pop();
		scanf( "%d%d", &n, &d );
		maxd = 0.0;
		for( j = 0; j < n; ++j )
			{
			scanf( "%d%d", &p[j], &v[j] );
			htd = 0.5 * (v[j] - 1) * d;
			be[j].begin = p[j] - htd;
			be[j].end = p[j] + htd;
			if( htd > maxd )
				{
				maxd = htd;
				}//end if
			}//end for
		for( j = 1; j < n; ++j )
			{
			if( be[j-1].end + d > be[j].begin + 0.1 )
				{
merge:			if( stb.empty() )
					{
					begin = 0;
					}
				else{
					begin = stb.top() + 1;
					}//end if
				avd = ( p[begin] - be[begin].begin  + be[j].end - p[j] +  be[j-1].end + d - be[j].begin ) * 0.5;
				be[begin].begin = p[begin] - avd;
				be[j].end = p[j] + avd;
				if( avd > maxd )
					{
					maxd = avd;
					}//end if
				if( !stb.empty() && be[stb.top()].end + d > be[j].begin + 0.1 )
					{
					stb.pop();
					goto merge;
					}//end if
				}
			else if( be[j-1].end + d < be[j].begin - 0.1 )
				{
				stb.push( j - 1 );
				}//end for
			}//end for
		printf( "Case #%d: %.08lf\n", i, maxd );
		}//end for

	return 0;
}
