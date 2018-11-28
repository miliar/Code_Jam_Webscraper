#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
int gcd(int a,int b) {
	while(b) {
		int t = b;
		b = a%b;
		a = t;
	}
	return a;
}
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		long long N;
		int pd, pg;
		scanf("%lld%d%d",&N,&pd,&pg);
		printf("Case #%d: ",cn);
		if(!pg && pd) printf("Broken\n");
		else if(pd < 100 && pg == 100) printf("Broken\n");
		else if(!pd) printf("Possible\n");
		else {
			int g = 100/gcd(pd,100);
			if(g <= N) printf("Possible\n");
			else printf("Broken\n");
		}
	}
}
