#include <cstdio>

using namespace std;

int main() {
	int t, n;
	long k, m;
	
	scanf("%d", &t);
	
	for( int i = 1; i <= t; ++i) {
		
		scanf("%d%ld", &n, &k);
		m = 1;
		
		for(int j = 0; j < n; ++j) {
				m = m * 2;
		}
		
		if( k >= m - 1 && (k - m + 1) % (m) == 0) {
			printf("Case #%d: ON\n", i);
		} else {
			printf("Case #%d: OFF\n", i);
		}
		
	}
	
	return 0;
	
}


