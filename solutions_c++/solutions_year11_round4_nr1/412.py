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
               FOR(j,2, (int)ceil(sqrt(i+0.1))) if (i%j==0) {ok=false; break;}
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
const char *out_file = "output_a_easy.txt";

bool ss(vector<int> a , vector<int> b)
{
	return a[1]<b[1];
}

int main()
{
        freopen(in_file, "r", stdin);
        freopen(out_file, "w", stdout);
		int T , n;
		cin>>T;
		REP(t,T)
		{
			cout<<"Case #"<<t+1<<": ";
			int X, S ,R , N;
			double time;
			cin>>X>>S>>R>>time>>N;
			vector<vector<int> > v(N+1, vector<int>(2));
			REP(i,N)
			{
				int a,b;
				cin>>a>>b>>v[i][0];
				v[i][1]= b-a;
				v[i][0]+=S;
				X -= v[i][1];
			}
			v[N][1] = X;
			v[N][0] = S;
			R -=S;
			
			double res = 0 ;
			SORT(v);
			REP(i,N+1)
			{
				double c = ((double)v[i][1])/(R+v[i][0]);
				if (c>time)
					c = time;
				time -=c;
				res+= c;
				//cout<<i<<" res:"<<res<<" c: "<<c<<endl;
				res +=  (double)(v[i][1] - c*(R+v[i][0]))/(v[i][0]);
			}

			printf ("%.6lf\n", res);


		}
		return 0;
}
