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

int M, V;
char change[10010];
char op[10010];
int inter_num;
int leaf_num;
int val_start;

int dp[10010][2];

const int inf = 10020;

void update(int &a, int b) {
	if (b == inf)
		return;
	if (b < a)
		a = b;
}

void solve(int id) {
	for (int i=M; i>=val_start; --i) {
		dp[i][op[i]] = 0;
		dp[i][1 - op[i]] = inf;
	}
	for (int i=val_start-1; i>=1; --i) {
		dp[i][0] = dp[i][1] = inf;
		//or
		if (!(dp[i+i][0] == inf || dp[i+i+1][0] == inf) ) {
			if (op[i] == 0)
				update(dp[i][0] ,dp[i+i][0] + dp[i+i+1][0]);
			else if(change[i] == 1)
				update(dp[i][0] ,dp[i+i][0] + dp[i+i+1][0] + 1);
		}

		if (!(dp[i+i][1] == inf && dp[i+i+1][1] == inf) ) {
			if (op[i] == 0)
				update(dp[i][1],  min(dp[i+i][1], dp[i+i+1][1]) );
			else if (change[i] == 1) 
				update(dp[i][1],  min(dp[i+i][1], dp[i+i+1][1]) + 1);
			
		}
	
		// and
		if (!(dp[i+i][0] == inf && dp[i+i+1][0] == inf) ) {
			if (op[i] == 1)
				update(dp[i][0], min(dp[i+i][0], dp[i+i+1][0]));
			else if (change[i] == 1)
				update(dp[i][0], min(dp[i+i][0], dp[i+i+1][0]) + 1);

		}

		if (!(dp[i+i][1] == inf || dp[i+i+1][1] == inf) ) {
			if (op[i] == 1)
				update(dp[i][1], dp[i+i][1] + dp[i+i+1][1] );
			else if (change[i] == 1)
				update(dp[i][1], dp[i+i][1] + dp[i+i+1][1] + 1);
		}
		
	}

	printf("Case #%d: ", id);
	if (dp[1][V] == inf)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", dp[1][V]);
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	int N;
	scanf("%d", &N);
	for (int id=1; id<=N; ++id) {
		scanf("%d %d", &M, &V);
		inter_num = (M - 1) / 2;
		for (int i=1; i<= inter_num; ++i) {
			scanf("%d %d", op + i, change + i);
		}
		leaf_num = (M + 1) / 2;
		val_start = inter_num + 1;
		for (int i=0; i<leaf_num; ++i) {
			scanf("%d", op + val_start + i);
		}
		solve(id);
	}
	return 0;
}