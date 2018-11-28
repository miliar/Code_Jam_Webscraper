#include <cstdio>
//#include <iostream>
using namespace std;
typedef long long ll;
int t,ii;
ll n;
int pd,pg;
int gcd(int a, int b) {
	if (b==0) return a; else return gcd(b,a%b);
}
int main() {
	scanf("%d",&t);
	int d,g;
	for (ii=1; ii<=t; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%I64Ld%d%d",&n,&pd,&pg);
//		n=1000000000000000LL;
//		cerr << ii << '\n';
		for (d=1; d<=n && d<=10000; ++d) {
			for (g=d; g<=10000; ++g) {
				if (d%(100/gcd(100,pd))==0 && g%(100/gcd(100,pg))==0 && d*pd<=g*pg && d*(100-pd)<=g*(100-pg)) {
//					cerr << d << ' ' << g << '\n';
					printf("Possible\n");
					break;
				}
			}
			if (g<=10000) break;
		}
		if (d<=n && d<=10000) continue;
		printf("Broken\n");
	}
	return 0;
}