#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(int i=0; i<n; i++)
#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define RFOR(i, x, y) for(ll i=x; i>=y; i--)
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
const double pi=acos(-1.0);


vector<double> a;

int main()
{	

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	

	int tests;
	cin>>tests;
	

	REP(test, tests)
	{
		int X, N, b, e, w;
		double t, S, R;

		cin>>X>>S>>R>>t>>N;
		
		a.resize(X);
		REP(i, X)
			a[i] = S;

		REP(i, N)
		{
			cin>>b>>e>>w;
			FOR(i, b, e-1)
				a[i]+=w;
		}
		
		sort(ALL(a));

		
		double sol = 0;

		if (R > S)
		REP(i, X)
		{
			if (t == 0)
			{
				sol += 1.0 / a[i];
				continue;
			}

			if (1.0/double(a[i] + (R - S)) <= t)
			{
				t-=1.0/double(a[i] + (R - S));
				a[i]+=(R - S);
				sol+=1.0 / (a[i]);
			}

			else

			{
				double x1;
				x1 = t * (a[i] + (R-S));
				sol+=t;
				t = 0;
				sol+=(1.0 - x1)/a[i];
			}			
		}	

		printf("Case #%d: %.8lf\n", test+1, sol);
	}
	//system("PAUSE");
}