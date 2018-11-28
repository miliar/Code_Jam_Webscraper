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
typedef long long ll;
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
		int x, s, r, t, N;
		cin >> x >> s >> r >> t >> N;
		vector< pair<int, pair<int, int> > > data;
		int c = 0;
		for(int j=0; j<N; j++)
		{
			int b, e, w;
			cin >> b >> e >> w;
			if(c < b)
			{
				data.push_back(make_pair(0, make_pair(c, b)));
				c = b;
			}
			data.push_back(make_pair(w, make_pair(b, e)));
			c = e;
		}
		if(c != x)
		{
			data.push_back(make_pair(0, make_pair(c, x)));
		}
		sort(data.begin(), data.end());
		double ret = 0;
		double tleft = t;
		for(int j=0; j<data.size(); j++)
		{
			//cout << data[j].second.first << " - " << data[j].second.second << endl;
			double dist = data[j].second.second - data[j].second.first;
			double runtime = min(dist/(r+data[j].first), tleft);
			//cout << ret << endl;
			ret += runtime;
			//cout << ret << endl;
			tleft -= runtime;
			if(tleft < 0)tleft = 0;
			double runtime2 = dist/(r+data[j].first) - runtime;
			if(1e-10 < runtime2)
			{
				ret += (dist - runtime*(r+data[j].first))/(s+data[j].first);
			}
			//cout << ret << endl;
		}
		cout << "Case #" << i+1 << ": ";
		printf("%.10lf\n", ret);
	}
	return 0;
}
