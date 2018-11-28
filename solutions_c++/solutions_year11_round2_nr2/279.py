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

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void CMAX(T &a,T b){if(b>a) a=b;} 
template<class T> inline void CMIN(T &a,T b){if(b<a) a=b;}

#define MAX(a, b) ((a)>(b)?(a):(b))

int D, C;
int P[256], V[256];
LL len[256];
LL sv;
bool Check(LL t)
{
    LL r = -(1LL << 50);
    
    int i;
    for(i = 0; i < C; ++i)
    {
          //printf("i=%d, r=%lld\n", i, r/2);
        if(len[i] > t) 
        {//printf("AAA %lld %lld\n", len[i], r/2);
                  return 0;
        }
        r = MAX(r + len[i] * 2, 2 * P[i] - t + len[i] * 2);
         //printf("len2 = %lld, r2= %lld\n", len[i], r/2);
        if(r - P[i] * 2 > t) 
        {
             //printf("BBB r2= %lld, %lld, %d, %lld\n", r/2, r, P[i]*2.);
             return 0;
             }
        r += D  * 2;
    }
    return 1;
}
LL Solve()
{
    LL l = -1, h = sv * D * 10;
    
    while(l < h - 1)
    {
        LL m = (h + l) / 2;
        //printf("m=%lld, res=%d\n", m, Check(m));
        if(Check(m)) h = m;
        else l = m;
    }
    return h;
}
int main()
{
    //freopen("B_S2.in", "r", stdin);freopen("B_S2.out", "w", stdout);
freopen("B-large.in", "r", stdin);freopen("B-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;
    scanf("%d", &T);
    while(T--)
    {
              sv = 0;
        scanf("%d%d", &C, &D);
        for(i = 0; i < C; ++i)
        {
            scanf("%d%d", &P[i], &V[i]);
            sv += V[i];
            len[i] = ((LL)(V[i] - 1) ) * D;
        }
        
        LL res = Solve();
        printf("Case #%d: ", ++cs);
        if(res & 1) printf("%lld.5\n", res / 2);
        else printf("%lld.0\n", res / 2);
    }
	return 0;
}
/*
10

3 2
0 1
3 2
6 1

2 2
0 3
1 1

1 1
0 1

1 1
0 2

1 1
0 1000000

2 1
-1 100
1 100
*/
