#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <limits>
#include <iomanip>
#include <iterator>
#include <complex>
using namespace std;

#define FOR(i,a,b) for(int __n(b), i(a); i<__n; ++i)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),__b(b); i>=__b;--i)
#define ALL(c) (c).begin(), (c).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define SORT(c) sort(ALL(c))
#define X first
#define Y second
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define DBG(a) cout << #a" = " << (a) << endl
#define DBGA(c) copy(ALL(c), ostream_iterator<typeof(*c.begin())>(cout, "\n"))
#define CLR(a) memset((a), 0 ,sizeof(a))
const double PI  = acos(-1.0);
static const double EPS = 1e-5;
typedef long long LL;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
template<class T> inline T sqr(T x) {return x*x;}
template<typename T, typename U> T lexical_cast(const U& src)
{
	T tmp;
	stringstream ss;
	ss << src;
	ss >> tmp;
	return tmp;
}

int main()
{
	int n;
	cin >> n;
	for(int i=0; i<n; i++)
	{
		ull nbst, bsttime, N, C, ret = 0;
		ull disttime = 0;
		cin >> nbst >> bsttime >> N >> C;
		vector< pair<ull,ull> > dist(C);
		REP(j,C)
		{
			cin >> dist[j].first;
			dist[j].second = N/C;
			disttime += dist[j].first*2;
		}
		REP(j,N%C)
		{
			dist[j].second++;
		}
		ull nmuri = bsttime/disttime;
		if(nmuri)
		{
			REP(j,C)
			{
				ull tmp = min(nmuri, dist[j].second);
				dist[j].second -= tmp;
				ret += dist[j].first * tmp * 2;
			}
		}
		nmuri = bsttime%disttime;
		REP(j,C)
		{
			if(dist[j].first*2 < nmuri)
			{
				ull tmp = min(1ull, dist[j].second);
				dist[j].second -= tmp;
				ret += dist[j].first * tmp * 2;
				nmuri -= dist[j].first*2;
			}
			else
			{
				if(dist[j].second)
				{
					dist[j].second--;
					ret += nmuri;
					if(dist[j].first*2-nmuri)
					{
						//cout << dist[j].first*2-nmuri << endl;
						dist.push_back(make_pair((dist[j].first*2-nmuri)/2, 1));
						C++;
					}
				}
				break;
			}
		}
		sort(dist.rbegin(), dist.rend());
		REP(j,C)
		{
			if(nbst)
			{
				ull tmp = min(nbst, dist[j].second);
				ret += dist[j].first*tmp;
				dist[j].second -= tmp;
				nbst -= tmp;
			}
			ret += dist[j].first * dist[j].second * 2;
		}
		cout << "Case #" << i+1 << ": " << ret << endl;
	}
	return 0;
}
