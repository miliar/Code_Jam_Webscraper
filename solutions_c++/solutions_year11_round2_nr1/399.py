#include <cstdio>
#include <cstring>

namespace gcj {
	using namespace std;

	const int maxn = 105;
	char mat[maxn][maxn];
	double WP[maxn];
	double WP_par[maxn][2];
	double OWP[maxn];
	double OOWP[maxn];
	
	void solve() {
		int t, n, c = 0;
		scanf("%d", &t);
		while (t --) {
			c ++;
			scanf("%d", &n);
			for (int i = 0; i < n; i ++)
				scanf("%s", mat[i]);
				
			// WP
			for (int i = 0; i < n; i ++) {
				double sum = 0.0, win = 0.0;
				WP_par[i][0] = WP_par[i][1] = 0.0;
				for (int j = 0; j < n; j ++) {
					if (mat[i][j] == '.')
						continue;
					sum += 1.0;
					if (mat[i][j] == '1')
						win += 1.0;
				}
				WP_par[i][0] = win;
				WP_par[i][1] = sum;
				WP[i] = win / sum;
			}
			
			// OWP
			for (int i = 0; i < n; i ++) {
				double sum = 0.0, win = 0.0;
				for (int j = 0; j < n; j ++) {
					if (mat[i][j] == '.')
						continue;
					sum += 1.0;
					if (mat[i][j] == '1')
						win += (WP_par[j][0]) / (WP_par[j][1] - 1.0);
					else
						win += (WP_par[j][0] - 1.0) / (WP_par[j][1] - 1.0);
				}
				OWP[i] = win / sum;
			}
			
			// OOWP
			for (int i = 0; i < n; i ++) {
				double sum = 0.0, win = 0.0;
				for (int j = 0; j < n; j ++) {
					if (mat[i][j] == '.')
						continue;
					sum += 1.0;
					win += OWP[j];
				}
				OOWP[i] = win / sum;
			}
			
			
			// Output
			printf("Case #%d:\n", c);
			for (int i = 0; i < n; i ++) {
				printf("%.12lg\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
			}
		}
	}

}


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	gcj::solve();
	return 0;
}
