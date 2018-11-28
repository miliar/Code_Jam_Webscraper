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
		int A, N, M;
		scanf("%d%d%d", &N, &M, &A);
		if( A == N*M )
		{
			printf("%d %d %d %d %d %d\n", 0, 0, N, 0, 0, M);
		}
		else if( A>N*M )
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			int x1, y1, x2, y2;
			if( M<N )
			{
				int s = (A+M-1)/M*M;
				y1 = 1, x2 = s-A;
				y2 = M, x1 = s/M;
			}
			else
			{
				int s = (A+N-1)/N*N;
				y1 = 1, x2 = s-A;
				x1 = N, y2 = s/N;
			}
			printf("%d %d %d %d %d %d\n", 0, 0, x1, y1, x2, y2);
		}
	}
	return 0;
}
