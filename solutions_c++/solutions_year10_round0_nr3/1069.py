#include <cstdio>
using namespace std;

const int MAXG = 10000005;
int g[MAXG], next[MAXG];
long long v[MAXG];

int main()
{
	freopen("data.in", "r", stdin);
	freopen("result.out", "w", stdout);

	int curt, tn;
	scanf("%d", &tn);
	for(curt = 1; curt <= tn; ++curt) {
		int r, k, n;
		scanf("%d %d %d", &r, &k, &n);
		int i, j;
		for(i = 0; i < n; ++i) scanf("%d", &g[i]);

		long long sum = 0;
		for(i = j = 0; i < n; ++i) {
			int j0 = j;
			while(sum + g[j] <= k) {
				sum += g[j];
				j = (j+1) == n ? 0 : j+1;
				if(j == j0) break;
			}
			next[i] = j;
			v[i] = sum;
			sum -= g[i];
		}


		int curp = 0;
		long long ans = 0;
		for(i = 0; i < r; ++i) {
			ans += v[curp];
			curp = next[curp];
		}

		printf("Case #%d: %lld\n", curt, ans);
	}
	return 0;
}