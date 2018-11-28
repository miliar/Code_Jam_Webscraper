#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int t;
	cin >> t;

	REP (tt, t)
	{
		cout << "Case #" << (tt+1) << ":";

		int n, m ;
		cin >> n >> m;

		vector <string> a(n);

		REP (i, n)
			cin >> a[i];

		while (m--)
		{
			string s;
			cin >> s;

			map <pair<string, int>, set<char> > M;

			REP (i, n)
			{
				string ss(a[i].size(), '*');

				REP (j, s.size()+1)
				{
					REP (k, a[i].size())
						M[make_pair(ss, j)].insert(a[i][k]);

					if (j < s.size())
						REP (k, a[i].size())
							if (a[i][k] == s[j])
								ss[k] = s[j];
				}
			}

			int res = 0;
			string ress = a[0];

			REP (i, n)
			{
				string ss(a[i].size(), '*');

				int r = 0;

				REP (j, s.size())
				{
					if (ss == a[i])
						break;

					if (!M[make_pair(ss, j)].count(s[j]))
						continue;

					bool good = false;

					REP (k, a[i].size())
						if (a[i][k] == s[j])
						{
							good = true;
							ss[k] = s[j];
						}
					if (!good) r++;
				}

				if (r > res)
				{
					res = r;
					ress = a[i];
				}
			}

			cout << " " << ress;
		}
		cout << endl;
	}

	return 0;
}
