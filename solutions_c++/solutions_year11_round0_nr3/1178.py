#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>

using namespace std;

const double EPS = 1e-9;
const long LONGMAX = numeric_limits<long>::max();
const long INTMAX = numeric_limits<int>::max();

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())



const char *in_file = "input.txt";
const char *out_file = "output.txt";

void main()
{
	freopen(in_file, "r", stdin);
	freopen(out_file, "w", stdout);
	int T;
	cin>>T;
	REP(t,T)
	{
		cout<<"Case #"<<t+1<<": ";
		int n;
		cin>>n;
		vector<int> v(n);
		REP(i,n) cin>>v[i];
		int res = v[0];
		FOR(i,1,n)
			res ^= v[i];
		if (res == 0)
		{
			SORT(v);
			int sum =0;
			FOR(i,1,n)
				sum+=v[i];
			cout<<sum<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}
}