#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <list>

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define ALL(cont) cont.begin(), cont.end()

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<double> vd;

typedef complex<int> ci;
typedef pair<ci, ci> rect; 

istream& operator>>(istream &is, ci &rhs)
{
	int x, y;
	is >> x >> y;
	rhs = ci(x, y);
	return is;
}

//bool operator<(const ci &lhs, const ci &rhs)
//{
//	return lhs.real() != rhs.real() ? lhs.real() < rhs.real() : lhs.imag() < rhs.imag();
//}

//bool operator<(const rect &lhs, const rect &rhs)
//{
//	return lhs.first < rhs.first;
//}

bool intersect(const rect &a, const rect &b)
{
	return
		a.first.real() <= b.second.real() &&
		a.first.imag() <= b.second.imag() &&
		b.first.real() <= a.second.real() &&
		b.first.imag() <= a.second.imag();
}

int main()
{
	int T;
	cin >> T;
	REP(t,T)
	{
		int R;
		cin >> R;
		vector<rect> r(R);
		REP(i,R) cin >> r[i].first >> r[i].second;
		REP(i,R) r[i].second = ci(r[i].second.real() + 1, r[i].second.imag() + 1);
		vector<list<int> > g;
		REP(i,R)
		{
			vi b;
			REP(j,g.size())for(list<int>::iterator it = g[j].begin(); it != g[j].end(); ++it)
			{
				if(intersect(r[i], r[*it]))
				{
					b.push_back(j);
					break;
				}
			}
			if(b.empty())
			{
				b.push_back(g.size());
				g.push_back(list<int>());
			}
			FOR(j,1,b.size()) g[b[0]].splice(g[b[0]].end(), g[b[j]]);
			g[b[0]].push_back(i);
		}
		int ans = 0;
		REP(i,g.size())
		{
			int max_x = 0, max_y = 0, min_xy = 1000001;
			for(list<int>::iterator it = g[i].begin(); it != g[i].end(); ++it)
			{
				max_x = max(max_x, r[*it].second.real());
				max_y = max(max_y, r[*it].second.imag());
				min_xy = min(min_xy, r[*it].first.real() + r[*it].first.imag());
			}
			ans = max(ans, max_x + max_y - min_xy - 1);
		}

		printf("Case #%d: %d\n", t + 1, ans);
	}
	
	return 0;
}
