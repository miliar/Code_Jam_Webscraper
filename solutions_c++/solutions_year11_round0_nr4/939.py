#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <set>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(int i=0; i<n; i++)
#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define RFOR(i, x, y) for(ll i=x; i>=y; i--)
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
const double pi=acos(-1.0);

double p(double iter)
{
	if (iter == 100)
		return iter/24 + (iter+2)/4 + (iter+3)/3;

	return iter/24 + (iter+2)/4 + (iter+3)/3 + p(iter+1)*9.0/24.0;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);


	int test;
	cin>>test;

	REP(t, test)
	{
		int n;
		cin>>n;
		vector<int> a(n);

		REP(i, n)
		{
			cin>>a[i];
			a[i]--;
		}

		int cnt = 0;
		REP(i, n)
			if (i != a[i])
				++cnt;

		printf("Case #%d: %d.000000\n", t+1, cnt);
	}	
}