#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

long long N;
int PD, PG;

void init() {
	cin >> N >> PD >> PG;
}

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
void work() {
	if (PD < 100 && PG == 100) { printf("Broken\n"); return; }
	if (PD > 0 && PG == 0) { printf("Broken\n"); return; }
    if (PD == 0) { printf("Possible\n"); return; }
	int d, ta;
	d = gcd(PD, 100);
	ta = 100 / d;
	if (N < ta) { printf("Broken\n"); return; }
	printf("Possible\n");
}

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++) {
		printf("Case #%d: ", ti);
		init();
		work();
	}
	return 0;
}
