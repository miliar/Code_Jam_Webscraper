#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

const int h = 111;

int T, n;
char s[h];
int a[h][h];
double wp[h], wpo[h], wpoo[h];
pii w[h];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d%*c", &n);
		for (int i = 0; i < n; i++) {
			gets(s);
			for (int j = 0; j < n; j++)
				if (s[j] == '.')
					a[i][j] = -1;
				else
					a[i][j] = s[j] - '0';
		}
		for (int i = 0; i < n; i++) {
			int e = 0, r = 0;
			for (int j = 0; j < n; j++) {
				if (a[i][j] > -1) {
					r ++;
					if (a[i][j])
						e ++;
				}
			}
			wp[i] = e / (double) r;
			w[i] = make_pair(e, r);
		}
		for (int i = 0; i < n; i++) {
			double e = 0.;
			int r = 0;
			for (int j = 0; j < n; j++) {
				if (a[i][j] > -1) {
					r ++;
					if (a[i][j])
						e += w[j].first / (double) (w[j].second - 1);
					else
						e += (w[j].first - 1) / (double) (w[j].second - 1);
				}
			}
			wpo[i] = e / (double) r;
		}
		for (int i = 0; i < n; i++) {
			double e = 0.;
			int r = 0;
			for (int j = 0; j < n; j++) {
				if (a[i][j] > -1) {
					r ++;
					e += wpo[j];
				}
			}
			wpoo[i] = e / (double) r;
		}
		printf("Case #%d:\n", t+1);
		for (int i = 0; i < n; i++)
			printf("%.8lf\n", 0.25 * wp[i] + 0.5 * wpo[i] + 0.25 * wpoo[i]);
	}
	return 0;
}