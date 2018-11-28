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
	int T, N, C, x, m;
	long long sum;
	cin >> T;
	forn(CASE,T) {
		cin >> N;
		sum = 0;
		x = 0;
		m = 1<<30;
		while (N--) {
			cin >> C;
			x ^= C;
			m = min(m, C);
			sum += C;
		}
		printf("Case #%d: ", CASE+1);
		if (x) cout << "NO";
		else cout << sum - m;
		cout << endl;
	}
	return 0;
}
