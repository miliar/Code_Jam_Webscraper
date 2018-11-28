#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <map>
#include <vector>
#include <math.h>
using namespace std;

#define PN 36
int _p[PN], _q, _r;
void pinit() { signal(SIGCHLD, SIG_IGN); }
void pblock(int p = _p[_q]) { while (p && !kill(p, 0)) usleep(1e4L); }
int pfork() {
	_r = (_q + 1) % PN; pblock(_p[_r]);
	if (_p[_r] = fork()) return _q = _r, 1; return 0;
}
void pexit() { fflush(stdout); exit(0); }





int N;
int L[1024], P[1024];

void input() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) scanf("%d", &L[i]);
	for (int i = 0; i < N; i++) scanf("%d", &P[i]);
}

void solve(int case_x) {
	vector< pair<double, int> > order;
	for (int i = 0; i < N; i++) {
		order.push_back(make_pair(log(1.0 - P[i] / 100.0) / L[i] + i * 1e-8, i));
	}
	sort(order.begin(), order.end());
	pblock();
	printf("Case #%d: ", case_x);
	for (int i = 0; i < order.size(); i++) {
		printf(" %d", order[i].second);
	}
	puts("");
}

int main() {
	int case_number;
	scanf("%d", &case_number);
	pinit();
	for (int case_x = 1; case_x <= case_number; case_x++) {
		input();
		if (pfork()) continue;
		solve(case_x);
		pexit();
	}
	pblock();
	return 0;
}
