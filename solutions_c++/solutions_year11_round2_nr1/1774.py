#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
const int maxn = 101;

int main() {
	int T;
	freopen("A-large.in", "r", stdin);
	scanf("%d", &T);
	int n;
	char buf[maxn][maxn];
	double total[maxn];
	double win[maxn];
	double wp[maxn];
	double owp[maxn];
	double oowp[maxn];
	for (int t = 1; t <= T; t++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s", buf[i]);
			total[i] = .0;
			win[i] = .0;
			for (int j = 0; buf[i][j]; j++) if (buf[i][j] != '.') {
				total[i] += 1.0;
				win[i] += 1.0 * (buf[i][j] - '0');
			}
			wp[i] = win[i] / total[i];
		}
		for (int i = 0; i < n; i++) {
			double tmp = .0;
			for (int j = 0; j < n; j++) {
				if (buf[i][j] == '0') 
					tmp += (win[j] - 1.0) / (total[j] - 1.0);
				else if (buf[i][j] == '1') 
					tmp += win[j] / (total[j] - 1.0);
			}
			owp[i] = (tmp / total[i]);
		}

		for (int i = 0; i < n; i++) {
			double tmp = .0;
			for (int j = 0; j < n; j++)  if (buf[i][j] != '.') 
				tmp += owp[j];
			oowp[i] = (tmp / total[i]);
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < n; i++) 
			printf("%lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);

	}
	return 0;
}
