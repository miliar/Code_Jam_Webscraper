#include <iostream>
#include <cstdio>
#include <cstdlib>
#define LL long long

using namespace std;

int gcd(int a,int b) {
	while (b!=0) {
		int c=a % b;
		a=b; b=c;
	}
	return a;
}

int tt;

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		LL n;
		int p1,p2;
		cin >> n >> p1 >> p2;
		int d=100/gcd(100,p1);
		if ((p2==100 && p1<100) || (p2==0 && p1>0)) {
			printf("Case #%d: Broken\n",ii);
			continue;
		}
		if ((LL)d>n) printf("Case #%d: Broken\n",ii);
		else printf("Case #%d: Possible\n",ii);
	}
}
