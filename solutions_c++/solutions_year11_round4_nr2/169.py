#include <cstdio>
#include <cmath>

double sumx[600][600], sumy[600][600], tsum[600][600];
int v[600][600];


double hvx(int i, int j, int k) {
   return 	((v[i][j] + v[i + k][j]) * (j + 1) + (v[i][j + k] + v[i + k][j + k]) * (j + k + 1));
}
double hvy(int i, int j, int k) {
   return	((v[i][j] + v[i][j + k]) * (i + 1) + (v[i + k][j] + v[i + k][j + k]) * (i + k + 1));
}
double hvt(int i, int j, int k) {
   return ((v[i][j] + v[i][j + k])+ (v[i + k][j] + v[i + k][j + k]));
}

bool zero(double x, double y) {
	return fabs(x - y) < 1e-5;
}

int work() {
	int r, c, d;
	scanf("%d%d%d", &r, &c, &d);
	for (int i = 0; i < r; ++i) {
		char s[800];
		scanf("%s", s);
		for (int j = 0; j < c; ++j) {
			v[i][j] = s[j] - '0' + d;
			sumx[i + 1][j + 1] = sumx[i][j + 1] + 
				sumx[i + 1][j] - sumx[i][j] + v[i][j] * (j + 1);
			sumy[i + 1][j + 1] = sumy[i][j + 1] + 
				sumy[i + 1][j] - sumy[i][j] + v[i][j] * (i + 1);
			tsum[i + 1][j + 1] = 
				tsum[i + 1][j] + tsum[i][j + 1] - tsum[i][j] + v[i][j];
		}
	}
	int ans = -1;
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			for (int k = 3; i + k <= r && j + k <= c; ++k) {
				int i1 = i + k, j1 = j + k;
				double s1 = sumx[i1][j1] - sumx[i][j1] - sumx[i1][j]
					+ sumx[i][j] - hvx(i, j, k - 1);
				double s2 = sumy[i1][j1] - sumy[i][j1] - sumy[i1][j]
				   	+ sumy[i][j] - hvy(i, j, k - 1);
				double s3 = tsum[i1][j1] - tsum[i][j1] - tsum[i1][j]
					+ tsum[i][j] - hvt(i, j, k - 1);
				//fprintf(stderr, "%d %d %d %lf %lf %lf\n", i, j, k, s1, s2, s3);
				if (zero(s2 * 2, s3 * (i + i1 + 1)) && 
						zero(s1 * 2, s3 * (1 + j + j1)))
					//fprintf(stderr, "%d %d %d", i, j, k);
					if (ans < k)
						ans = k;
			}
		}
	}
	return ans;
}
int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		int t = work();
		printf("Case #%d: ", Ti);
		if (t >= 0)
			printf("%d\n", t);
		else
			printf("IMPOSSIBLE\n");
	}
}
