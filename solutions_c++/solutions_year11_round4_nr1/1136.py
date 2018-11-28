#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <cassert>
#include <math.h>
#include <vector>
#include <time.h>
#include <set>
#include <queue>
#define REP(i,n) for(int i=0, _n=(n); i<_n; i++)
#define REPD(i,n) for(int i=n-1; i>=0; i--)
#define FOR(i,a,b) for(int i=a,_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=a,_b=(b); i>=_b; i--)
#define FILL(x, v) memset(&x,v,sizeof(x))
#define DB(vari) cout<<#vari<<" = "<<vari<<endl;
#define x first
#define y second
#define mp make_pair
#define pb push_back

using namespace std;

typedef pair<int, int> pii;
typedef long long LL;

const int maxn = 100000;
const int MAXC = 1;

int x, t, s, r, n, w[maxn], b[maxn], e[maxn];
double ans;
pair<int, pii> segm[maxn];

int main()
{
	freopen("input.txt","r", stdin); freopen("output.txt","w", stdout);
	scanf("%d", &t);
	REP(i, t)
	{
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		ans = 0;
		REP(j, n)
		{
			scanf("%d%d%d", &segm[j].y.x, &segm[j].y.y, &segm[j].x);
			x -= segm[j].y.y - segm[j].y.x;
		}
		sort(segm, segm + n);
		double tt = t;
		double tr = x / double(r);
		if (tt > tr)
		{
			tt -= tr;
			ans += tr;
		}
		else
		{
			ans += tt + (x - tt*r) / double(s);
			tt = 0;
		}
		//DB(ans);
		//DB(x);
		REP(j, n)
		{
			int slen = segm[j].y.y - segm[j].y.x;
			//DB(segm[j].y.y);
			//DB(slen);
			tr = slen / double(r + segm[j].x);
			if (tt > tr)
			{
				tt -= tr;
				ans += tr;
			}
			else
			{
				ans += tt + (slen - tt*(r + segm[j].x)) / double(s + segm[j].x);
				tt = 0;
			}
		}
		printf("Case #%d: %.9lf\n", i+1, ans);
	}
	return 0;
}
