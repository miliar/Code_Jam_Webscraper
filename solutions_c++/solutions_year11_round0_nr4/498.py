#include <cstdio>
#include <algorithm>
#include <cstring>
#define MAXN 1001
using namespace std;
int main() {
	int cas, cs = 1;
	scanf("%d", &cas);
	while(cas--) {
		int n, a[MAXN], vis[MAXN];
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			--a[i];
		}
		int ans = 0;
		memset(vis, 0, sizeof(vis));
		for(int i = 0; i < n; ++i) {
			if(a[i] == i || vis[i])
				continue;
			++ans;
			vis[i] = 1;
			for(int j = a[i]; j != i; j = a[j]) {
				++ans;
				vis[j] = 1;
			}
		}
		printf("Case #%d: %.6lf\n", cs, (double)ans);
		++cs;
	}
	return 0;
}
