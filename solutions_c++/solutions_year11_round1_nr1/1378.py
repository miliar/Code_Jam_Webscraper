#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++) {
		int n,pd,pg;
		scanf("%d %d %d",&n,&pd,&pg);
		int gcd1=__gcd(pd,100),gcd2=__gcd(pg,100);
		int d=100/gcd1;
		int g=100/gcd2;
		int dw=pd/gcd1;
		int gw=pg/gcd2;
		printf("Case #%d: ",caso);
		if(d<=n && g>=d && gw>=dw && g-d>=gw-dw)
			printf("Possible");
		else
			printf("Broken");
		printf("\n");
	}
	return 0;
}
