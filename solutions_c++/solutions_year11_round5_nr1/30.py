#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <double, double> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

const int nmax = 150;

pii a[nmax];
pii b[nmax];
int w, n, m, c;

double calc(pii *a, int n, double r){
	double res = 0;
	for (int i = 0; i < n-1; i++){
		if (a[i].x >= r) break;
		pii rgt = a[i+1];
		if (rgt.x > r){
			rgt.y = a[i].y + (r - a[i].x) * (a[i+1].y - a[i].y) / (a[i+1].x - a[i].x);
			rgt.x = r;
		}
		res += (rgt.x - a[i].x) * (rgt.y + a[i].y) / 2;
	}
	return res;
}

double calc(double r){
	double res = calc(b, m, r) - calc(a, n, r);
	return res;
}


void solve(){
	puts("");
	cin >> w >> n >> m >> c;
	forn(i, n)
		cin >> a[i].x >> a[i].y;
	forn(i, m)
		cin >> b[i].x >> b[i].y;
	double now = calc(w) / c;
	double left = 0;
	for (int i = 0; i < c-1; i++){
		double l, r, mid;
		l = left;
		r = w;
		forn(j, 50){
			mid = (l + r) / 2;
			if (calc(mid) < (i + 1) * now)
				l = mid;
			else
				r = mid;
		}
		printf("%0.9lf\n", l);
	}
}	        

int main ()
{
	int tst;
	cin >> tst;
	forn(i, tst){
		printf("Case #%d: ", i + 1);
		solve();
	}

	
	return 0;
}
