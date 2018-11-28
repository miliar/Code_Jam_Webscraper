#include <stdio.h>
#include <string.h>
int a[10005];
int main () {
	freopen ("C-small-attempt0.in","r",stdin);
	freopen ("c-small.out","w",stdout);
	int t;
	scanf ("%d",&t);
	for (int ca=1;ca<=t;ca++) {
		int n,l,h;
		scanf ("%d%d%d",&n,&l,&h);
		for (int i=1;i<=n;i++) {
			scanf ("%d",&a[i]);
		}
		
		bool find = 0;
		for (int i=l;i<=h;i++) {
			bool ok =1;
			for (int j=1;j<=n;j++) {
				if (i%a[j]!=0 && a[j]%i!=0) {
					ok = 0;
					break;
				}
			}
			if (ok) {
				find = 1;
				printf ("Case #%d: %d\n",ca,i);
				break;
			}
		}
		if (find == 0) {
			printf ("Case #%d: NO\n",ca);
		}
	}
	return 0;
}
