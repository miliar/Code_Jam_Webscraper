#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <string>
#include <cassert>
typedef long long i64d;
typedef unsigned long long i64u;
using namespace std;

#define LOCAL

const int maxN = 10086;

int dist[maxN], len[maxN];
int N, D, yes;

void dfs(int idx, int dep)
{
	if( idx == N - 1 ) {
		if( dist[idx] + dep >= D )
			yes = 1;
		return ;
	}

	if( dist[idx] + dep >= D ) {
		yes = 1; return ;
	}

	if( yes ) return ;

	for(int i = idx + 1; i < N; i++)
		if( dist[idx] + dep >= dist[i] )
			dfs(i, min(dist[i] - dist[idx], len[i]));
}

int main()
{
#ifdef LOCAL
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif

	int nt, idx = 0;
	scanf("%d", &nt);
	while( (nt --) > 0 ) {
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
			scanf("%d %d", dist + i, len + i);
		scanf("%d", &D);
		yes = 0;
		dfs(0, dist[0]);
		printf("Case #%d: %s\n", ++idx, yes ? "YES" : "NO");
	}


#ifdef LOCAL
	//system("pause");
#endif
	return 0;
}
