#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<set>
#include<cmath>
using namespace std;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T, d[1010], n;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d", &n);
		int i;
		for (i = 1; i <= n; i++)
			scanf("%d", &d[i]);
		int total = 0;
		double ans = 0;
		for (i = 1; i <= n; i++) {
			if (d[i] != i) {
				if (d[d[i]] == i) {
					ans += 2.0;
				}
				else total ++;
			}
		}
		ans /= 2.0;
		ans += total;
		printf("Case #%d: %lf\n", t, ans);
	}
	return 0;
}
