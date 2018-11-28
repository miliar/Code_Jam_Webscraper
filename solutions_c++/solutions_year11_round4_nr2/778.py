#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#define all(x) (x).begin(), (x).end()
#define sz(v) int((v).size())
#define fori(i,b,n) for (int i = (b); i < (n); i++)
#define forn(i,n) fori(i,0,n)
#define forall(i,v) forn(i,sz(v))
#define var(x,y) typeof(y) x = y
#define foreach(it,v) for (var(it,(v).begin()); it != (v).end(); it++)
#define forreach(it,v) for (var(it,(v).rbegin()); it != (v).rend(); it++)

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef set<int> iset;
typedef set<string> sset;

typedef map<int,int> iimap;

typedef vector<int> ivec;
typedef vector<vector<int> > iivec;

int main() {
	int T;
	cin >> T;
	forn (CASE, T) {
		int res = 1;
		int R, C, D;
		cin >> R >> C >> D;
		int w[R][C];
		char ch;
		forn(r,R) forn(c,C) {
			cin >> ch;
			w[r][c] = D + (ch - '0');
		}
		int md = 3;
		forn(r,R) forn(c,C) fori(d,md,11){
			if (r+d <= R && c+d <= C) {
				int64 x = 0, y = 0;
				double m = 0;
				fori(rd,r,r+d) fori(cd,c,c+d) {
					if ((cd == c || cd == c+d-1) && (rd == r || rd == r+d-1)) continue;
					x += rd * w[rd][cd];
					y += cd * w[rd][cd];
					m += w[rd][cd];
				}
				//cout << x/m << ',' << y/m << endl;
				//cout << r+d/2.0 << ',' << c+d/2.0 << endl;
				if (x/m==r+(d-1)/2.0 && y/m==c+(d-1)/2.0)
						res = md = d;
			}
		}
		printf("Case #%d: ", CASE+1);
		if (res < 3) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}
