#include <cstdio>
#include <cstring>
#include <math.h>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
#include <map>
#include <cassert>

using namespace std;

const int NMAX(1024);
const int MMAX(128);

__int64 A[MMAX];
int seq[NMAX];
int cc[NMAX];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int N, n, m, X, Y, Z;
	scanf("%d", &N);
	for( int nCase=1; nCase<=N; nCase++ )
	{
		scanf("%d%d%d%d%d", &n, &m, &X, &Y, &Z);
		for( int i=0; i<m; i++ )
		{
			scanf("%I64d", &A[i]);
		}
		for( int i=0; i<n; i++ )
		{
			seq[i] = A[i%m];
			A[i%m] = ((__int64)X*A[i%m]+(__int64)Y*(i+1)) % Z;
		}
		memset(cc, 0, sizeof(cc));
		for( int i=0; i<n; i++ )
		{
			cc[i] = 1;
			for( int j=0; j<i; j++ )
			{
				if( seq[j]<seq[i] )
				{
					cc[i] += cc[j];
					cc[i] %= 1000000007;
				}
			}
		}
		__int64 sum = 0;
		for( int i=0; i<n; i++ )
		{
			sum += cc[i];
			sum %= 1000000007;
		}
		printf("Case #%d: %I64d\n", nCase, sum);
	}
	return 0;
}
