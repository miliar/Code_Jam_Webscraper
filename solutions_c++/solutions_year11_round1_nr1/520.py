#include<stdio.h>

int nCase;

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		long long N;
		int pd, pg;
		scanf("%lld %d %d", &N, &pd, &pg);
		printf("Case #%d: ", cs);
		if(pg == 0 || pg == 100) puts(pd==pg?"Possible":"Broken");
		else {
			int t = 100;
			if(pd%4 == 0) t /= 4;
			else if(pd%2 == 0) t /= 2;
			if(pd%25 == 0) t /= 25;
			else if(pd%5 == 0) t /= 5;
			puts(t<=N?"Possible":"Broken");
		}
	}
}
