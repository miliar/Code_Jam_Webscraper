#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <map>
using namespace std;

#define PN 16
int _p[PN], _q;
void pblock(int p = _p[_q]) { while (p && !kill(p, 0)) usleep(1e4L); }

int case_x, case_n;
int X, S, R, T, N;
int B[1024], E[1024], W[1024];

int input() {
	scanf("%d%d%d%d%d",&X, &S, &R, &T, &N);
	for (int i = 0; i < N; i++) {
		scanf("%d%d%d", &B[i], &E[i], &W[i]);
	}
	return 1;
}

int solve() {
	map<int, int> l;
	int sum = 0;
	for (int i = 0; i < N + 1; i++) {
		int s = i ? E[i - 1] : 0;
		int e = (i != N) ? B[i] : X;
		sum += e - s;
	}
	l[0] = sum;
	for (int i = 0; i < N; i++) {
		l[W[i]] += E[i] - B[i];
	}
	double ans = 0.0;
	double last_run = T;
	for (__typeof(l.begin()) it = l.begin(); it != l.end(); it++) {
		double speed = it->first, dist = it->second;
//		printf("speed: %lf, dist: %lf, last_run: %lf\n", speed, dist, last_run);
		if (last_run < 1e-9) {
			ans += dist / (speed + S);
		} else if (dist / (speed + R) < last_run + 1e-9) {
			last_run -= dist / (speed + R);
			ans += dist / (speed + R);
		} else {
			ans += last_run;
			dist -= last_run * (speed + R);
			ans += dist / (speed + S);
			last_run = 0.0;
		}
	}
	// Block before writing
	pblock();
	printf("Case #%d: %.9lf\n", case_x, ans);
}

int main() {
	int case_n; scanf("%d", &case_n);
	signal(SIGCHLD, SIG_IGN);
	for (case_x = 1; case_x <= case_n; case_x++) {
		input();
		int _r = (_q + 1) % PN;
		pblock(_p[_r]);
		if (_p[_r] = fork()) _q = _r;
		else return solve();
	}
	pblock();
	return 0;
}
