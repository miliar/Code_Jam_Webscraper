#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#define LD long double
using namespace std;

LD p[111111];
int _, a, b;
double x;
LD sol;

void solve(){
	p[0] = 1;
	scanf("%d%d", &a, &b);
	for (int i = 1; i <= a; i++){
		scanf("%lf", &x);
		p[i] = p[i - 1] * x;
	}
	sol = b + 2;
	for (int bak = 0; bak <= a; bak++)
		sol = min(sol, p[a - bak] * (LD)(bak + b - a + bak + 1) + (1 - p[a - bak]) * (LD)(bak + b - a + bak + 1 + b + 1));
	printf("%.10lf\n", (double)sol);
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &_);
	for (int tst = 1; tst <= _; tst++){
		printf("Case #%d: ", tst);
		solve();
	}

	return 0;
}
