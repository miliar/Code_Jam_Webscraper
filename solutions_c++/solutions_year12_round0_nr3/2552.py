#include <cstdio>

using namespace std;

int ceil(int x) {
	int r = 1;
	while(r < x) r *= 10;
	return r;
}

int g[9];
int gs;

int main() {
	int t;
	scanf("%i", &t);
	for(int i = 0; i < t; i++) {
		printf("Case #%i: ", i + 1);
		int a, b;
		scanf("%i%i", &a, &b);
		long long cnt = 0;
		for(int x = a; x <= b; x++) {
			gs = 0;
			for(int m = ceil(x), j = 10; j < m; j *= 10) {
				int high = x / j, low = x % j;
				int y = low * (m / j) + high;
				//printf("\n%i:%i=%i ", high, low, y);
				if(low * 10 >= j && x < y && y <= b) {
					int k;
					for(k = 0; k < gs; k++) if(g[k] == y) break;
					if(k == gs) {
						g[gs++] = y;
						cnt++;
					}
				}
			}
		}
		printf("%lli\n", cnt);
	}
}

