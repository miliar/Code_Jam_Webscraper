
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

double solve(int A,int B, vector<double> v)
{
	double res = 0;
	vector<double> exp(A), mult(A);
	mult[0] = v[0];
	FOR(i,1,A)
	{
		mult[i]= mult[i-1]*(v[i]);
	}


	REP(i,A)
	{
		exp[i] = 2*(A-i-1) + (B-A+1) + (1-mult[i])*(B+1);
	}

	res = *min_element(exp.begin(),exp.end());

	res = min(res, B+2.0);

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
		int A,B;
		cin>>A>>B;
		vector<double> v(A);
		REP(i,A)
			cin>>v[i];

		printf("Case #%d: %0.6f\n",t+1,solve(A,B,v));
	}

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}