#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

#define MAX 105

int n;
char a[MAX][MAX];

double wp[MAX], owp[MAX], oowp[MAX];
int plays[MAX], wins[MAX];

double getWP(int who) {
	return double(wins[who])/plays[who];
}

double getWP_t(int who, int throwout) {
	int win = wins[who], play = plays[who];
	if (a[who][throwout]!='.') {
		--play;
		win -= (a[who][throwout]=='1');
	}
	return double(win)/play;
}

double getOWP(int who) {
	int num = 0;
	double score = 0;
	for (int i = 0; i < n; ++i) {
		if (a[who][i] != '.') {
			score += getWP_t(i, who);
			++num;
		}
	}
	return score/num;
}

double getOOWP(int who) {
	int num = 0;
	double score = 0;
	for (int i = 0; i < n; ++i) {
		if (a[who][i] != '.') {
			score += owp[i];
			++num;
		}
	}
	return score/num;
}

void doCnts() {
	for (int i = 0; i < n; ++i) {
		int play = 0, win = 0;
		for (int j = 0; j < n; ++j) {
			if (a[i][j] != '.') ++play;
			if (a[i][j] == '1') ++win;
		}
		plays[i] = play;
		wins[i] = win;
	}
}

void doWPs() {
	for (int i = 0; i < n; ++i) {
		wp[i] = getWP(i);
	}
}

void doOWPs() {
	for (int i = 0; i < n; ++i) {
		owp[i] = getOWP(i);
	}
}

void doOOWPs() {
	for (int i = 0; i < n; ++i) {
		oowp[i] = getOOWP(i);
	}
}

void solve() {
	doCnts();
	doWPs();
	doOWPs();
	doOOWPs();
	for (int i = 0; i < n; ++i) {
		double rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
		printf("%.12lf\n", rpi);
	}
}

void input() {
	memset(wp, -1, sizeof(wp));
	memset(owp, -1, sizeof(owp));
	memset(oowp, -1, sizeof(oowp));
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%s", a[i]);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i) {
		input();
		printf("Case #%d:\n", i+1);
		solve();
	}
}

