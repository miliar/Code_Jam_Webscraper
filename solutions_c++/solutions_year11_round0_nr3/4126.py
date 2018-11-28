#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAXN 1100

int val[MAXN];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int caseT = 1; caseT <= cases; ++caseT) {
		int n, t = 0, sum = 0;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			scanf("%d", val + i);
			t ^= val[i];
			sum += val[i];
		}
		sort(val, val + n);
		sum -= val[0];
		printf("Case #%d: ", caseT);
		if(t == 0) printf("%d\n", sum);
		else puts("NO");
	}
	return 0;
}
