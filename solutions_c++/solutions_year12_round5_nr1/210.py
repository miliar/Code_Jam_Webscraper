#include <cstdio>
#include <utility>
#include <algorithm>

const int MAX_N = 1005;
int T, N;

struct Info {
	Info(int _t = -1, int _p = -1, int _i = -1) : time(_t), prob(_p), index(_i) {}
	int time, prob, index;

	bool operator<(const Info& c) const {
		if (prob != c.prob) return c.prob < prob;
		if (time != c.time) return c.time < time;
		return index < c.index;
	}
} troll[MAX_N];


int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &troll[i].time);
			troll[i].index = i;
		}
		for (int i = 0; i < N; ++i) {
			scanf("%d", &troll[i].prob);
		}
		printf("Case #%d:", t);
		std::sort(troll, troll+N);
		for (int i = 0; i < N; ++i) {
			printf(" %d", troll[i].index);
		}
		printf("\n");

	}
}