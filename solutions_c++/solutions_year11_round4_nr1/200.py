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
typedef long long int64;
const int64 MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void CMAX(T &a,T b){if(b>a) a=b;} 
template<class T> inline void CMIN(T &a,T b){if(b<a) a=b;}

int X, S, R, t, N;
struct WW
{
    int S, E, W, L;
}w[1024];
bool operator<(const WW& a, const WW& b)
{
     return a.W < b.W;
}
int main()
{
    //freopen("A_S0.in", "r", stdin);freopen("A_S0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;
    int tot;
    scanf("%d", &T);
    while(T--)
    {
       scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
       tot = X;
       for(i = 0; i < N; ++i)
       {
           scanf("%d%d%d", &w[i].S, &w[i].E, &w[i].W);
           w[i].L = w[i].E - w[i].S;
           tot -= w[i].L;
       }
       w[N].L = tot;
       w[N].W = 0;
       N++;
       sort(w, w + N);
       
       double res = 0;
       double rest = t;
       for(i = 0; i < N; ++i)
       {
           double tt = w[i].L * 1.0 / (R + w[i].W);
           
           tt = min(tt, rest);
           
           
           
           res += tt + (w[i].L - tt * (R + w[i].W)) * 1.0 / (S + w[i].W);
           
           rest -= tt;
           
       }
       
       printf("Case #%d: %.6lf\n", ++cs, res);
    }
	return 0;
}

