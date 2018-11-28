#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdint.h>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG
#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif
#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int move_digits(int n, int k)
{
	int mp = 0;
	int p = 1;
	FORN(i, 0, k){
		mp += (n % 10) * p;
		p *= 10;
		n /= 10;
	}
	int d = 1;
	while(d <= n) d *= 10;
	return d * mp + n;
}

int solve(int a, int b)
{
	set<pair<int, int> > rps;
	FORN(n, a, b){
		int p = 1;
		int nd = 0;
		while(p <= n){
			p *= 10;
			nd++;
		}
		FORN(k, 1, nd){
			int m = move_digits(n, k);
			if(m <= n) continue;
			if(m > b) continue;
			rps.insert(make_pair(n, m));
		}
	}
	return rps.size();
}

int main()
{
	int ntc;
	scanf("%d", &ntc);
	FORN(tc, 0, ntc){
		int a, b;
		scanf("%d%d", &a, &b);
		int s = solve(a, b);
		printf("Case #%d: %d\n", tc + 1, s);
	}
}
