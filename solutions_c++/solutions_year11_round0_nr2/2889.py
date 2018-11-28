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
		int f;
		string combine = "   ";
		string opposed = "  ";
		string str;
		cin >> f;
		if(f)cin >> combine;
		cin >> f;
		if(f)cin >> opposed;
		cin >> f >> str;
		vector<int> o0;
		vector<int> o1;
		for(int j=0; j<str.size(); j++)
		{
			if(j)
			{
				if((str[j-1]==combine[0] && str[j]==combine[1])||(str[j-1]==combine[1] && str[j]==combine[0]))
				{
					if(str[j-1] == opposed[0])o0.pop_back();
					if(str[j-1] == opposed[1])o1.pop_back();
					str[j-1] = '-';
					str[j] = combine[2];
				}
			}
			if(str[j] == opposed[0])
			{
				if(!o1.empty())
				{
					for(int k=0; k<=j; k++)
					{
						str[k] = '-';
					}
					o0.clear();
					o1.clear();
				}
				else
				{
					o0.push_back(j);
				}
			}
			if(str[j] == opposed[1])
			{
				if(!o0.empty())
				{
					for(int k=0; k<=j; k++)
					{
						str[k] = '-';
					}
					o0.clear();
					o1.clear();
				}
				else
				{
					o1.push_back(j);
				}
			}
			//cout << str << endl;
		}
		cout << "Case #" << i+1 << ": [";
		int cnt = 0;
		for(int j=0; j<str.size(); j++)
		{
			if(str[j] != '-')
			{
				if(cnt++)cout << ", ";
				cout << str[j];
			}
		}
		cout << "]" << endl;
	}
	return 0;
}
