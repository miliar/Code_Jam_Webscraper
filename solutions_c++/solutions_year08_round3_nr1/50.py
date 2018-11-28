#include <stdio.h>
#include <functional>
#include <algorithm>
using namespace std;

const int N = 1010;

int f[N];

typedef long long LL;

int main()
{
	 freopen("A-large.in", "r", stdin);
	 freopen("A-large.txt", "w", stdout);

	int ntc, i, j, x, m, n, L, tc = 0, k;
	scanf("%d", &ntc);
	while(ntc--) {
		printf("Case #%d: ", ++tc);
		scanf("%d%d%d", &m, &n, &L);
		for(i = 0; i < L; ++i) {
			scanf("%d", f+i);
		}
		if(L > m * n) {
			printf("Impossible\n");
			continue;
		}
		sort(f, f+L, greater<int>());
		j = 0, k = 1;
		LL ans = 0;
		for(i = 0; i < L; ++i) {
			if(j == n) {
				j = 0;
				k++;
			}
			ans += f[i] * k;
			j++;
		}
		printf("%I64d\n", ans);
	}
	return 0;
}
