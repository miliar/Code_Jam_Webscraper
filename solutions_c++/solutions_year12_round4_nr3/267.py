#include <cstdio>
#include <cstring>
typedef long long ll;
const int c=2048;
int t,ii;
int x[c];
int h[c];
int n;
int main() {
	scanf("%d",&t);
	int i,j,k,p;
	for (ii=1; ii<=t; ++ii) {
		scanf("%d",&n);
		for (i=1; i<n; ++i) scanf("%d",&x[i]);
		memset(h,0,sizeof(int)*(n+1));
		bool q,qq;
		for (p=0; p<10*n; ++p) {
			q=1;
			for (i=1; i<n; ++i) {
				qq=1;
				j=x[i];
				for (k=i+1; k<j; ++k)
					if ((h[j]-h[i])*(k-i)<=(h[k]-h[i])*(j-i)) break;
				if (k<j) qq=0;
				for (k=j+1; k<=n; ++k)
					if ((h[j]-h[i])*(k-i)<(h[k]-h[i])*(j-i)) break;
				if (k<=n) qq=0;
				if (!qq) ++h[j];
				if (!qq) q=0;
			}
			if (q) break;
		}
		printf("Case #%d: ",ii);
		if (q) {
			for (i=1; i<=n; ++i) printf("%d ",h[i]);
		} else printf("Impossible");
		printf("\n");
	}
	return 0;
}
