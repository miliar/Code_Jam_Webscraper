#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define PI 2*acos(0)
#define EPS 1e-7
#define LL long long
#define INF 1000000000
#define PQ priority_queue

typedef pair<int, int> i2;
typedef pair<int, i2> i3;
typedef pair<i2, i2> i4;

int tc, N, score[105], S, P, dp[105][105];

int surprise(int idx, bool b) {
	
	int x;
	
	if (b) {
		if (score[idx] - 4 >= 0 && (score[idx] - 4) % 3 == 0) {
			x = (score[idx] - 4) / 3;
			if (x >= P || x + 2 >= P) return 1;
		} else if (score[idx] - 2 >= 0 && (score[idx] - 2) % 3 == 0) {
			x = (score[idx] - 2) / 3;
			if (x >= P || x + 2 >= P) return 1;
		} else if (score[idx] - 3 >= 0 && (score[idx] - 3) % 3 == 0) {
			x = (score[idx] - 3) / 3;
			if (x >= P || x + 1 >= P || x + 2 >= P) return 1;
		}
		return 0;
	} else {
		if (score[idx] % 3 == 0) {
			x = score[idx] / 3;
			if (x >= P) return 1;
		} else if (score[idx] - 1 >= 0 && (score[idx] - 1) % 3 == 0) {
			x = (score[idx] - 1) / 3;
			if (x >= P || x + 1 >= P) return 1;
		} else if (score[idx] - 2 >= 0 && (score[idx] - 2) % 3 == 0) {
			x = (score[idx] - 2) / 3;
			if (x >= P || x + 1 >= P) return 1;
		}
		return 0;
	}
}

int main() {

	//freopen("file.in", "r", stdin);
	
	scanf("%d", &tc);
	int t = 0;
	while (tc--) {
		scanf("%d %d %d", &N, &S, &P);
		for (int i = 0; i < N; i++) scanf("%d", &score[i]);
		
		// for (int i = 0; i < N; i++) printf("score[%d] = %d\n", i, score[i]);
		
		memset(dp, 0, sizeof dp);
		for (int i = 1; i <= N; i++)
			for (int j = 0; j <= S; j++)
				dp[i][j] = max(dp[i - 1][j] + surprise(i - 1, 0), (j > 0) ? dp[i - 1][j - 1] + surprise(i - 1, 1) : 0);
		
		/*
		for (int i = 1; i <= N; i++)
			for (int j = 0; j <= S; j++) printf("dp[%d][%d] = %d\n", i, j, dp[i][j]);
		*/
		
		printf("Case #%d: %d\n", ++t, dp[N][S]);
	}
	
	return 0;
}
