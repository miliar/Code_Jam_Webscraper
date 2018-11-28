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
#define FOREACH(i, c) FORAB(i, (c).begin(), (c).end())
#define RFOREACH(i, c) FORAB(i, (c).rbegin(), (c).rend())
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REV(c) reverse(ALL(c))
#define MAXE(c) max_element(ALL(c))
#define MINE(c) min_element(ALL(c))
#define MP(a, b) pair<__typeof(a), __typeof(b)> (a, b)
#define PB(c) push_back(c)
#define BLAH(a) cerr << a << endl
#define DBG(x) BLAH(#x << ": " << (x))
#define X first
#define Y second
#define SQ(e) (e)*(e)

#define ARPRNT(r) FOREACH(it2, (r)) cerr << (*it2) << ' '; BLAH("");
#define GRPRNT(c) BLAH(#c); FOREACH(it1, ((c))) { ARPRNT((*it1)); } BLAH("");

#define gin int TTT; cin >> TTT; for(int gtest = 1; gtest <= TTT; gtest++)
#define gout cout <<"Case #" << gtest << ": "
#define gprintf(s, a...) printf(strcat("Case #%i: ", s), a)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef pair<double, double> xy;
typedef long double LD;

typedef deque<int> DI;
typedef deque<DI> DDI;
typedef deque<string> DS;
typedef pair<int, int> PII;
typedef deque<PII> DPII;

int gcd(int a, int b)
{
	if(!b) return a;
	return gcd(b, a % b);
}

int r, c;

bool dfs(vector<vector<char> >& g, int h, int l)
{
	//DBG(h); DBG(l); GRPRNT(g);
	//`BLAH("");
	if(h + 1 == r || l + 1 == c) return false;
	if(g[h][l+1] == '#' && g[h+1][l] == '#' && g[h+1][l+1] == '#')
	{
		g[h][l] = '/'; g[h][l+1] = '\\'; g[h+1][l] = '\\'; g[h+1][l+1] = '/';
		int nh = -1, nl;
		for(int i = 0; i < r && nh == -1; i++) FOR(j, c) if(g[i][j] == '#') { nh = i; nl = j; break; }
		if(nh == -1) return true;
		return dfs(g, nh, nl);
	}
	else
		return false;
}

int main()
{
	gin
	{
		cin >> r >> c;
		vector<vector<char> > g(r, vector<char> (c, false));
		FOR(i, r)
			FOR(j, c)
				cin >> g[i][j];
		int h = -1, l = 0; //high, left
		FOR(i, r) if(h == -1) { FOR(j, c) if(g[i][j] == '#') { h = i; l = j; break; } }
		bool good = true;
		if(h != -1)
		good = dfs(g, h, l);
		if(!good)
			gout << endl << "Impossible" << endl;
		else
		{
			gout<<endl;;
			FOR(i, r)
			{
				FOR(j, c) cout << g[i][j];
				cout << endl;
			}
		}
	}
}
