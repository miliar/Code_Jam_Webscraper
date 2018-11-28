#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
using namespace std;

#define VAR(a, b) __typeof(b) a = b
#define FORAB(i, a, b) for(VAR(i, a); i != b; i++)
#define FOR(i, n) FORAB(i, 0, n)
#define RFOR(i, a, b) for(VAR(i, a); i != b; i--)
#define FOREACH(it, c) FORAB(i, (c).begin(), (c).end())
#define RFOREACH(it, c) FORAB(i, (c).rbegin(), (c).rend())
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) pair<__typeof(a), __typeof(b)> (a, b)
#define PB(c) push_back(c)
#define BLAH(a) cerr << a << endl
#define DBG(x) BLAH(#x << ": " << x)

#define ARPRNT(r) FOREACH(it, r) cerr << r << ' '; BLAH("");
#define GRPRNT(c) FOREACH(it, c) { ARPRNT(*it); } BLAH(""); 

#define gin int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gout cout <<"Case #" << gtest << ": "
#define gprintf(s, a...) printf(strcat("Case #%i: ", s), a)

int gcd(int a, int b)
{
	if(!b) return a;
	return gcd(b, a % b);
}

int blah[101] = {0, 100, 50, 100, 25, 20, 50, 100, 25, 100, 10, 100, 25, 100, 50, 20, 25, 100, 50, 100, 5,
100, 50, 100, 25, 4, 50, 100, 25, 100, 10, 100, 25, 100, 50, 20, 25, 100, 50, 100, 5, 100, 50, 100, 25,
20, 50, 100, 25, 100, 2, 100, 25, 100, 50, 20, 25, 100, 50, 100, 5, 100, 50, 100, 25, 20, 50, 100, 25,
100, 10, 100, 25, 100, 50, 4, 25, 100, 50, 100, 5, 100, 50, 100, 25, 20, 50, 100, 25, 100, 10, 100, 25, 
100, 50, 20, 25, 100, 50, 100, 1}; 

int main()
{
	gin
	{
		int pd, pg;
		long long int n;
		cin >> n >> pd >> pg;
		DBG(n);
		DBG(pd);
		DBG(pg);
		bool good = false;
		good = blah[pd] <= n;
		good &= (!pg && !pd) || (pg && (double)pd / blah[pd] - (double) pg/blah[pg] >= 0);
		gout << (good ? "Possible" : "Broken") << endl;
	}
}
