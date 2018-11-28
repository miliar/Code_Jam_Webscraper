#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;

#define PN 6
int _p[PN], _q, _r;
// main に入った直後に呼ぶ
void pinit() { signal(SIGCHLD, SIG_IGN); }
// 子プロセスの出力直前と親プロセスの終了直前に呼ぶ
void pblock(int p = _p[_q]) { while (p && !kill(p, 0)) usleep(1e4L); }
// 親プロセスの入力直後に呼ぶ
int pfork() {
	_r = (_q + 1) % PN; pblock(_p[_r]);
	if (_p[_r] = fork()) return _q = _r, 1; return 0;
}
// 子プロセスの終了を行う
void pexit() { fflush(stdout); exit(0); }

/// 以下サンプル
ll W, H, N, R[100001];
ll X[100001], Y[100001];
int sw;

int input() {
	scanf("%lld%lld%lld", &N, &W, &H);
	for (int i = 0; i < N; i++) scanf("%lld", &R[i]);
	return 0;
}

int rank(ll val) {
	ll th = 1;
	for (int i = 0; i < 30; i++, th *= 2) {
		if (val <= th) return i;
	}
}

int solve(int case_x) {
	vector< pair<ll, int> > Rs;
	for (int i = 0; i < N; i++) Rs.push_back(make_pair(R[i], i));
	sort(Rs.rbegin(), Rs.rend());
	sw = 0;
	if (W < H) { swap(H, W); sw = 1; }
	// TODO
	ll xx = -Rs[0].first;
	for (int i = 0; i < N;) {
		int hblocks = H / Rs[i].first / 2 + 1;
		ll yy = -Rs[i].first;
		ll oxx = xx;
		for (int j = 0; j < hblocks && i < N; j++, i++) {
			X[Rs[i].second] = max((ll)0, oxx + Rs[i].first);
			Y[Rs[i].second] = max((ll)0, yy + Rs[i].first);
			// printf("%lld %lld\n", xx, yy);
			xx = max(xx, X[Rs[i].second] + Rs[i].first);
			yy = max(yy, Y[Rs[i].second] + Rs[i].first);
		}
	}
	//
	if (sw) {
		swap(H, W);
		for (int i = 0; i < N; i++) {
			swap(X[i], Y[i]);
		}
	}
	for (int i = 0; i < N; i++) {
		if (X[i] < 0 || W < X[i] || Y[i] < 0 || H < Y[i]) {
			fprintf(stderr, "%d: %d-th is out-of-range\n", case_x, i);
		}
		for (int j = 0; j < i; j++) {
			if ((X[j] - X[i]) * (X[j] - X[i]) + (Y[j] - Y[i]) * (Y[j] - Y[i]) < (R[i] + R[j]) * (R[i] + R[j])) {
				fprintf(stderr, "%d: %d and %d are intersected\n", case_x, i, j);
			}
		}
	}
	pblock();
	printf("Case #%d:", case_x);
	for (int i = 0; i < N; i++) {
		printf(" %.1f %.1f", (double)X[i], (double)Y[i]);
	}
	printf("\n");
}

int main() {
	int cases;
	scanf("%d", &cases);
	pinit();
	for (int case_x = 1; case_x <= cases; case_x++) {
		input();
		if (pfork()) continue;
		solve(case_x);
		pexit();
	}
	pblock();
	return 0;
}
