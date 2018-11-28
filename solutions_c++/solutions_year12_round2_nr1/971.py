
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
#include<ctime>

using namespace std;

const double EPS = 1e-9;
//const long long  INF = 1000000000000000000;

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


       // int N;
       // cin >> N;

       // VI s(N);
       // rep(i,N) cin >> s[i];

       // vector<double> p(N);
       // rep(i,N) p[i] = 1.0*s[i] / 100;

       // double x = 0;
       // rep(i,N) x += p[i];

       ////cout << "x: " << x << endl;

       // printf("Case #%d: ", cs+1);
       // rep(i,N) printf("%f ", 100*(2.0/N - p[i]/x)); printf("\n");


vector<double> solve(vector<int> v)
{
	int n = v.size();
	double X =0,left;
	vector<double> res(n,-1);

	REP(i,n) X+=v[i];
	left = X;

	int T = n;

	while(true)
	{
		bool ok = false;
		REP(i,n)
		{
			if (res[i]!=-1) continue;
			if ((X+left)/(X*T) - v[i]/X<0 || fabs((X+left)/(X*T) - v[i]/X)<EPS)
			{
				res[i]=0;
				T--;
				left-=v[i];
				ok = true;
				break;
			}
		}
		if (!ok) break;
	}

	REP(i,n)
	{
		if (res[i]==-1)
			res[i]= 100*((X+left)/(X*T) - v[i]/X);
	}

	return res;
}

int main()
{
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output_a_hard.txt","w",stdout);
#endif

	int T;
	cin>>T;

	REP(t,T)
	{
		int n;
		cin>>n;
		vector<int> v(n);
		REP(i,n)
			cin>>v[i];
		vector<double> res = solve(v);

		printf("Case #%d: ",t+1);
		REP(i,n)
		{
			if (i) cout<<" ";
			printf("%0.6f",res[i]);
		}
		printf("\n");
	}

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}