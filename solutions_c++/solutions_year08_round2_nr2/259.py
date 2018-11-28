#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

VI pr(1000005, 1);

void buildprime() {

	REP(d, pr.sz)
	{
		if (d >= 2 && pr[d])
		{
			int x = d;
			while (x+d <pr.sz)
			{
				x = x+d;
				pr[x] = 0;
			}
		}
	}

}

void testcase(int tst)
{
	ll a, b, p;
	
	ifs >> a >> b >> p;

	ll o = b-a+1;
	VI c(o);
	VVI r(o, VI());
	REP(i, o)
	{
		c[i] = i;
		r[i].pb(i);
	}


	for (ll d = p; d < b-a+50; d++)
		if (d < pr.sz && pr[d])
	{
		ll x = (((a-1)/d)+1)*d;
		if (x < a || x > b) continue;
		int cur = c[x-a];
		VI u;
		while (x + d <= b)
		{
			x = x + d;
			if (c[x-a] != cur) {
				u.pb(c[x-a]);
				c[x-a] = cur;
				r[cur].pb(x-a);
			}
		}
		REP(l, u.sz)
		{
			int y = u[l];
			REP(k, r[y].sz)
			{
				if (c[r[y][k]] != cur)
				{
					c[r[y][k]] = cur;
					r[cur].pb(r[y][k]);
				}
			}
			r[y].clear();
		}
	}

	int res = 0;
	VI was(o, 0);
	REP(i, o)
		if (!was[c[i]]) {
			was[c[i]] = 1;
			res++;
		}
		

	ofs << "Case #" << tst+1 << ": " << res << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	

	buildprime();

	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
