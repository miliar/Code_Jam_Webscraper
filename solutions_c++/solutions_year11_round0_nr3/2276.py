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
#define DBG(a) BLAH(#a << ": " << a)

#define gin int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gout cout <<"Case #" << gtest << ": "

int gcd(int a, int b)
{
	if(!b) return a;
	return gcd(b, a % b);
}

int solve(vector<int>& c)
{
	int best = -1;
	FOR(i, c.size())
	{
		int p = 0, r = 0;
		FOR(j, c.size())
		{
			if(i == j) continue;
			else { p ^= c[j]; r += c[j]; }
		}
		best = !(p - c[i]) ? max(best, r) : -1;
	}
	return best;
}

int main()
{
	gin
	{
		int n; cin >> n;
		vector<int> candy(n);
		FOR(i, n)
			cin >> candy[i];
		int ans = solve(candy);
		if(ans != -1)
			gout << ans << endl;
		else
			gout << "NO" << endl;
	}
}
