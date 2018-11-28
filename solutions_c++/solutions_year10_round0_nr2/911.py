#include <cstdio>

using namespace std;

int main() {
	int c, n;
	long t[1010], d[1010];
	
	scanf("%d", &c);
	
	for( int i = 1; i <= c; ++i) {
		scanf("%d", &n);
		scanf("%ld", &t[0]);
		
		//1隣りとの差を出す
		for( int j = 1; j <= n - 1; ++j) {
			scanf("%ld", &t[j]);
			
			if( t[j] > t[j - 1]) {
				d[j - 1] = t[j] - t[j - 1];
			} else {
				d[j - 1] = t[j - 1] - t[j];
			}
		}
		//1end
		
		//2漸化的にgcdを出したい
		for( int k = 0; k < n - 2; ++k) {
			
			if( d[k + 1] == 0) {
				d[k + 1] = d[k];
				
			//2'互除法
			} else if( d[k] != 0) {
				
				for( ; d[k] % d[k + 1] != 0 && d[k + 1] % d[k] != 0; ) {
					if( d[k] < d[k + 1]) {
						d[k + 1] = d[k + 1] % d[k];
					} else {
						d[k] = d[k] % d[k + 1];
					}
				}
				
				if( d[k + 1] > d[k]) {
					d[k + 1] = d[k];
				}
			}
			//2'end
		}
		//2end
		
		//3いつ？
		if( t[0] % d[n - 2] == 0) {
			printf("Case #%d: 0\n", i);
		} else {
			printf("Case #%d: %ld\n", i, d[n - 2] - t[0] % d[n - 2]);
		}
		//3end	
		
	}
}


