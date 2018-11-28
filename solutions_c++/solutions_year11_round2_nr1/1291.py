#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
#define pb push_back

vector<string> b;
double wp[105], wpall[105], owp[105], oowp[105];

int main() {
	int T;
	freopen("c:\\A-large (1).in", "r", stdin);
	//freopen("c:\\A-large (1).out", "w", stdout);

	scanf("%d", &T);


	for (int testCase = 1; testCase <= T; ++testCase) {
		int n;
		scanf("%d", &n);
		memset (wp, 0, sizeof(wp));
		memset (owp, 0, sizeof(owp));
		memset (oowp, 0, sizeof(oowp));


		b = vector<string>(n);
		for (int i = 0; i < n; ++i) {
			char s[105];
			scanf("%s", s);
			b[i] = s;
		}


		printf("Case #%d:\n", testCase);

		double d = 0, all = 0;
		for (int k = 0; k < n; ++k) {
			//printf ("wp[%d]=%lf\n", k, wp[k]);
			d = 0, all = 0;
			for (int i = 0; i < n; ++i) {
				if (b[k][i] == '1') {
					++d;
				}
				if (b[k][i] != '.') {
					++all;
				}
			}
			wp[k] = d / all;
			//printf ("wp[%d]=%lf\n", k, wp[k]);
		}

		for (int k = 0; k < n; ++k) {
			double res = 0, dd = 0;
			for (int i = 0; i < n; ++i) {
				d = 0, all = 0;
				if (b[i][k] == '.') continue;
				for (int j = 0; j < n; ++j) {
					if (j != k) {
						if (b[i][j] == '1') {
							++d;
						}
						if (b[i][j] != '.') {
							++all;
						}
					
					}
				}
				if (i != k) {
					res += d / all;
					++dd;
				}
			}
			owp[k] = res / dd;
			//printf ("owp[%d]=%lf\n", k, owp[k]);
		}

		for (int k = 0; k < b.size(); ++k) {
			d = 0, all = 0;
			for (int i = 0; i < b[k].size(); ++i) {
				if (b[k][i] != '.') {
					d += owp[i];
					++all;
				}
			}
			oowp[k] = d / all;
			//printf ("oowp[%d]=%lf\n", k, oowp[k]);
		}


		for (int i = 0; i < n; ++i) {
			double r = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf ("%.10lf\n", r);
		}
	}

	return 0;
}