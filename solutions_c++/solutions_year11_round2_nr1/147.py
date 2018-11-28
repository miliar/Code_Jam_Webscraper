#include <cstdio>
#include <vector>

using namespace std;

const int MAX_N = 100 + 5;

int T;
char a[MAX_N][MAX_N];
int main() {
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t ++) {
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i ++) {
			scanf("%s", a[i]);
		}
		vector<int> wins(N), played(N);
		vector<double> wp(N), owp(N), oowp(N);
		for (int i = 0; i < N; i ++) {
			for (int j = 0; j < N; j ++) {
				if (a[i][j] != '.') {
					played[i] ++;
					if (a[i][j] == '1') {
						wins[i] ++;
					}
				}
			}
			wp[i] = wins[i] / (double)played[i];
		}
		for (int i = 0; i < N; i ++) {
			double cur = 0;
			int cnt = 0;
			for (int j = 0; j < N; j ++) {
				if (a[i][j] != '.') {
					cnt ++;
					cur += (wins[j] - (a[j][i] == '1')) / (played[j] - 1.);
				}
			}
			owp[i] = cur / cnt;
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < N; i ++) {
			double cur = 0;
			int cnt = 0;
			for (int j = 0; j < N; j ++) {
				if (a[i][j] != '.') {
					cnt ++;
					cur += owp[j];
				}
			}
			oowp[i] = cur / cnt;
			double res = wp[i] / 4 + owp[i] / 2 + oowp[i] / 4;
			printf("%.10lf\n", res);
		}
	}
}