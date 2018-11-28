
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

#define NN 110
char m[NN][NN];
int wc[NN], t[NN];
double owp[NN], oowp[NN];

int main() {
	int T;
	scanf("%d ", &T);
	for (int ct = 1; ct <= T; ct++) {
		int n; scanf("%d ", &n);
		for (int i = 0; i < n; i++) gets(m[i]);

		for (int i = 0; i < n; i++) {
			t[i] = wc[i] = 0;
			for (int j = 0; j < n; j++) {
				wc[i] += m[i][j] == '1';
				t[i] += m[i][j] != '.';
			}
		}

		for (int i = 0; i < n; i++) {
			owp[i] = 0;
			for (int j = 0; j < n; j++) {
				if (m[i][j] == '0')
					owp[i] += double(wc[j]-1)/(t[j]-1);
				else if (m[i][j] == '1')
					owp[i] += wc[j]/double(t[j]-1);
			}
			owp[i] /= t[i];
		}

		for (int i = 0; i < n; i++) {
			oowp[i] = 0;
			for (int j = 0; j < n; j++) {
				if (m[i][j] != '.')
					oowp[i] += owp[j];
			}
			oowp[i] /= t[i];
		}

		printf("Case #%d:\n", ct);
		for (int i = 0; i < n; i++)
			printf("%.12lf\n", (0.25*wc[i])/t[i] + 0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}
