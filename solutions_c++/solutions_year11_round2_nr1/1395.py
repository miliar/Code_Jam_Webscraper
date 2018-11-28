#include <stdio.h>
#include <stdlib.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		int n;
		scanf("%d ",&n);
		char f[n+2][n+2];
		for (int i=0; i<n; ++i)
			scanf("%s ",f[i]);
		double wp[n], owp[n], oowp[n];
		int nop[n], wins[n];
		for (int i=0; i<n; ++i) {
			wins[i] = 0;
			nop[i] = 0;
			for (int j=0; j<n; ++j) {
				wins[i] += f[i][j] == '1';
				nop[i] += f[i][j] != '.';
			}
			wp[i] = (double) wins[i];
		}
		for (int i=0; i<n; ++i) {
			double s = 0.;
			for (int j=0; j<n; ++j)
				if (f[i][j] != '.')
					s += (double) (wins[j] - (f[i][j] == '0')) / (nop[j] - 1);
			owp[i] = s;
		}
		for (int i=0; i<n; ++i) {
			double s = 0.;
			for (int j=0; j<n; ++j)
				if (f[i][j] != '.')
					s += owp[j] / nop[j];
			oowp[i] = s;
		}

		printf("Case #%d:\n",c);
		for (int i=0; i<n; ++i)
			printf("%.12lf\n", (wp[i] + 2 * owp[i] + oowp[i]) / (4. * nop[i])); 

	}
	return 0;
}
