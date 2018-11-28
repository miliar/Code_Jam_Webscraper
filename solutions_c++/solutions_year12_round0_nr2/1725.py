#include <stdio.h>
#include <algorithm>
using namespace std;

int x[1000];
int main() {
	int t, ca= 0, i, j, num, n, s, p;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d%d", &n, &s, &p);
		num = 0;
		for (i=0;i<n;++i) {
			scanf("%d", &x[i]);
			if (x[i] >= 3 * p - 2) ++num; else 
			if (x[i] >=2 && x[i] >= 3 * p - 4 && s > 0) {
				++num;
				--s;
			}
		}
		printf("Case #%d: %d\n", ++ca, num);
	}
	return 0;
}