#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
#include <memory.h>
#include <ctype.h>

#include <iostream>

#include <string>
#include <complex>
#include <numeric>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>

//#pragma comment(linker, "/stack:64000000")

using namespace std;

template<typename TYPE> inline TYPE sqr(const TYPE& a) { return (a) * (a); }

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1000 * 1000 * 1000;
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 100;

const char _A = 'O';
const char _B = 'B';

void solve(int test) {
	int n;
	scanf("%d", &n);
	queue<int> a, b;
	queue<pair<char, int> > com;
	forn(i, n) {
		char x;
		int y;
		scanf(" %c %d", &x, &y);
		com.push(mp(x, y));
		if(x == _A) {
			a.push(y);
		} else {
			b.push(y);
		}
	}
	int ans = 0;
	int ap = 1, bp = 1;
	while(!com.empty()) {
		bool flag_a = false, flag_b = false;
		if(com.front().first == _A) {
			if(com.front().second == ap) {
				assert(ap == a.front());
				a.pop();
				com.pop();
				flag_a = true;
			}
		} else {
			if(com.front().second == bp) {
				assert(bp == b.front());
				b.pop();
				com.pop();
				flag_b = true;
			}
		}
		if(!a.empty() && !flag_a) {
			int goal = a.front();
			if(goal < ap) {
				--ap;
			} else if(goal > ap) {
				++ap;
			}
		}
		if(!b.empty() && !flag_b) {
			int goal = b.front();
			if(goal < bp) {
				--bp;
			} else if(goal > bp) {
				++bp;
			}
		}
		++ans;
	}
	printf("Case #%d: %d\n", test, ans);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	scanf("%d\n", &tests);

	for1(it, tests) {
		solve(it);		
	}
	

	return 0;
}
