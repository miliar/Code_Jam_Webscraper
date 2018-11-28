#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
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
typedef vector<bool> VB;
typedef vector<double> VD;
typedef vector<PII> VPI;
typedef vector<VPI> VVPI;
typedef set<string> SET;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef vector<int> VI;
typedef vector<string> VS;

int toInt(string s, int t)
{
	replace(ALL(s), ':', ' ');
	istringstream in(s);
	int h, m;
	in >> h >> m;
	return 60*h+m+t;
}
char buffer[1024];
int main()
{
    freopen("q1.in", "r", stdin);
    freopen("q1.out", "w+", stdout);
	int n;
	cin >> n;
	REP(it,n)
	{
		int t;
		cin >> t;
		VS E;
		cin.getline(buffer, 1024);
		REP(i,t)
		{
			cin.getline(buffer, 1024);
			string s = buffer;
			E.pb(s);
		}
		int q;
		cin >> q;
		VS Q;
		cin.getline(buffer, 1024);
		REP(i,q)
		{
			cin.getline(buffer, 1024);
			string s = buffer;
			Q.pb(s);
		}
		VI C(SZ(E), 0);
		VI N(SZ(E), 0);
		REP(qn,SZ(Q))
		{
			string q = Q[qn];
			C = N;
			fill(ALL(N), INF);
			REP(i,SZ(C))
				if (C[i] != INF)
				{
					if (E[i] != q)
					{
						N[i] = min(N[i], C[i]);
					}
					else
					{
						REP(j,SZ(N))
							if (i != j)
								N[j] = min(N[j], C[i]+1);
					}
				}
		}
		cout << "Case #" << it+1 << ": "<< *min_element(ALL(N)) << endl;
	}
}
