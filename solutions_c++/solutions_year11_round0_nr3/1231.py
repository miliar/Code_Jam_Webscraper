#include <stdio.h>
#include <string.h>

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		int y=0,s=0,m=1000000000;
		for(int i=0;i<n;++i) {
			int x;
			scanf("%d",&x);
			s+=x;
			y^=x;
			if(m>x) m=x;
		}
		printf("Case #%d: ",test);
		if(y) printf("NO\n");
		else printf("%d\n",s-m);
	}
	return 0;
}
