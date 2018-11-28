#include <cstdio>
using namespace std;

int t, n, s, p, x, x3, r;

int main(void) {
	scanf("%d", &t);
	for(int ti = 1; ti <= t; ti++) {
		scanf("%d %d %d", &n, &s, &p);
		r = 0;
		for(int i = 0; i < n; i++) {
			scanf("%d", &x);
			x3 = x / 3;
			switch(x%3) {
			case 0:
				if(x3 >= p) {
					r++;
				} else if(x > 0 && x < 30 && x3+1 >= p && s > 0) {
					s--;
					r++;
				}
				break;
			case 1:
				if(x3+1 >= p) {
					r++;
				}
				break;
			case 2:
				if(x3+1 >= p) {
					r++;
				} else if(x < 29 && x3+2 >= p && s > 0) {
					s--;
					r++;
				}
				break;
			}
		}
		printf("Case #%d: %d\n", ti, r);
	}
	return 48-48;
}
