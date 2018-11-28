#include <cstdio>
int main() {
	int t,i,n,a,x,s,min;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d", &n);
		s = 0;
		x = 0;
		min = 1000001;
		while(n--) {
				scanf("%d", &a);
				x ^= a;
				s += a;
				if(min > a) 
					min = a;
		}
		if(x == 0)
			printf("Case #%d: %d\n", i, s-min);
		else
			printf("Case #%d: NO\n", i);
	}
}
