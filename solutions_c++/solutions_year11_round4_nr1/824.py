#include <iostream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <stack>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(a) (int)a.size()

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

struct z{
	int X, Y, w;
	z(){};
};
const double EPS = 1e-9;
z p[10000], a[10000];
bool cmp(const z & a, const z & b){
	return a.w < b.w;
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;

	forn(test, tests){
		int x, s, r, n;
		double t;
		cin >> x >> s >> r >> t >> n;
		forn(i, n){
			cin >> p[i].X >> p[i].Y >> p[i].w;
		}
		int st = 0;
		int m = 0;
		forn(i, n){
			if(st != p[i].X){
				a[m].X = st;
				a[m].Y = p[i].X;
				a[m++].w = 0;
				st = p[i].X;
			}
			a[m++] = p[i];
			st = p[i].Y;
		}
		if(st != x){
			a[m].X = st;
			a[m].Y = x;
			a[m++].w = 0;
		}
		n = m;
		sort(a, a + n, cmp);
	
		double ans = 0;
		forn(i, n){
			if(t > EPS){
				if(double(a[i].Y - a[i].X) / double(r + a[i].w) <= t + EPS){
					t -= double(a[i].Y - a[i].X) / double(r + a[i].w);
					ans += double(a[i].Y - a[i].X) / double(r + a[i].w);
				}else{
					double len = t * (r + a[i].w);
				
					ans += t + double(a[i].Y - a[i].X - len) / double(s + a[i].w);
					t = 0;
				}
			}else{
				ans += double(a[i].Y - a[i].X) / double(s + a[i].w);
			}
		}
		printf("Case #%d: %.9lf\n", test + 1, ans);

	}
	return 0;
}