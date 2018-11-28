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

char G[128][128];
int N;
double WP[128], OWP[128], OOWP[128];
double res[128];
double GetWP(int i, int k) // i's WP against k
{
    int a = 0, b = 0;
    int j;
   for(j = 0; j < N; ++j) if(j != k)
   {
       if(G[i][j] != '.') ++b;
       if(G[i][j] == '1') ++a;
   }
   return a * 1.0 / b;    
}
void Solve()
{
     int i, j, k;
     for(i = 0; i < N; ++i)
     {
           
         WP[i] = GetWP(i, -1); 
     }
     for(i = 0; i < N; ++i)
     {
         int tot = 0;
         double sum = 0;
         for(j = 0; j < N; ++j) if(G[i][j] != '.')
         {
             double t = GetWP(j, i);
             tot++;
             sum += t;
         }
         OWP[i] = sum / tot;
     }
     for(i = 0; i < N; ++i)
     {
         int tot = 0;
         double sum = 0;
         for(j = 0; j < N; ++j) if(G[i][j] != '.')
         {
             tot++;
             sum += OWP[j];
         }
         OOWP[i] = sum / tot;
     }
     for(i = 0; i < N; ++i)
     {
           res[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
     }
}
int main()
{
    //freopen("A_S.in", "r", stdin);freopen("A_S.out", "w", stdout);
    freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &N);
        for(i = 0; i < N; ++i)
            scanf("%s", G[i]);
        Solve();
        printf("Case #%d:\n", ++cs);
        for(i = 0; i < N; ++i)
            printf("%.12lf\n", res[i]);
    }
	return 0;
}

