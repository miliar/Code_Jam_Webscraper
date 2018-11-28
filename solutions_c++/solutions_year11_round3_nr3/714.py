#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long int LL;

LL note[10009];

int main() {
	
	int t, n;
	LL h, l;
	
	scanf("%d", &t);
	
	for (int k = 1; k <= t; k++) {
		
		scanf("%d %lld %lld", &n, &l, &h);
		
		for (int i = 0; i < n; i++)
			scanf("%lld", &note[i]);
		
		
		bool dasie;
		
		for (int i = l; i <= h; i++) {
			
			dasie = true;
			
			for (int j = 0; j < n; j++) {
				if ((i < note[j] ? note[j] % i : i % note[j])) {
					dasie = false;
					break;
				}
			}
			
			if (dasie) {
				printf("Case #%d: %d\n", k, i);
				break;
			}
		}
		
		if (!dasie)
			printf("Case #%d: NO\n", k);
	}
	
	return 0;
	
}

		
		