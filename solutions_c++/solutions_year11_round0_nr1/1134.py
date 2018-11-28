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

#define all(x) x.begin(), x.end()
#define sz(v) int(v.size())
#define fori(i,b,n) for (int i = b; i < n; i++)
#define forn(i,n) fori(i,0,n)
#define forall(i,v) forn(i,sz(v))
#define var(x,y) typeof(y) x = y
#define foreach(it,v) for (var(it,v.begin()); it != v.end(); it++)
#define forreach(it,v) for (var(it,v.rbegin()); it != v.rend(); it++)
#define pb(x) push_back(x)

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef set<int> iset;
typedef set<string> sset;

typedef map<int,int> iimap;

typedef vector<int> ivec;
typedef vector<vector<int> > iivec;

int main() {
	int T, N, res;
	char color;
	int pos, opos, bpos, ores, bres;
	cin >> T;
	forn(CASE,T) {
		res = 0;
		ores = bres = 0;
		opos = bpos = 1;
		cin >> N;
		while (N--) {
			cin >> color >> pos;
			if (color == 'O') {
				ores = res = max(abs(pos-opos)+ores, res)+1;
				opos = pos;
			} else {
				bres = res = max(abs(pos-bpos)+bres, res)+1;
				bpos = pos;
			}
		}
		printf("Case #%d: %d\n", CASE+1, res);
	}
	return 0;
}
