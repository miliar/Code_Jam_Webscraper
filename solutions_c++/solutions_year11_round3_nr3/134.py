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


int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int tests;
	cin>>tests;
	REP(test, tests)
	{
		int n, l, h;
		cin>>n>>l>>h;
		vector<int> a(n);
		REP(i, n)
			cin>>a[i];

		int sol = -1;
		FOR(cur, l, h)
		{
			bool ok = true;
			REP(i, n)
				if (cur%a[i] && a[i]%cur)
				{
					ok = false;
					break;
				}

			if (ok)
			{
				sol = cur;
				break;
			}
		}

		printf("Case #%d: ", test+1);
		if (sol == -1)
			cout<<"NO\n";
		else cout<<sol<<endl;
	}

}

