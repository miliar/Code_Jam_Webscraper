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
		int n;
		cin>>n;
		vector<char> d(n);
		vector<int> v(n);
		REP(i,n)
			cin>>d[i]>>v[i];

		int pos1 = 1; int pos2 =1;
		int time1 = 0; int time2= 0;
		int res =0;
		REP(i,n)
		{
			int add;
			if (d[i]=='O')
			{
				add =  abs(v[i]-pos1) - time1;
				if (add<0) add = 1;	else add++;
				if (add>0) time2 += add;
				time1=0;
				pos1 = v[i];
			}
			else
			{
				add =  abs(v[i]-pos2) - time2;
				if (add<0) add = 1;	else add++;
				if (add>0) time1+=add;
				time2=0;
				pos2 = v[i];
			}
			res+=add;
		}
		printf("Case #%d: %d\n",t+1,res);
	}
}