
#include <cstdio>
#include <cstdlib>
#include "mymacros.h"

int n,pg,pd;

bool possible() {
	if (pg==100 && pd<100) return false;
	if (pg==0 && pd!=0) return false;
	if (n>100) return true;
	rep2(j,1,n) {
		rep(k,j+1) {
			if ( ((k*100)%j)==0 && ((k*100)/j)==pd )
				return true;
		}
	}
	return false;
}

int main(int argc, char **argv) {
	int t;
	scanf("%i",&t);
	rep(i,t) {
		printf("Case #%i: ",i+1);
		scanf("%i %i %i", &n, &pd, &pg);
		if (possible())
			printf("Possible\n");
		else
			printf("Broken\n");
	}
}
