#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve(int it) {
	int n;
	scanf("%d", &n);
	vector<string> r(n);
	for (int i = 0; i < n; i++) {
		cin >> r[i];
	}
	vector<double> wp(n);
	for (int i = 0; i < n; i++) {
		wp[i] = 0.0;
		int cnt = 0;
		for (int j = 0; j < n; j++) {
			if (r[i][j] == '1') {
				wp[i]++;
			}
			if (r[i][j] != '.') {
				cnt++;
			}
		}
		wp[i] /= cnt;
	}
	vector<double> owp(n);
	for (int i = 0; i < n; i++) {
		owp[i] = 0.0;
		int cnt = 0;
		for (int j = 0; j < n; j++) {
			if (r[i][j] != '.') {
				double tmp_wp = 0;
				int tmp_cnt = 0;
				for (int k = 0; k < n; k++) {
					if (k == i) continue;
					if (r[j][k] != '.') {
						tmp_cnt++;
						if (r[j][k] == '1') {
							tmp_wp++;
						}
					}
				}
				tmp_wp /= tmp_cnt;
				owp[i] += tmp_wp;
				cnt++;
			}
		}
		owp[i] /= cnt;
	}
	vector<double> oowp(n);
	for (int i = 0; i < n; i++) {
		oowp[i] = 0.0;
		int cnt = 0;
		for (int j = 0; j < n; j++) {
			if (r[i][j] != '.') {
				oowp[i] += owp[j];
				cnt++;
			}
		}
		oowp[i] /= cnt;
	}
	printf("\n");
	for (int i = 0; i < n; i++) {
		printf("%.20lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
}

int main() {
	int nt;
	scanf("%d", &nt);
	for (int it = 1; it <= nt; it++) {
		printf("Case #%d: ", it);
		solve(it);
	}
	return 0;
}
