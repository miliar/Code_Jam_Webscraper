#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <memory>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
//#define tt (ll+rr)/2
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define rnd() ((rand() << 16) ^ rand())

int main()
{
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout); 
	
	int TC;
	cin >> TC;
	rep(tc, TC)
	{
		int n, d;
		scanf("%d%d", &n, &d);
		vector<pair<ll, ll> > a;
		a.clear();

		rept(i, n)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			a.pb(mp(x, y));
		}
		ll res = 0, pred = -INF;

		rept(i, L(a))
		{
			ll cur = 0;
			if (a[i].x < pred)
			{
				cur += pred - a[i].x;
				pred = pred + a[i].y * d;
			}
			else
			{
				pred = a[i].x + a[i].y * d;
			}
			cur += (a[i].y - 1) * d;
			res = max(cur, res);
		}

		printf("Case #%d: ", tc);
		cout << res / 2 << "." << (res % 2) * 5 << endl;
	}
	
	return 0;
}
