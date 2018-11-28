#include<stdio.h>
#include<algorithm>
using namespace std;

int main() {
	int a[1024],b[1024];
	int N,n,cs=0,i,r;
	for(scanf("%d",&N);N--;) {
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%d",&a[i]),b[i]=a[i];
		sort(b,b+n);
		for(r=i=0;i<n;i++) if (a[i]!=b[i]) r++;
		printf("Case #%d: %d.000000\n",++cs,r);
	}
	return 0;
}
