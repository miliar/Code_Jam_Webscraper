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

int a[1000000];
int main() {
	int64 T, L, t, N, C;
	cin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		cin >> L >> t >> N >> C;
		forn(i,C) cin >> a[i];
		fori(i,C,N) a[i] = a[i%C];
		int64 count = 0, begin = -1;
		int64 sum = accumulate(a, a+N, 0ll)*2;
		
		vector<int64> dec;
		forn(i,N) {
			count += a[i]*2;
			if (count >= t) {
				dec.push_back((count - t)/2);
				while (++i < N)
					dec.push_back(a[i]);
			}
		}
		
		printf("Case #%d: ", CASE);
		//cout << sum << ',';
		sort(all(dec));
		int i = dec.size();
		while (L-- > 0 && --i >= 0) 
			sum -= dec[i];
		cout << sum << endl;
	}
	return 0;
}
