#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

const int N_SIZE = 14;
const int M_SIZE = 1003;

double f[N_SIZE];
double d[N_SIZE];
double p[N_SIZE][N_SIZE];
double a[N_SIZE];

int perm[M_SIZE];
bool marked[M_SIZE];

int main()
{
	f[0] = 1;
	d[0] = 1;
	for (int i = 1; i != N_SIZE; i++) {
		f[i] = f[i - 1] * i;
		d[i] = floor(f[i] / M_E + 0.5);
	}
	for (int n = 0; n != N_SIZE; n++)
		for (int k = 0; k <= n; k++)
			p[n][k] = d[k] / (f[n - k] * f[k]);
	memset(a, 0, sizeof(a));
	for (int n = 2; n != N_SIZE; n++) {
		for (int k = 0; k <= n - 1; k++)
			a[n] += a[k] * p[n][k];
		a[n] = (1 + a[n]) / (1 - p[n][n]);
	}
	
	freopen("d1.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int testCount, nCount;	
	double ans;
	scanf("%d", &testCount);
	for (int tc = 1; tc <= testCount; tc++) {
		scanf("%d", &nCount);
		for (int i = 1; i <= nCount; i++)
			scanf("%d", &perm[i]);
		memset(marked, false, sizeof(marked));
		ans = 0;
		for (int i = 1; i <= nCount; i++) {
			if (marked[i])
				continue;
			int len = 0;
			for (int j = i; !marked[j]; j = perm[j]) {
				marked[j] = true;
				len++;
			}
			if (len > 1)
				ans += len;
		}
		printf("Case #%d: %.6lf\n", tc, ans);
	}
	return 0;
}
