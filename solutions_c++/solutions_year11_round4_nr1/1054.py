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
#define x first.first
#define y first.second
#define z second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
//#define tt (ll+rr)/2
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define rnd() ((rand() << 16) ^ rand())

bool cmp(pair<pdd, double> a, pair<pdd, double> b)
{
	return a.second < b.second;
}

int main()
{
        #ifndef ONLINE_JUDGE 
        freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout); 
        #endif

		int TC;
		cin >> TC;
		rept(tc, TC)
		{
			double X, slow, fast, mt;
			cin >> X >> slow >> fast >> mt;
			int n;
			cin >> n;
			vector<pair<pdd, double> > v(n), q;
			rept(i, n)
				scanf("%lf%lf%lf", &v[i].x, &v[i].y, &v[i].z);

			v.pb(mp(mp(X, X), 0));

			v.pb(mp(mp(0, 0), 0));
			rept(i, L(v)) v[i].x = min(v[i].x, X), v[i].y = min(v[i].y, X);
			SORT(v);
			
			q = v;

			rept(i, L(v) - 1)
				q.pb(mp(mp(v[i].y, v[i + 1].x), 0));

			v = q;

			sort(all(v), cmp);

			double time = 0.0;
			double cur = 0.0;

			rept(i, L(v))
			{
				double d, ex;
				cur = v[i].x;

				d = v[i].y - cur;
				ex = min(d / (fast + v[i].z), mt);
				time += ex;
				cur += ex * (fast + v[i].z);
				mt -= ex;

				d = v[i].y - cur;
				ex = d / (slow + v[i].z);
				time += ex;
				cur += ex * (slow + v[i].z);
			}

			printf("Case #%d: %.9lf\n", tc + 1, time);
		}

        return 0;
}