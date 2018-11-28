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
	int T, N, L, H, res;
	cin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		cin >> N >> L >> H;
		int a[N]; forn(i,N) cin >> a[i];
		bool failed;
		fori (f,L,H+1) {
			failed = false;
			forn(i,N) if (!(a[i] % f == 0 || f % a[i] == 0)) {
				failed = true;
				break;
			}
			if (!failed) {
				res = f;
				break;
			}
		}
		
		printf("Case #%d: ", CASE);
		if (failed) puts("NO");
		else printf("%d\n", res);
	}
	return 0;
}
