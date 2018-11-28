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


vector<ll> a;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int test;
	cin>>test;

	REP(t, test)
	{
		int n;
		cin>>n;
		a.resize(n);
		REP(i, n)
			cin>>a[i];

		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());

		ll sum, cnt;
		sum = a[0];
		cnt = a[0];
		FOR(i, 1, n-2)
		{
			sum+=a[i];
			cnt = cnt ^ a[i];
		}
		
		if (cnt == a[n-1])
		{
			printf("Case #%d: ", t+1);
				cout<<sum<<endl;
		}
		else printf("Case #%d: NO\n", t+1);
	}
}