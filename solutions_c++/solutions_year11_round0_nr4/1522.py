#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAXN 1001
int main() {
	int cas;
	scanf("%d", &cas);
	for (int id = 1; id <= cas; ++id) {
		int n;
		scanf("%d", &n);
		int a[MAXN], b[MAXN];
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b, b + n);
		int res = 0;
		for (int i = 0; i < n; ++i) {
			if (a[i] != b[i]) {
				res++;
			}
		}
		printf("Case #%d: %lf\n", id, res * 1.0);
	}
	return 0;
}