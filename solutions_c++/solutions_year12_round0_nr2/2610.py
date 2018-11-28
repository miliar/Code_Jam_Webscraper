#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for(int z=1; z<=t; z++) {
		int n, sup, p, out = 0;
		scanf("%d %d %d", &n, &sup, &p);
		int tab[n];
		for(int i=0; i<n; i++)
			scanf("%d", &tab[i]);
		sort(tab, tab+n);
		
		--n;
		while(n>=0) {
			int pkt = tab[n];
			--n;
			// najlepszy wynik 'na sucho'
			int best = pkt/3;
			if(pkt%3) ++best;
			// printf("best: %d\n", best);
			if(best >= p)	// starczy?
				++out;
			else if(pkt>1 && sup>0) {
				++best;
				--sup;
					if(best >= p)	// starczy?
					++out;
			}
		}
		
		printf("Case #%d: %d\n", z, out);
	
	}
	return 0;
}
