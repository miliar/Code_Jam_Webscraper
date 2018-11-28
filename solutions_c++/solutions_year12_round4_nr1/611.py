#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int c=10010;
int t,ii;
int n;
int d;
int a[c],l[c];
int r[c];
int main() {
	scanf("%d",&t);
	int i,j,k;
	bool q;
	for (ii=1; ii<=t; ++ii) {
		scanf("%d",&n);
		for (i=1; i<=n; ++i) scanf("%d%d",&a[i],&l[i]);
		scanf("%d",&d);
		memset(r,0,sizeof(int)*(n+1));
		r[1]=a[1];
		i=1;
		q=0;
		for (i=1; i<=n; ++i) {
			if (r[i]==0) continue;
			if (r[i]>=d-a[i]) {
				q=1;
				break;
			}
			for (j=i+1; j<=n && a[j]-a[i]<=r[i]; ++j) {
				k=min(l[j],a[j]-a[i]);
				if (r[j]<k) r[j]=k;
			}
		}
		printf("Case #%d: ",ii);
		if (q) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}
