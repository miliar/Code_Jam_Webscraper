#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////

char mat[16][16];
int M, N;

int dp[101][1<<11];

void update(int& x, int val) {
	if (x == -1)
		x = val;
	else {
		if (x < val)
			x = val;
	}
}

void solve(int tid) {
	int total = M * N;
	memset(dp, -1, sizeof dp);
	int nbit = N + 1;
	int limit = 1 << (N + 1);
	memset(dp, -1, sizeof(dp) );
	dp[0][0] = 0;
	for (int pos=0; pos<total; ++pos) {
		for (int mask=0; mask<limit; ++mask) if (dp[pos][mask] != -1){
			int r= pos / N;
			int c = pos % N;			
			update(dp[pos+1][mask >> 1], dp[pos][mask]);
			
			if (mat[r][c] == '.') {
				bool flag = true;
				if (c>0 && r>0 && (mask & 1) )
					continue;
				if (c>0 && (mask & (1 << N)) )
					continue;
				if (c < N-1 && r>0 && (mask & (1 << 2) ) )
					continue;
				update(dp[pos+1][(mask >> 1) | (1<<N)], dp[pos][mask]+1);
			}
		}
	}

	int res = 0;
	for (int i=0; i<limit; ++i) {
		res = max(res, dp[total][i]);
	}
	printf("Case #%d: %d\n", tid, res);
	
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		scanf("%d %d", &M, &N);
		for(int i=0; i<M; ++i) {
			scanf("%s", mat+i);
		}
		solve(tid);
	}
	return 0;
}