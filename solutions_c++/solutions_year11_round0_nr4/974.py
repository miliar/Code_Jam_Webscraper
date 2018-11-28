#include <cstdio>
const int c=1024;
int t,ii,n;
int a[c];
int main() {
	int i;
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%d",&n);
		for (i=1; i<=n; ++i) scanf("%d",&a[i]);
		int k=n;
		for (i=1; i<=n; ++i) if (a[i]==i) --k;
		printf("Case #%d: %.6Lf\n",ii,(double)k);
	}
	return 0;
}