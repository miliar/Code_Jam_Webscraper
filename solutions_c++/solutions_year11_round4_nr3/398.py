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
#define ll long long

vector<int> getPrimes(int n)
{
       vector<int> res;
       FOR(i,2,n)
       {
               bool ok = true;
               FOR(j,2, (int)floor(sqrt(i+0.1))+1)
				   if (i%j==0) {ok=false; break;}
               if (ok) res.push_back(i);
       }
       return res;
}

int gcd (int a, int b) {
	return b ? gcd (b, a % b) : a;
}

int isPrime(int a) {
    int end = (int)sqrt((double)a);
    for (int i = 2; i <= int(end+1E-9); i++)
        if (a % i == 0)
           return false;
    return true;
}


const char *in_file = "input.txt";
const char *out_file = "output_c_easy.txt";

int main()
{
        freopen(in_file, "r", stdin);
       freopen(out_file, "w", stdout);
		vector<int> pr = getPrimes(1000000);
		int T;
		cin>>T;
		REP(t,T)
		{
			cout<<"Case #"<<t+1<<": ";
			ll n;
			cin>>n;
			int res = 0;
			REP(i,pr.size())
			{
				ll k = pr[i];
				int num = 0;
				while(k<=n/pr[i])
				{
					num++;
					k*=pr[i];
				}
				
				res += num;
			}
			if (n>1) res ++;
			cout<<res<<endl;

		}
		return 0;
}
