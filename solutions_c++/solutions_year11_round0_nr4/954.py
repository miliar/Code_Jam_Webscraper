#include <cstdio>
using namespace std;

double F[1111];

double dpr[1111][2];
bool visr[1111][2];
double rec(int n, int loose) {
    if(visr[n][loose]) {
	return dpr[n][loose];
    }
    visr[n][loose] = true;
    if(n == 0) {
	return 0.0;
    }
    if(n == 1) {
	return dpr[n][loose] = 1.0 * loose;
    }
    if(!loose) {
	return dpr[n][loose] = 1.0 * (n - 1) / n * rec(n - 1, 1);
    }
    else {
	return dpr[n][loose] = (1.0 * (n - 1) * rec(n - 1, 1) + rec(n - 1, 0)) / n;
    }
}

double dpc[1111];
bool visc[1111];
double calc(int n) {
    if(visc[n]) {
	return dpc[n];
    }
    visc[n] = true;
    if(n == 0) {
	return dpc[n] = 0.0;
    }
    double ret = 1;
    for(int i = 1; i <= n; ++i) {
	ret += 1.0 * rec(n - i, 0) * calc(n - i) / F[i];
    }
    return dpc[n] = ret / (1 - rec(n, 0));
}

void solve(int test) {
    printf("Case #%d: ", test);
    int n;
    scanf("%d", &n);
    int cnt = 0;
    for(int i = 1; i <= n; ++i) {
	int a;
	scanf("%d", &a);
	if(a != i) {
	    cnt++;
	}
    }
    //printf("%.8lf %.8lf\n", calc(cnt), 1.0 * cnt);
    printf("%.8lf\n", 1.0 * cnt);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    F[0] = 1.0;
    for(int i = 1; i <= 1000; ++i) {
	F[i] = F[i - 1] * i;
    }
    for(int i = 1; i <= 4; ++i) {
	fprintf(stderr, "p[%d] = %.5lf\n", i, rec(i, 0));
    }
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
	solve(i);
    }
    return 0;
}
