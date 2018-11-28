#include <cstdio>

long long gcd(long long a, long long b) {
	while(b) {
		long long temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}

int main() {
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++) {
		long long n;
		int ptoday;
		int pever;
		scanf("%lld %d %d",&n,&ptoday,&pever);
		bool possible=false;
		if(pever==0 || pever == 100) {
			if(ptoday==pever) {
				possible = true;
			} else {
				possible = false;
			}
		} else {
			if (ptoday==0) {
				possible = true;
			} else {
				long long num = ptoday;
				long long den = 100;
				long long gd = gcd(num,den);
				num/=gd;
				den/=gd;
				if(den<=n) {
					possible = true;
				} else {
					possible = false;
				}
			}
		}
		printf("Case #%d: %s\n",i+1,possible?"Possible":"Broken");
	}
	return 0;
}
