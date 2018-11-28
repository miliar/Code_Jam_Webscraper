#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>

#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <list>

#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) a.size() - 1
#define all(a) a.begin(), a.end()
#define I (int)
#define I64 (long long)
#define LD (long double)
#define VI vector<int>
#define pti pair<int, int>
#define ptd pair<long double, long double>
#define sqr(x) ((x) * (x))

const long double EPS = 1E-9;
const int INF = (int)1E9;
const long long INF64 = (long long)1E18;
const long double PI = 2 * acos(.0);

typedef long double ld;
typedef long long ll;

int p, q;
int a[100010];

vector<int> v;

int getVal() {
	set<int> s;
	forn(i, q)
		s.insert(a[i]);

	s.insert(0);
	s.insert(p + 1);
	int ans = 0;

	forn(j, q) {
		set<int>::iterator it = s.lower_bound(a[v[j]]);
		it--;
		int l = *it;
		it = s.upper_bound(a[v[j]]);
		int r = *it;
		s.erase(a[v[j]]);
		ans += r - l - 2;	
	}

	return ans;
}

void solve() {
	scanf("%d%d", &p, &q);
	int ans = INF;

	v.resize(q);	
	forn(i, q) {
		scanf("%d", &a[i]);		
		v[i] = i;
	}
	
	do {
		ans = min(ans, getVal());
	} while (next_permutation(all(v)));


	printf("%d\n", ans);
}


int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int n;
	scanf("%d", &n);
	forn(i, n) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	
    return 0;
}
