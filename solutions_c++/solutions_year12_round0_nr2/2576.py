#include <iostream>
#include <cstdio>

using namespace std;


int main() {
	
	
	int t;
	scanf("%d",&t);
	
	for (int i=1; i<=t; ++i) {
		int n,s,p;
		scanf("%d %d %d",&n,&s,&p);
		
		int sol = 0;
		
		for (int j=0; j<n; ++j) {
			int total;
			scanf("%d",&total);
			
			switch(total) {
				case 0:
					if ( p <= 0 ) sol++;
					break;
				case 1:
					if ( p <= 1 ) sol++;
					break;
				case 29:
				case 30:
					if ( p <= 10 ) sol++;
					break;
				default:
					if ( 3*p-2 <= total ) sol++;
					else {
						if ( 3*p-4 <= total && s >= 1 ) {
							sol++;
							--s;
						}
					}
					break;
			}
		}
		
		printf("Case #%d: %d\n",i,sol);
	}
	
	return 0;
}
