#include<cstdio>
#include<iostream>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for(int i = 1; i <= tc; i++) {
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		int sp, tot;
		sp = tot = 0;
		while(n--) {
			int num;
			scanf("%d", &num);
			if((num == 3 * p - 4 || num == 3 * p - 3) && (num >= 2)) {
				sp++;
			} else if(num > 3 * p - 3) {
				tot++;
			}
		}
		printf("Case #%d: %d\n", i, tot + min(sp, s));
	}
	return 0;
}
