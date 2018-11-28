#include <cstdio>
#include <algorithm>
#include <numeric>
#define MAXN 1024
using namespace std;
int main() {
	int cas, cs = 1;
	scanf("%d", &cas);
	while(cas--) {
		int n, a[MAXN], tmp = 0;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			tmp ^= a[i];
		}
		if(tmp != 0) {
			printf("Case #%d: NO\n", cs);
		}
		else {
			int ans = accumulate(a, a + n, 0) - *min_element(a, a + n);
			printf("Case #%d: %d\n", cs, ans);
		}
		++cs;
	}
	return 0;
}
