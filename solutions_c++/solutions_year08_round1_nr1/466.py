#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>
#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))

using namespace std;

int v[900], w[900];

int main() {
	int T, n, i, ans, test=1;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		for (i=0;i<n;i++) {
			scanf("%d", &v[i]);
		}
		for (i=0;i<n;i++) {
			scanf("%d", &w[i]);
		}
		sort(v, v+n, greater<int>() );
		TRACE(
		for(i=0;i<n;i++) PRINT("%d ", v[i]);
		PRINT("\n");
		);
		sort(w, w+n, less<int>() );
		TRACE(
		for(i=0;i<n;i++) PRINT("%d ", w[i]);
		PRINT("\n");
		);
		ans = 0;
		for (i=0;i<n;i++) {
			ans += v[i]*w[i];
		}
		printf("Case #%d: %d\n", test++, ans);
	}
	return 0;
}
