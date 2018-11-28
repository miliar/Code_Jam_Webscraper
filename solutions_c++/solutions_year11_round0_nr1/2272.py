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

#define ARPRNT(r) FOREACH(it, r) cerr << r << ' '; BLAH("");
#define GRPRNT(c) FOREACH(it, c) { ARPRNT(*it); BLAH(""); }

#define gin int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gout cout <<"Case #" << gtest << ": "
#define gprintf(s, a...) printf(strcat("Case #%i: ", s), a)

int gcd(int a, int b)
{
	if(!b) return a;
	return gcd(b, a % b);
}

struct but
{
	bool isO;
	int k;
	but();
	but(bool i, int k) : isO(i), k(k) {}
};

int main()
{
	gin 
	{
		int n;
		cin >> n;
		deque<but> bs;
		deque<int> bpos, opos;
		FOR(i, n)
		{
			char c; int k;
			cin >> ws >> c >> ws >> k;
			bs.PB(but(c == 'O', k));
			if(bs.back().isO) opos.PB(k);
			else bpos.PB(k);
		}
		int p = 0, t = 0;
		int bc = 1, oc = 1, bb = 0, ob = 0;
		bool bm = false, om = false;
		while(n - p > 0)
		{
			t++;
			if(bb < bpos.size() && bc != bpos[bb])
			{
				bm = true;
				bc += bpos[bb] > bc ? 1 : -1;
			}
			if(ob < opos.size() && oc != opos[ob])
			{
				om = true;
				oc += opos[ob] > oc ? 1 : -1;
			}
			if(!om && bs[p].isO && opos[ob] == oc)
			{
				p++;
				ob++;
			}
			else if(!bm && !bs[p].isO && bpos[bb] == bc)
			{
				p++;
				bb++;
			}
			bm = false; om = false;
		}
		gout << t << endl;
	}
}
