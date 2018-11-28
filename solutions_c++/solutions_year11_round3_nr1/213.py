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
		bool flag = true;
		int h, w;
		cin >> h >> w;
		vector<string> tiles(h);
		for(int y=0; y<h; y++)
		{
			cin >> tiles[y];
		}
		for(int y=0; flag&&y<h; y++)
		{
			for(int x=0; flag&&x<w; x++)
			{
				if(tiles[y][x] == '#')
				{
					if(x+1 == w || y+1 == h)
					{
						flag = false;
					}
					else if(tiles[y][x+1] != '#' || tiles[y+1][x] != '#' || tiles[y+1][x+1] != '#')
					{
						flag = false;
					}
					else
					{
						tiles[y][x] = tiles[y+1][x+1] = '/';
						tiles[y][x+1] = tiles[y+1][x] = '\\';
					}
				}
			}
		}
		cout << "Case #" << i+1 << ":" << endl;
		if(flag)
		{
			for(int y=0; y<h; y++)
			{
				cout << tiles[y] <<endl;
			}
		}
		else
		{
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
