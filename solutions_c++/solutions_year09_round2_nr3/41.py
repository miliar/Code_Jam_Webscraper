// GCJ Round 1B - Problem C
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

// code written during the competition follows
string dp[23][23][4050];
int unused[23][23][4050];
const int X[] = {0, 1, 0, -1};
const int Y[] = {1, 0, -1, 0};
#define INSIDE(x, y) ((x) >= 0 && (y) >= 0 && (x) < w && (y) < w)
bool better(string s, string t)
{
	return s.size() < t.size() || s.size() == t.size() && s < t;
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int w, q;
		cin >> w >> q;
		VS v(w);
		for (int i=0; i<w; i++)
		{
			cin >> v[i];
		}
		printf("Case #%d:\n", tkase+1);
		for (int i=0; i<w; i++)
			for (int j=0; j<w; j++)
				for (int k=0; k<4050; k++)
					dp[i][j][k].clear();
		memset(unused, 0, sizeof unused);
		for (int len=0; len<500; len+=2) // TODO
		{
			int L = len;
			if (len)
				L--;
			for (int i=0; i<w; i++)
				for (int j=0; j<w; j++)
				{
					if (!isdigit(v[i][j]))
						continue;
					for (int val=-500; val<=500; val++)
					{
						int xx = val + 2000;
						if ((int)dp[i][j][xx].size() != L)
							continue;
						if (dp[i][j][xx].empty() && (len || val))
							continue;
						unused[i][j][xx] = 1;
						for (int k=0; k<4; k++)
							for (int z=0; z<4; z++)
							{
								int x0 = i + X[k];
								int y0 = j + Y[k];
								int x1 = x0 + X[z];
								int y1 = y0 + Y[z];
								if (!INSIDE(x0, y0) || !INSIDE(x1, y1))
									continue;
								int op = (len == 0 || v[x0][y0] == '+') ? 1 : -1;
								int res = val + op * (int)(v[x1][y1]-'0');
								string &r = dp[x1][y1][res+2000];
								string t = dp[i][j][xx];
								if (len)
									t += v[x0][y0];
								t += v[x1][y1];
								if (r.empty() || better(t, r))
								{
									r = t;
//									cout << res << " " << t << endl;
								}
							}
					}
				}
		}
		for (int t=0; t<q; t++)
		{
			int qq;
			cin >> qq;
			string sol(10000, 'X');
			for (int i=0; i<w; i++)
				for (int j=0; j<w; j++)
				{
					string &r = dp[i][j][qq+2000];
					if (!r.empty() && better(r, sol))
						sol = r;
				}
			assert(sol.size() < 10000);
			cout << sol << endl;
		}
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
