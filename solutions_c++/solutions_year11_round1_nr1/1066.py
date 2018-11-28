#include <stdio.h>
#include <string.h>

#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b) {
	int t;
	while (b!=0) {
		t=b;
		b=a%b;
		a=t;
	}
//	printf("gcd=%d\n", a);
	return a;
}


int main() {

	int tt;
	long long N;
	int Pd, Pg;
	int D, G;
	int Wd, Wg;
	cin>>tt;
	
	for (int casen=1;casen<=tt;++casen) {
		printf("Case #%d: ", casen);
		cin >>N>>Pd>>Pg;
		
		if (Pg==0) {
			printf((Pd==0)?"Possible\n":"Broken\n");
			continue;
		}
		
		if (Pg==100) {
			printf((Pd==100)?"Possible\n":"Broken\n");
			continue;
		}
		
		if (Pd==0) {
			printf("Possible\n");
			continue;
		}
		
		int g=gcd(Pd, 100);
		Wd=Pd/g;
		D=100/g;
		
		if (D>N) {
			printf("Broken\n");
//		printf("D=%d Wd=%d G=%d Wg=%d N=%d\n", D, Wd, G, Wg, N);
			continue;
		}
		
		printf("Possible\n");
	}
}
