#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

int main()
{
	ifstream fin("b.in"); ofstream fout("b.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int n;
		fin >> n;

		int ca, cb;

		map<string,vector<pair<int,int> > > clr;
		FOR(i, n)
		{
			string s;
			int a, b;
			fin >> s >> a >> b;
			clr[s].push_back(make_pair(a,b));
			ca = a, cb = b;
		}

		if (SZ(clr) < 2) clr["2"].push_back(make_pair(ca,cb));
		if (SZ(clr) < 3) clr["3"].push_back(make_pair(ca,cb));

		vector<vector<pair<int,int> > > c;
		for(map<string,vector<pair<int,int> > >::iterator it = clr.begin(); it != clr.end(); ++it)
		{
			c.push_back(it->second);
		}

		int m = SZ(c);
		int ans = 1000;

		FOR(i, m) FORD(j, i+1, m-1) FORD(k, j+1, m-1)
		{
			vector<pair<int,int> > d;
			FOR(z, SZ(c[i])) d.push_back(c[i][z]);
			FOR(z, SZ(c[j])) d.push_back(c[j][z]);
			FOR(z, SZ(c[k])) d.push_back(c[k][z]);

			sort(ALL(d));

			int st = 1, bi = -1, tmp = 0;
			FOR(z, SZ(d))
			{
				if (d[z].first <= st)
				{
					if (bi == -1) bi = z;
					if (d[bi].second < d[z].second)	bi = z;
				}
				else
				{
					if (bi == -1) break;
					st = d[bi].second + 1;
					bi = -1;
					++tmp;
					--z;
					if (st > 10000) break;
				}
			}

			if (bi != -1)
			{
				st = d[bi].second + 1;
				++tmp;
			}

			if (st > 10000) ans = min(ans, tmp);
		}

		if (ans < 1000)
			fout << "Case #" << tt+1 << ": " << ans << endl; 
		else
			fout << "Case #" << tt+1 << ": IMPOSSIBLE" << endl; 
	}
	return 0;	
}
