#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <algorithm>
#include <math.h>

using namespace std;

typedef __int64 int64;

const int MMAX(10000+10);

int tree[MMAX], M, V;
int changable[MMAX];
int best[2][MMAX];

const int INF(100000000);


#define SUBMIT

int main()
{
	freopen("in.txt", "r", stdin);

#ifdef SUBMIT
	freopen("ans.txt", "w", stdout);
#endif

	int totCase;
	scanf("%d", &totCase);
	for( int nCase=1; nCase<=totCase; nCase++ )
	{
		printf("Case #%d: ", nCase);
		scanf("%d%d", &M, &V);
		for( int i=1; i<=(M-1)/2; i++ )
		{
			scanf("%d%d", &tree[i], &changable[i]);
		}
		for( int i=(M+1)/2; i<=M; i++ )
		{
			scanf("%d", &tree[i]);
			best[tree[i]][i] = 0;
			best[tree[i]^1][i] = INF;
		}
		for( int i=(M-1)/2; i>=1; i-- )
		{
			int lc = i*2, rc = i*2+1;
			if( tree[i]==0 ) //OR
			{
				best[1][i] = min(best[1][lc], best[1][rc]);
				best[0][i] = best[0][lc]+best[0][rc];
			}
			else //AND
			{
				best[1][i] = best[1][lc]+best[1][rc];
				best[0][i] = min(best[0][lc], best[0][rc]);
			}
			if( changable[i] )
			{
				if( tree[i]==0 ) //OR
				{
					int x = min(best[0][lc], best[0][rc])+1;
					if( x<best[0][i] )
					{
						best[0][i] = x;
					}
				}
				else //AND
				{
					int x = min(best[1][lc], best[1][rc])+1;
					if( x<best[1][i] )
					{
						best[1][i] = x;
					}
				}
			}
			if( best[0][i]>INF ) best[0][i] = INF;
			if( best[1][i]>INF ) best[1][i] = INF;
		}
		if( best[V][1]==INF )
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", best[V][1]);
		}
	}
	return 0;
}
