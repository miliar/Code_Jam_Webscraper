#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

const int MAXN = 1024;

int N;
double W, L;
pair <double, int> r[MAXN];
pair <double, double> answer[MAXN];

bool DFS(int idx) {
	if (idx == -1) {
		return true;
	}
	for (int i = 0; i < 10; i++) {
		double x = rand() / (double)RAND_MAX * W, y = rand() / (double)RAND_MAX * L;
		bool valid = true;
		for (int j = idx + 1; j < N; j++) {
			if (hypot(x - answer[r[j].second].first, y - answer[r[j].second].second) < r[idx].first + r[j].first) {
				valid = false;
				break;
			}
		}
		if (!valid) continue;
		answer[r[idx].second] = make_pair(x, y);
		if (DFS(idx - 1)) {
			return true;
		}
	}
	return false;
}

void solve() {
	int n = N;
/*	if (n > 0) {
		answer[r[--n].second] = make_pair(0, 0);
	} else {
		return ;
	}
	if (n > 0) {
		answer[r[--n].second] = make_pair(W, L);
	} else {
		return ;
	}
	if (n > 0) {
		answer[r[--n].second] = make_pair(W, 0);
	} else {
		return ;
	}
	if (n > 0) {
		answer[r[--n].second] = make_pair(0, L);
	} else {
		return ;
	}*/
	if (!DFS(n - 1)) {
//		assert(false);
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (i != j && hypot(answer[r[i].second].first - answer[r[j].second].first, answer[r[i].second].second - answer[r[j].second].second) < r[i].first + r[j].first) {
				printf("N = %d fail @ %d %d\n", N, i, j);
				assert(false);
			}
		}
	}
}

int main() {
	int taskNumber;
	scanf("%d", &taskNumber);
	for (int taskIdx = 0; taskIdx < taskNumber; taskIdx++) {
		scanf("%d%lf%lf", &N, &W, &L);
		for (int i = 0; i < N; i++) {
			scanf("%lf", &r[i].first);
			r[i].second = i;
		}
		sort(r, r + N);
		solve();
		printf("Case #%d:", taskIdx + 1);
		for (int i = 0; i < N; i++) {
			printf(" %.6lf %.6lf", answer[i].first, answer[i].second);
		}
		putchar('\n');
	}
	return 0;
}
