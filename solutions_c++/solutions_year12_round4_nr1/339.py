#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <map>
#include <algorithm>
using namespace std;

#define PN 48
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
int N;
int D[10001], L[10001], A[10001];
int G;

int input() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d%d", &D[i], &L[i]);
		A[i] = -1;
	}
	scanf("%d", &G);
	return 0;
}

int solve(int case_x) {
	bool result = false;
	A[0] = D[0];
	D[N] = G;
	L[N] = 0;
	A[N] = -1;
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j <= N; j++) {
			if (D[j] <= D[i] + A[i]) {
				A[j] = max(A[j], min(D[j] - D[i], L[j]));
			} else break;
		}
	}
	result = (A[N] == 0);
	// Program to solve
	// Block before writing
	pblock();
	printf("Case #%d: %s\n", case_x, result ? "YES" : "NO");
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
