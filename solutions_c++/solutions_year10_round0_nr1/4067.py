// CodeJam2010Round1.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include "math.h"


int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("input.in", "r", stdin);
	freopen("outLarge.in", "w", stdout);
	int numCases;
	scanf("%d", &numCases);
	for(int i=0; i<numCases; ++i) {
		int n, k;
		scanf("%d %d", &n, &k);
		if((k | ((1<<n) - 1)) == k) printf("Case #%d: ON\n", i+1);
		else printf("Case #%d: OFF\n", i+1);
	}
	return 0;
}

