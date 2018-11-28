#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
int a[1001];

int main() {
	freopen("D-large.in", "r", stdin);
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		int n;
		double res = 0.0;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		for (int i = 1; i <= n; i++) {
			if (a[i] == i)
				continue;
			int s = i;
			int k = 1;
			while (a[s] != i) {
				++k;
				int tmp = s;
				s = a[s];
				a[tmp] = tmp;
			}
			a[s] = s;
			res += k;
		}
		printf("Case #%d: %.6lf\n", k, res);
	}
	return 0;
}
