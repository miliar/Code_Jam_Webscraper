#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int n;
char res[111][111];

double wp(int i, int skip) {
	int wins = 0;
	int cnt = 0;
	for (int j = 0; j < n; ++j) {
		if (j == skip) continue;
		if (res[i][j] == '1') ++wins;
		if (res[i][j] != '.') ++cnt;
	}
	return (double)wins / cnt;
}

double owp(int i) {
	double sum = 0;
	int cnt = 0;
	for (int j = 0; j < n; ++j) {
		if (res[i][j] != '.') {
			sum += wp(j, i);
			++cnt;
		}
	}
	return sum/cnt;
}

double oowp(int i) {
	double sum = 0;
	int cnt = 0;
	for (int j = 0; j < n; ++j) {
		if (res[i][j] != '.') {
			sum += owp(j);
			++cnt;
		}
	}
	return sum/cnt;
}

int main() {
	int t;
	scanf("%d\n", &t);
	for (int tt = 1; tt <= t; ++tt) {
		scanf("%d\n", &n);
		for (int i = 0; i < n; ++i) {
			gets(res[i]);
		}

		printf("Case #%d:\n", tt);
		for (int i = 0; i < n; ++i) {
			printf("%.9lf\n", 0.25*wp(i, -1) + 0.5*owp(i) + 0.25*oowp(i));
		}
	}
}
