#include <cstdio>
#include <map>
#include <utility>

const int MAX_N = 10005;
int N, T;
std::map<std::pair<int, int>, bool> troll;
//dist, len
std::pair<int, int> lens[MAX_N];

bool dp(int prev, int cur) {
	std::pair<int, int> cstate(prev, cur);
	if (troll.find(cstate) != troll.end()) return troll[cstate];

	if (cur == N) return true;

	int clen;
	if (prev == -1) clen = std::min(lens[cur].second, lens[cur].first);
	else clen = std::min(lens[cur].second, lens[cur].first-lens[prev].first);
	for (int i = cur+1; i <= N; ++i) {
		if (clen < lens[i].first-lens[cur].first) break;
		if (dp(cur, i)) {
			troll[cstate] = true;
			return true;
		}
	}
	troll[cstate] = false;
	return false;
}

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d %d", &lens[i].first, &lens[i].second);
		}
		scanf("%d", &lens[N].first);
		lens[N].second = 0;
		troll.clear();

		printf("Case #%d: %s\n", t, dp(-1, 0) ? "YES" : "NO");
	}

}