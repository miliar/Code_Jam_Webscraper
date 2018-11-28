#include <iostream>
using namespace std;

const int maxn = 110;
int n;
char a[maxn][maxn];

double wp[maxn], owp[maxn], oowp[maxn];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		cin >> n;
		for (int i = 0; i < n; i++)
			scanf("%s", a[i]);
		
		memset(oowp, 0, sizeof(oowp));
		memset(owp, 0, sizeof(owp));

		// wp
		for (int i = 0; i < n; i++) {
			int tot = 0, w = 0;
			for (int j = 0; j < n; j++)
				if (a[i][j] == '0' || a[i][j] == '1') {
					tot++;
					if (a[i][j] == '1')
						w++;
				}
			wp[i] = (double)w / (double)tot;
		}

		// owp
		for (int i = 0; i < n; i++) {
			double res = 0;
			int tt = 0;
			for (int j = 0; j < n; j++)
				if (a[i][j] != '.') {
					tt++;
					int tot = 0, w = 0;
					for (int k = 0; k < n; k++)
						if (k != i && a[j][k] != '.') {
							tot++;
							if (a[j][k] == '1')
								w++;
						}
					res += (double) w / (double) tot;
				}
			owp[i] = res / (double)tt;
		}


		// oowp
		for (int i = 0; i < n; i++) {
			int tot = 0;
			for (int j = 0; j < n; j++)
				if (a[i][j] == '0' || a[i][j] == '1') {
					oowp[i] += owp[j];
					tot++;
				}
			oowp[i] /= tot;
		}
		
		printf("Case #%d:\n", tt);
		for (int i = 0; i < n; i++)
			printf("%.7lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
	}
}