#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

int potenza(int exp) {
	if ( exp == 0 ) return 1;
	else return 10*potenza(exp-1);
}

set<int> numeri;

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=1; i<=t; ++i) {
		int a,b;
		scanf("%d %d",&a,&b);
		
		int sol = 0;
		
		int l = 0;
		int pow = 1;
		while ( pow <= a ) {
			l++;
			pow *= 10;
		}
		
		
		for (int n=a; n<b; ++n) {
			numeri.clear();
			
			for (int k=1; k<l; ++k) {
				int m = (n/(potenza(k))) + potenza(l-k)*(n%potenza(k));
				if ( n < m && m <= b ) {
					numeri.insert(m);
					//printf("%d %d\n",n,m);
				}
			}
			
			sol += numeri.size();
		}
		
		printf("Case #%d: %d\n",i,sol);
	}
	
	return 0;
}
