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

int freq[NMAX];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int N, P, K, L;
	scanf("%d", &N);
	for( int nCase=1; nCase<=N; nCase++ )
	{
		scanf("%d%d%d", &P, &K, &L);
		for( int i=0; i<L; i++ )
		{
			scanf("%d", &freq[i]);
		}
		sort(freq, freq+L);
		__int64 min = 0;
		for( int i=L-1; i>=0; i-- )
		{
			int times = (L-1-i)/K+1;
			min += times*freq[i];
		}
		printf("Case #%d: %I64d\n", nCase, min);
	}
	return 0;
}
