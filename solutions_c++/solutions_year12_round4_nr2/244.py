//b Hewr
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
#define fo(i,a,b) for (int i = a; i <= b; ++i)
#define MP make_pair
#define fi first
#define se second
#define updmax(a,b) a = max(a, b)
#define sqr(x) ((x) * (x))

typedef pair<double, double> po;

const double eps = 1e-8;
const int mn = 1100;

po a[mn];
int r[mn], b[mn];
int n, W, L;

int sgn(double x){
	if (fabs(x) <= eps) return 0;
	if (x > eps) return 1;
	return -1;
}

double dis(po a, po b){
	return sqrt(sqr(a.fi - b.fi) + sqr(a.se - b.se));
}

double ran(int x){
	return (rand() * RAND_MAX + rand()) % x;
}

bool cmp(int x, int y){
	return r[x] > r[y];
}

bool chk(int p){
	fo (i, 1, p - 1) if (sgn(dis(a[b[i]], a[b[p]]) - r[b[i]] - r[b[p]]) < 0) 
		return 0;
	return 1;
}

int main(){
	int T;
	cin >> T;
	fo (Ca, 1, T){
		cin >> n >> W >> L;
		fo (i, 1, n){
			cin >> r[i];
			b[i] = i;
		}
		sort(b + 1, b + n + 1, cmp);
		fo (i, 1, n) do {
			a[b[i]] = MP(ran(W), ran(L));
		} while (!chk(i));
		printf("Case #%d:", Ca);
		fo (i, 1, n) printf(" %.1f %.1f", a[i].fi, a[i].se);
		printf("\n");
	}
}
