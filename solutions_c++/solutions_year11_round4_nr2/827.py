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
		int h, w, d;
		cin >> h >> w >> d;
		vector< vector<ull> > data(w, vector<ull>(h, d));
		for(int y=0; y<h; y++)
		{
			string str;
			cin >> str;
			for(int x=0; x<w; x++)
			{
				data[x][y] += str[x]-'0';
			}
		}
		vector< vector<ull> > table(w+1, vector<ull>(h+1, 0));
		for(int y=1; y<=h; y++)
		{
			for(int x=1; x<=w; x++)
			{
				table[x][y] = table[x][y-1] + table[x-1][y] - table[x-1][y-1] + data[x-1][y-1];
			}
		}

		ull ret = 0;
		for(ull k = min(w, h); k>=3; k--)
		{
			for(int y=0; y+k<=h; y++)
			{
				for(int x=0; x+k<=w; x++)
				{
					ull up = 0, down = 0, left = 0, right = 0;
					ull N = k/2;
					for(ull j=1; j<=N; j++)
					{
						int Y = y+k/2-j;
						if(k%2)
							up += j*(table[x+k][Y+1]-table[x+k][Y]-table[x][Y+1]+table[x][Y]);
						else
							up += (2*j-1)*(table[x+k][Y+1]-table[x+k][Y]-table[x][Y+1]+table[x][Y]);
					}
					for(ull j=1; j<=N; j++)
					{
						int Y = y+k/2+j - !(k%2);
						if(k%2)
							down += j*(table[x+k][Y+1]-table[x+k][Y]-table[x][Y+1]+table[x][Y]);
						else
							down += (2*j-1)*(table[x+k][Y+1]-table[x+k][Y]-table[x][Y+1]+table[x][Y]);
					}
					for(ull j=1; j<=N; j++)
					{
						int X = x+k/2-j;
						if(k%2)
							left += j*(table[X+1][y+k]-table[X][y+k]-table[X+1][y]+table[X][y]);
						else
							left += (2*j-1)*(table[X+1][y+k]-table[X][y+k]-table[X+1][y]+table[X][y]);
					}
					for(ull j=1; j<=N; j++)
					{
						int X = x+k/2+j - !(k%2);
						if(k%2)
							right += j*(table[X+1][y+k]-table[X][y+k]-table[X+1][y]+table[X][y]);
						else
							right += (2*j-1)*(table[X+1][y+k]-table[X][y+k]-table[X+1][y]+table[X][y]);
					}
					if(k%2)
					{
						up -= (data[x][y] + data[x+k-1][y])*N;
						down -= (data[x][y+k-1] + data[x+k-1][y+k-1])*N;
						left -= (data[x][y] + data[x][y+k-1])*N;
						right -= (data[x+k-1][y] + data[x+k-1][y+k-1])*N;
					}
					else
					{
						up -= (data[x][y] + data[x+k-1][y])*(N*2-1);
						down -= (data[x][y+k-1] + data[x+k-1][y+k-1])*(N*2-1);
						left -= (data[x][y] + data[x][y+k-1])*(N*2-1);
						right -= (data[x+k-1][y] + data[x+k-1][y+k-1])*(N*2-1);
					}
					//cout << k << ": " << up << " == " << down << ", " << left << " == " << right << endl;
					if(up == down && left == right)
					{
						ret = k;
						goto next;
					}
				}
			}
		}
		next:
		if(ret)
		{
			cout << "Case #" << i+1 << ": " << ret << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
