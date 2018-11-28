#include <stdio.h>

int main() {
	int t,c;
	scanf("%d",&t);
	for (c=1;c<=t;++c) {
		int n,k,x=0,s=0,m=0x7fffffff;
		scanf("%d",&n);
		while (n--) {
			scanf("%d",&k);
			x^=k;
			s+=k;
			if (k<m)
				m=k;
		}
		if (x)
			printf("Case #%d: NO\n", c);
		else
			printf("Case #%d: %d\n", c, s - m);
	}
	return 0;
}
