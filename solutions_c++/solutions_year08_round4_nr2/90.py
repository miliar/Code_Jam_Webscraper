#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

long long n, m;
long long s;

void outdata() {
}

long long ABS(long long x) {
	if (x < 0) return -x;
	return x;
}

bool tryit(long long vx1, long long vy1, long long vx2, long long vy2) {
	long long lx = max(max(-vx1, -vx2), 0LL);
	long long rx = min(min(n - vx1, n - vx2), n);
	if (rx < lx) return false;
	long long ly = max(max(-vy1, -vy2), 0LL);
	long long ry = min(min(m - vy1, m - vy2), m);
	if (ry < ly) return false;
	cout << lx << " " << ly << " " << lx + vx1 << " " << ly + vy1 << " " << lx + vx2 << " " << ly + vy2 << endl;
	assert(0 <= lx && lx <= n);
	assert(0 <= lx + vx1 && lx + vx1 <= n);
	assert(0 <= lx + vx2 && lx + vx2 <= n);
	assert(0 <= ly && ly <= m);
	assert(0 <= ly + vy1 && ly + vy1 <= m);
	assert(0 <= ly + vy2 && ly + vy2 <= m);
	assert(ABS(vx1 * vy2 - vx2 * vy1) == s);
	return true;
}


void solve() {
	//x1 != 0
	for(long long x1 = -n; x1 <= n; ++x1) if (x1 != 0) {
		for(long long y1 = -m; y1 <= m; ++y1) {
			for(long long x2 = -n; x2 <= n; ++x2) {
				for(int t = -1; t <= 1; t += 2) {
    				long long q = t * s + x2 * y1;
    				if (q % x1 != 0) continue;
    				long long y2 = q / x1;
                    if (tryit(x1, y1, x2, y2)) return ;
    			}
			}
		}
	}
	long long x1 = 0;
   	for(long long y1 = -m; y1 <= m; ++y1) if (y1 != 0) {
   		for(long long y2 = -m; y2 <= m; ++y2) {
  			for(int t = -1; t <= 1; t += 2) {
  				long long q = t * s + x1 * y2;
  				if (q % y1 != 0) continue;
  				long long x2 = q / y1;
                if (tryit(x1, y1, x2, y2)) return ;
 			}
        	   			
   		}
	}
	cout << "IMPOSSIBLE" << endl;
}

void readdata() {
	cin >> n >> m >> s;
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		readdata();
		solve();
		outdata();
	}
	return 0;
}
