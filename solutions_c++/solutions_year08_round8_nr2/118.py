// Muenchen ist die beste Stadt der Welt!
// GCJ EMEA Onsite - Problem B
// I can't tell you how proud I am,
// I'm writing down things that I don't understand.
// -- blackmath

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
// code written during the competition follows
map<string, int> mp;
struct Fence
{
	int a, b, color;
	void read()
	{
		string c;
		cin >> c >> a >> b;
		int k = mp.size();
		if (mp.count(c))
			color = mp[c];
		else
			color = mp[c] = k;
	}
	bool operator<(const Fence &f) const
	{
		return a < f.a;
	}
};
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		mp.clear();
		int n;
		cin >> n;
		vector<Fence> v;
		for (int i=0; i<n; i++)
		{
			Fence f;
			f.read();
			v.push_back(f);
		}
		sort(v.begin(), v.end());
		int z = mp.size();
		vector<vector<Fence> > vv(z);
		FORIT(it, v)
			vv[it->color].push_back(*it);
		int best = oo;
		
		for (int i=0; i<z; i++)
			for (int j=i; j<z; j++)
				for (int k=j; k<z; k++)
				{
					vector<Fence> w;
					FORIT(it, vv[i])
						w.push_back(*it);
					FORIT(it, vv[j])
						w.push_back(*it);
					FORIT(it, vv[k])
						w.push_back(*it);
					sort(w.begin(), w.end());
					int sofar = 0;
					int cnt = 0;
					int pos = 0;
					while (sofar < 10000 && pos < (int)w.size())
					{
						int next = -1;
						int sofar2 = sofar;
						while (pos < (int)w.size())
						{
							if (w[pos].a <= sofar + 1)
							{
								next = max(next, w[pos].b);
								pos++;
							}
							else
								break;
							sofar2 = next;
						}
						if (next == -1)
							break;
						sofar = sofar2;
						cnt++;
					}
					if (sofar == 10000)
					{
						best = min(best, cnt);
					}
				}
		printf("Case #%d: ", tkase+1);
		if (best == oo)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << best << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
