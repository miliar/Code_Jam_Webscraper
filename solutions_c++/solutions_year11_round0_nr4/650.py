#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int a[10000], b[10000];

int main() {
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++) {
		scanf("%d", &n);

		for (int i=0;i<n;i++) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(a, a+n);
		int ans = 0;
		for (int i=0;i<n;i++)
			if (b[i] != a[i]) ans ++;
		printf("Case #%d: %d.000000\n", ti, ans);
	}
	return 0;
}
