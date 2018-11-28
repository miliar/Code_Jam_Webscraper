// thiago kronig <thiagokronig@gmail.com>

#include <cstdio>

using namespace std;

int main() {
	
	int t,tt;
	
	scanf("%d",&t);
	for (int tt=1; tt<=t; tt++) {
		int n,x,min,xum;
		long long sum = 0;
		
		scanf("%d", &n);
		for (int i=0; i<n; i++) {
			scanf("%d",&x);
			if (i == 0) {
				xum = x;
				min = x;
			}
			else {
				xum ^= x;
				min = x < min ? x : min;
			}
			sum += x;
		}
		
		if (xum != 0)
			printf("Case #%d: NO\n", tt);
		else
			printf("Case #%d: %lld\n", tt, sum - (long long)min);
	}
	
	return 0;
}