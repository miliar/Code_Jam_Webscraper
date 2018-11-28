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
		int m;
		cin >> m;
		vector< pair<int, int> > O_proc;
		vector< pair<int, int> > B_proc;
		for(int j=0; j<m; j++)
		{
			int b;
			char t;
			cin >> t >> b;
			if(t == 'O')
			{
				O_proc.push_back(make_pair(j, b));
			}
			else
			{
				B_proc.push_back(make_pair(j, b));
			}
		}
		int O_pos = 1;
		int B_pos = 1;
		int step = 0;
		while(!O_proc.empty() || !B_proc.empty())
		{
			if(O_proc.empty())
			{
				int tmp = B_proc[0].second;
				B_proc.erase(B_proc.begin());
				step += abs(B_pos-tmp)+1;
				B_pos = tmp;
			}
			else if(B_proc.empty())
			{
				int tmp = O_proc[0].second;
				O_proc.erase(O_proc.begin());
				step += abs(O_pos-tmp)+1;
				O_pos = tmp;
			}
			else
			{
				if(B_proc[0].first < O_proc[0].first)
				{
					int tmp = B_proc[0].second;
					B_proc.erase(B_proc.begin());
					int d = abs(B_pos-tmp)+1;
					step += d;
					B_pos = tmp;
					O_pos = O_proc[0].second+max(0, abs(O_pos-O_proc[0].second)-d);
				}
				else
				{
					int tmp = O_proc[0].second;
					O_proc.erase(O_proc.begin());
					int d = abs(O_pos-tmp)+1;
					step += d;
					O_pos = tmp;
					B_pos = B_proc[0].second+max(0, abs(B_pos-B_proc[0].second)-d);
				}
			}
		}
		cout << "Case #" << i+1 << ": " << step << endl;
	}
	return 0;
}
