#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(ll i=0; i<n; i++)
#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define RFOR(i, x, y) for(ll i=x; i>=y; i--)
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
#define X first
#define Y second
#define VI vector<short>
const double pi=acos(-1.0);

vector<int> CC;
vector<int> a;
vector<double> speed;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int tests;
	cin>>tests;

	REP(test, tests)
	{

		ll l, t, n, c;
		cin>>l>>t>>n>>c;
		
		CC.resize(c);
		a.resize(n);
		speed.resize(0);
		
		REP(i, c)
			cin>>CC[i];
//			scanf("%lld", &CC[i]);

		REP(i, n)
			a[i] = CC[i%c];


		int first = -1;
		double sum = 0;

		REP(i, n)
		{
			if (sum >= t)
			{
				first = i;
				speed.pb(a[i]);
				break;
			}

			if (t < sum+a[i]*2)
			//if (t + a[i] < sum + a[i]*2)
			{
				first = i;
				//speed.pb(sum+a[i]*2 - t - a[i]);
				double TT = t - sum;
				TT/=2;
				speed.pb(2*a[i] - (t - sum) - (a[i] - TT));
				break;
			}
			
			sum+=2*a[i];
		}
		
		sum = 0;
		REP(i, n)
			sum+=a[i];

		sum*=2;

		FOR(i, first+1, n-1)
			speed.pb(a[i]);

		sort(ALL(speed));
		reverse(ALL(speed));

		ll k = l;
		if (speed.size() < k)
			k = speed.size();

		REP(i, k)
			sum-=speed[i];
		
		ll x = sum;
		printf("Case #%d: ", test+1, sum);	
		cout<<x<<endl;

	}

}

