#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	int z, n;
	scanf("%d",&z);
	int g = 1;
	while (z--) {
		scanf("%d",&n);
		char s[n][n+1];
		for (int i=0; i<n; i++)
			scanf("%s", s[i]);
		int a[n];
		for (int i=0; i<n; i++)	a[i] = i;
		int ans = 1<<28;
		do {
			int b[n];
			bool ok = 1;
			for (int i=0; ok&&i<n; i++) {
				int u = a[i];
				for (int j=i+1;j<n;j++)
					ok &= s[u][j]!='1';
			}
			if (!ok)	continue;
			memcpy(b,a,sizeof(a));
			int tot=0;
			for (int i=n-1;i>=0;i--) {
				int u = 0;
				while (b[u]!=i) ++u;
				for (int j=u;j<i;j++)
					swap(b[j],b[j+1]), ++tot;
			}
			ans = min(ans,tot);
		} while (next_permutation(a,a+n));
		printf("Case #%d: %d\n", g++,ans);
	}
}
