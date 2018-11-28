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
	int T, R, C;
	cin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		cin >> R >> C;
		string lines[R];
		forn(i,R) cin >> lines[i];
		bool impossible = false;
		forn(i,R) {
			forn(j,C)	{
				if (lines[i][j] == '#') {
					if (j+1 < C && lines[i][j+1] == '#' &&
						i+1 < R && lines[i+1][j] == '#' && lines[i+1][j+1] == '#') {
						lines[i][j] = '/';
						lines[i][j+1] = '\\';
						lines[i+1][j] = '\\';
						lines[i+1][j+1] = '/';
					} else {
						impossible = true;;
					}
				}
			}
		}
		printf("Case #%d:\n", CASE);
		if (impossible)
			puts("Impossible");
		else
			forn(i,R)
				puts(lines[i].c_str());
	}
	return 0;
}
