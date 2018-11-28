// GCJ Round 2 - Problem B
// -- strapahuulius

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
const LL OO = 1000000000000000000LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}
class mersenne_twister
{
	private:
	unsigned MT[624];
	double v;
	bool precalc;
	int ix;
	void init(unsigned seed=0)
	{
		precalc = false;
		ix = 0;
		MT[0] = seed;
		for (unsigned i=1; i<624; i++)
			MT[i] = 1812433253u * (MT[i-1] ^ (MT[i-1]>>30)) + i;
	}
	void generate()
	{
		for (int i=0; i<624; i++)
		{
			unsigned y = (MT[i] & 1) + (MT[i==623?0:i+1] & ((1u<<31)-1));
			MT[i] = MT[i+397>=624?i+397-624:i+397] ^ (y >> 1);
			if (y & 1)
				MT[i] ^= 2567483615u;
		}
	}
	public:
	unsigned next()
	{
		if (ix == 0)
			generate();
		unsigned y = MT[ix];
		y ^= y >> 11;
		y ^= (y << 7) & 2636928640u;
		y ^= (y << 15) & 4022730752u;
		y ^= y >> 18;
		if (++ix >= 624)
			ix = 0;
		return y;
	}
	mersenne_twister() { init(); }
	double rand01() { return next() * .00000000023283064365; }
	double gaussian()
	{
		if (precalc)
		{
			precalc = false;
			return v;
		}
		double x, y, r2;
		do
		{
			x = 2 * rand01() - 1.0;
			y = 2 * rand01() - 1.0;
			r2 = x*x + y*y;
		} while (r2 > 1 || r2 == 0);
		double s = sqrt(-2.0 * log(r2) / r2);
		double u = s * x;
		v = s * y;
		precalc = true; // XXX
		return u;
	}

} mt;
// code written during the competition follows
LL X[1024], Y[1024];
LL sq(LL x) { return x * x; }
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int n;
		LL w, l;
		cin >> n >> w >> l;
		vector<LL> r(n);
		for (int i=0; i<n; i++)
		{
			cin >> r[i];
		}
		vector<int> p;
		for (int i=0; i<n; i++)
			p.push_back(i);
		int tmp = 0;
		while (1)
		{
			if (++tmp & 1)
				random_shuffle(p.begin(), p.end());
			else
			{
				vector<PII> v;
				for (int i=0; i<n; i++)
					v.push_back(PII(r[i], i));
				sort(v.begin(), v.end());
				for (int i=0; i<n; i++)
					p[i] = v[n - 1 - i].second;
			}
			bool solved = true;
			for (int i=0; i<n; i++)
			{
				LL R = r[p[i]];
				bool good = false;
				for (int j=0; j<15; j++)
				{
					LL x = mt.next() % (w + 1);
					LL y = mt.next() % (l + 1);
					good = true;
					for (int j=0; j<i; j++)
						if (sq(x - X[p[j]]) + sq(y - Y[p[j]]) < sq(R + r[p[j]]))
						{
							good = false;
							break;
						}
					if (good)
					{
						X[p[i]] = x;
						Y[p[i]] = y;
						break;
					}
				}
				if (!good)
				{
					solved = false;
					break;
				}
			}
			if (solved)
				break;
		}
		printf("Case #%d:", tkase+1);
		for (int i=0; i<n; i++)
			cout << " " << X[i] << " " << Y[i];
		cout << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
