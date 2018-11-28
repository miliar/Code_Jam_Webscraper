#include <cstdio>
#include <cmath>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define MP(x, y) make_pair(x, y)
#define forn(i, n) for(int i = 0; i < n; i++)

typedef long long int64;

#define TASK "c"

const int MAXN = 2000;

int R, k, N;
int g[MAXN], before[MAXN];
int64 cost[MAXN];
bool was[MAXN];

pair<int64, int> next(int start) {
	int index = start;
	int64 loaded = 0;
	if (g[start] > k) return MP(0, start);
	do {
		loaded += g[index];
		index = (index + 1) % N;
	} while (index != start && loaded + g[index] <= k);
	return MP(loaded, index);
}

pair<int64, int> dfs(int start) {
	if (was[start]) {
		return MP(0, 0);
	}
	was[start] = true;
	pair<int64, int> result = dfs(before[start]);
	return MP(result.first + cost[start], result.second + 1);
}

int main() {
	freopen(TASK ".in", "rt", stdin);
	freopen(TASK ".out", "wt", stdout);
	int T;
	scanf("%d", &T);
	forn(t, T) {
		scanf("%d%d%d", &R, &k, &N);
		forn(i, N) scanf("%d", &g[i]);

		//strange case
		for (int i = 0, j = g[0]; (i < N) && (i < R); j += g[++i]) {
			if (g[i] > k) {
				return 0 * printf("%d\n", j);
			}
		}

		memset(before, -1, sizeof(before));
		memset(cost, 0, sizeof(cost));

		int64 answer = 0;
		int steps_done = 0, start = 0;
		bool is_cycle = false;
///		
		for (; steps_done < R && !is_cycle; steps_done++) {
			pair<int64, int> result = next(start);
			is_cycle = (before[result.second] >= 0);

			before[result.second] = start;
			cost[result.second] = result.first;
			start = result.second;
			answer += result.first;

//			printf("+ %d\n", (int)result.first);
		}

/*		printf("START : %d\n", start);
		forn(i, N) {
			printf("%d ", before[i]);
		}
		printf("\n");
*/
		memset(was, 0, sizeof(was));
		pair<int64, int> cycle = dfs(start);

//		printf("CYCLE\n| COST : %d\n| LENGTH : %d\n", (int)cycle.first, cycle.second);

		int64 cycles_number = ((int64)R - steps_done) / (int64)cycle.second;

//		printf("CYCLES NUMBER : %d\n", cycles_number);

		answer += cycles_number * cycle.first;
		steps_done += cycles_number * cycle.second;
////
		for (; steps_done < R; steps_done++) {
			pair<int64, int> result = next(start);
			start = result.second;
			answer += result.first;		
		}

		cout << "Case #" << t + 1 << ": " << answer << endl;
	}


	return 0;
}