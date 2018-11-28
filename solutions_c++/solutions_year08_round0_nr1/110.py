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

char ss[10000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	gets(ss);
	int tt;
	sscanf(ss, "%d", &tt);

	REP (t, tt)
	{
		cout << "Case #" << (t+1)<<": ";
		gets (ss);
		int n;
		sscanf (ss, "%d", &n);
		map <string, int> M;
		REP (i, n)
		{
			gets (ss);
			M[string(ss)] = i;
		}
		int m;
		gets (ss);
		sscanf (ss, "%d", &m);
		VI a;
		REP (i, m)
		{
			gets (ss);
			a.pb (M[string(ss)]);
		}

		VVI res(m+1, VI(n, INF));
		REP (i, n)
			res[0][i] = 0;

		REP (i, m)
		{
			int mi=INF;
			REP (j, n)
			{
				mi<?=res[i][j];
				if (j!=a[i])
				{
					res[i+1][j]<?=res[i][j];
				}
			}
			REP (j, n)
				if (j!=a[i])
					res[i+1][j]<?=mi+1;
		}

		int r = INF;
		REP (i, n)
			r<?=res[m][i];

		cout << r << endl;
	}
	return 0;
}
