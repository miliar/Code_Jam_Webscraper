#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const int nMax= 1003;
int t[nMax];
int nwd(int a, int b) {
	if (a == 0) return b;
	if (b == 0) return a;
	if (a > b) return nwd(b, a % b);
	else return nwd(a, b % a);
}
int main() {
	int c; scanf("%d", &c);
	for(int i = 1; i <= c; i++) {
		int n, a; scanf("%d", &n);
		//printf("%d", nwd(n, a));
		for(int j = 0; j < n; j++) scanf("%d", t+j);
		printf("Case #%d: ", i);
		sort(t, t+n);
		if (n == 2) a = t[1] - t[0];
		else a = nwd(t[1]-t[0], t[2] - t[1]);
		//printf("%d\n", a);
		//printf("%d", (-32) % 12);
		if (t[0] % a == 0) printf("0\n");
		else printf("%d\n", a+(-t[0]) % a);
	
	}
}
