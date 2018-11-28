#include <cstdio>
const int c=1024;
int t,ii;
int n;
int a[c];
int main() {
	scanf("%d",&t);
	int i,k;
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%d",&n);
		for (i=1; i<=n; ++i) scanf("%d",&a[i]);
		k=0;
		for (i=1; i<=n; ++i) k^=a[i];
		int j;
		if (k!=0) printf("NO\n"); else {
			j=1;
			for (i=1; i<=n; ++i) if (a[i]<a[j]) j=i;
			k=0;
			for (i=1; i<=n; ++i) if (i!=j) k+=a[i];
			printf("%d\n",k);			
		}
	}
	return 0;
}