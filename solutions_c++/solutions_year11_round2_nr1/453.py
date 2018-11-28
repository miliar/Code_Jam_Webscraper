#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

char a[150][150];
double wp[150], owp[150], oowp[150], zs[150], os[150];

void solve() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%s", a[i]);
	for (int i = 0; i < n; ++i) {
		zs[i] = std::count(a[i], a[i]+n, '0');
		os[i] = std::count(a[i], a[i]+n, '1');
		wp[i] = os[i] / (zs[i] + os[i]);
	}
	for (int i = 0; i < n; ++i) {
		double sum = 0;
		double cnt = 0;
		for (int j = 0; j < n; ++j) if (a[i][j] != '.') {
			double num = os[j];
			double den = os[j] + zs[j];
			if (a[j][i] == '0')
				--den;
			else if (a[j][i] == '1')
				--den, --num;
			sum += num / den;
			++cnt;
		}
		owp[i] = sum / cnt;
	}
	for (int i = 0; i < n; ++i) {
		double sum = 0;
		double cnt = 0;
		for (int j = 0; j < n; ++j) if (a[i][j] != '.') {
			sum += owp[j];
			cnt++;
		}
		oowp[i] = sum / cnt;
	}
	for (int i = 0; i < n; ++i) 
		printf("%.9lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);

}

char s[1024];
int main(int argc, char* argv[]) {
    freopen(argv[1], "r", stdin);
    strcat(s, argv[1]);
    strcat(s, ".out");
    freopen(s, "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d:\n", i+1);
		solve();
    }
        
}