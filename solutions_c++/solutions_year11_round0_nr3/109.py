#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<set>
#include<cmath>
using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		int n, min = 1000000000, total = 0, totalV = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			int d;
			scanf("%d", &d);
			totalV += d;
			if (d < min) {
				min = d;
			}
			total ^= d;
		}
		if (total == 0) {
			printf("Case #%d: %d\n", t, totalV - min);
		} else {
			printf("Case #%d: NO\n", t);
		}
	}
	return 0;
}
