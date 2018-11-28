#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define FORI(it, x) for (typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
#define PB push_back
#define MP make_pair
#define x first
#define y second

typedef long long llong;
typedef vector <string> VS;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 0x3f3f3f3f;
const int NMAX = 1 << 14;

int N, T[NMAX], DP[NMAX][2], C[NMAX];

void go(int k) {
	if (k > (N - 1) / 2) {
		DP[k][T[k]] = 0;
		DP[k][!T[k]] = INF;
		return;
	}

	int st, dr, c;
	st = 2 * k;
	dr = 2 * k + 1;

	go(st); go(dr);

	c = (T[k] == 1);

	if (C[k] == 1 || c == 0) {
		DP[k][0] = min(DP[k][0], DP[st][0] + DP[dr][0] + c);
		DP[k][1] = min(DP[k][1], DP[st][1] + DP[dr][1] + c);
		DP[k][1] = min(DP[k][1], DP[st][0] + DP[dr][1] + c);
		DP[k][1] = min(DP[k][1], DP[st][1] + DP[dr][0] + c);
	}

	c = (T[k] == 0);

	if (C[k] == 1 || c == 0) {
		DP[k][0] = min(DP[k][0], DP[st][0] + DP[dr][0] + c);
		DP[k][0] = min(DP[k][0], DP[st][1] + DP[dr][0] + c);
		DP[k][0] = min(DP[k][0], DP[st][0] + DP[dr][1] + c);
		DP[k][1] = min(DP[k][1], DP[st][1] + DP[dr][1] + c);

	}

//	printf("%d => 0 %d 1 %d\n", k, DP[k][0], DP[k][1]);
}

int main(void) {
	freopen("large.in", "rt", stdin);
	freopen("test.out", "wt", stdout);

	int cn, CN;
	int i, V;

	scanf(" %d", &CN);

	for (cn = 1; cn <= CN; ++cn) {

		scanf(" %d %d", &N, &V);

		for (i = 1; i <= (N - 1) / 2; ++i)
			scanf(" %d %d", T + i, C + i);
		
		for (i = (N - 1) / 2 + 1; i <= N; ++i)
			scanf(" %d", T + i);

		memset(DP, 0x3f, sizeof(DP));
		go(1);
		
		printf("Case #%d: ", cn);
		if (DP[1][V] == INF)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", DP[1][V]);
	}

	return 0;
}


