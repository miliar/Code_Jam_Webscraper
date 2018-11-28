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
const long long  INF = 1000000000000000000;

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())



const char *in_file = "input.txt";
const char *out_file = "output_a.txt";

int n,m;

int main()
{
        freopen(in_file, "r", stdin);
        freopen(out_file, "w", stdout);
		int T;
		cin>>T;
		REP(t,T)
		{
			cout<<"Case #"<<t+1<<": ";
			long long n , pd, pg;
			cin>>n>>pd>>pg;
			if (pg == 0)
			{
				if (pd == 0)
					cout<<"Possible"<<endl;
				else
					cout<<"Broken"<<endl;
				continue;
			}

			if (pg == 100)
			{
				if (pd == 100)
					cout<<"Possible"<<endl;
				else
					cout<<"Broken"<<endl;
				continue;
			}

			if (n>=100)
				cout<<"Possible"<<endl;
			else
			{
				bool ok = false;
				for(int i=1; i<=n;++i)
				{
					int tmp1  = (i*pd)/100;
					int tmp2 = (i*(100-pd))/100;
					if ( tmp1+tmp2 == i)
					{
						double f = i*(pd/100.0)+0.0;
						//cout<<"Test"<<tmp1<<" "<<f<<endl;
						ok = true;
						break;
					}
				}
				if (ok)
					cout<<"Possible"<<endl;
				else
					cout<<"Broken"<<endl;
			}
		}
}
