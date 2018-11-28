/*
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <math.h>

using namespace std;

int main()
{
	freopen("out.txt","w", stdout);
	return 0;
}
*/

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <math.h>
#include <cassert>

using namespace std;

const int LMAX(128);
const int SMAX(128);
const int QMAX(1024);

int N, S, Q;

char engine[SMAX][LMAX];
int  query[QMAX];
int  best[QMAX][SMAX];

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt","w", stdout);
	scanf("%d", &N);
	for( int nCase=1; nCase<=N; nCase++ )
	{
		int i, j;
		scanf("%d", &S);
		fgets(engine[0], LMAX, stdin);

		for( i=0; i<S; i++ )
		{
			fgets(engine[i], LMAX, stdin);
		}

		scanf("%d", &Q);
		char buf[LMAX];
		fgets(buf, LMAX, stdin);

		for( i=0; i<Q; i++ )
		{
			fgets(buf, LMAX, stdin);
			for( j=0; j<S; j++ )
			{
				if( !strcmp(buf, engine[j]) )
				{
					query[i] = j;
					break;
				}
			}
			assert(j<S);
		}

		for( i=0; i<S; i++ )
		{
			best[0][i] = 0;
		}

		for( i=1; i<=Q; i++ )
		{
			for( j=0; j<S; j++ )
			{
				if( j!=query[i-1] )
				{
					best[i][j] = best[i-1][j]<best[i-1][query[i-1]]+1? best[i-1][j] : best[i-1][query[i-1]]+1;
				}
			}
			best[i][query[i-1]] = QMAX;
		}

		int min = QMAX;
		for( i=0; i<S; i++ )
		{
			if( best[Q][i] < min )
			{
				min = best[Q][i];
			}
		}

		printf("Case #%d: %d\n", nCase, min);
	}
	return 0;
}
