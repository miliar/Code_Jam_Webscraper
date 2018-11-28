#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
typedef long long LL;
const LL MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))
#define eps 1e-9
#define eps2 1e-15
template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void CMAX(T &a,T b){if(b>a) a=b;} 
template<class T> inline void CMIN(T &a,T b){if(b<a) a=b;}

#define FOR(a,b,c) for(a=b;a<c;++a)
#define REP(a,b) for(a=0;a<b;++a)

int W, L, U, G;
int lx[128], ly[128];
int ux[128], uy[128];
double GetArea(double e)
{
	int i;
	double res = e * 2000;	
	double dx;
	//DB(res);
	for(i = 1; lx[i] < e - eps; ++i)
	{
		dx = (lx[i] - lx[i-1]);

		res -= (ly[i-1] + 1000 + ly[i] + 1000) / 2.0 * dx;
		//printf("%.6lf %.2lf\n", dx, (ly[i-1] + 1000 + ly[i] + 1000) / 2.0 * dx);
		//DB(res);
		//res -= (1000 - uy[i-1] + 1000 - uy[i]) / 2.0 * dx;
	}

	dx = e - lx[i-1];
	
	double lyi = (ly[i] - ly[i-1]) * 1.0 / (lx[i] - lx[i-1]) * dx + ly[i-1];

	res -= (ly[i-1] + 1000 + lyi + 1000) / 2.0 * dx;
	
	//printf("%.6lf %.6lf  %.6lf %.2lf\n",  ly[i-1]*1.0,lyi*1.0, dx, (ly[i-1] + 1000 + lyi + 1000) / 2.0 * dx);
	
	for(i = 1; ux[i] < e - eps; ++i)
	{
		dx = (ux[i] - ux[i-1]);

		//res -= (ly[i-1] + 1000 + ly[i] + 1000) / 2.0 * dx;

		res -= (1000 - uy[i-1] + 1000 - uy[i]) / 2.0 * dx;
		//printf("%.6lf %.2lf\n", dx, (1000 - uy[i-1] + 1000 - uy[i]) / 2.0 * dx);

		//DB(res);
	}

	dx = e - ux[i-1];

	double uyi = (uy[i] - uy[i-1]) * 1.0 / (ux[i] - ux[i-1]) * dx + uy[i-1];

	res -= (1000 - uy[i-1] + 1000 - uyi) / 2.0 * dx;

	return res;
}
double GetX(double a)
{
	double l, r, m;
	l = 0, r = W;
	while(r - l > eps)
	{
		m = (r + l) / 2;

		double tmp = GetArea(m);

		if(tmp > a + eps2)
		{
			r = m;
		}
		else if(tmp < a - eps2)
		{
			l = m;
		}
		else return m;
	}
	return m;
}
int main()
{
    //freopen("A_S0.in", "r", stdin);freopen("A_S0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;

    scanf("%d", &T);
    while(T--)
    {
       scanf("%d%d%d%d", &W, &L, &U, &G);
		REP(i, L)
			scanf("%d%d", &lx[i], &ly[i]);
		REP(i, U)
			scanf("%d%d", &ux[i], &uy[i]);

	   double tota = GetArea(W);

	   
	//printf("%.6lf\n", tota);
	//continue;
       printf("Case #%d:\n", ++cs);
	   REP(i, G-1)
		   printf("%.6lf\n", GetX( tota / G * (i+1)));
    }
	return 0;
}

