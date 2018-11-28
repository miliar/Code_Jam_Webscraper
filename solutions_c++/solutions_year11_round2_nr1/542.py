#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int testnum;
	scanf("%d", &testnum);
	char M[101][101];
	bool OO[101][101];
	double OWP[ 101], OOWP[ 101];
	double WP[101][101];
	
	for (int testcase = 1; testcase <= testnum; testcase++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%s", M[i]);
					
		for (int i = 0; i < n; i++) {
			int m = 0, win = 0;
			for (int j = 0; j < n; j++) {
				if (M[i][j] == '1')
					win++;
				if (M[i][j] != '.')
					m++;
			}
			for (int j = 0; j < n; j++) {
				if (M[i][j] != '.') {
					if (M[i][j] == '1')
						WP[i][j] = (win - 1) / (double)(m - 1);
					else
						WP[i][j] = win / (double)(m - 1);
				}
			}
			WP[i][i] = win / (double)m;
		}
		
		for (int i = 0; i < n; i++) {
			int m = 0;
			double sum = 0;
			for (int j = 0; j < n; j++) {
				if (M[i][j] != '.')
					m++, sum += WP[j][i];
			}
			OWP[i] = sum / m;
		}
			
		for (int i = 0; i < n; i++) {
			int m = 0;
			double sum = 0;
			for (int j = 0; j < n; j++) {
				if (M[i][j] != '.')
					m++, sum += OWP[j];
			}
			OOWP[i] = sum / m;
		}		
		
		printf("Case #%d:\n", testcase);
		for (int i = 0; i < n; i++) {
			printf("%.10lf\n", 0.25 * WP[i][i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}
