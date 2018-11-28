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

int R, C, D;
int FX[512][512];
int FY[512][512];
int GX[512][512];
int GY[512][512];
char S[512][512];
int M[512][512];
int Sum(int i, int j, int i2, int j2, int FX[][512])
{
    return  FX[i2][j2] - FX[i-1][j2] - FX[i2][j-1] + FX[i-1][j-1];
}
bool Check(int i, int j, int k)
{
     //printf("Check %d %d %d\n", i, j, k);
     int j2 = j+k-1;
     int i2 = i+k-1;
     int v1 = (Sum(i, j, i2, j2, FX)
           - M[i2][j2] * j2 - M[i][j2] * j2 - M[i2][j] * j - M[i][j] * j) * 2;
     int v2 = (Sum(i, j, i2, j2, GX)
              - M[i2][j2] - M[i][j2] - M[i2][j] - M[i][j]) * (j + j2);
    bool f1 =  v1 == v2;
    //printf("%d %d\n",  v1, v2);

    v1 = (Sum(i, j, i2, j2, FY)
           - M[i2][j2] * i2 - M[i][j2] * i - M[i2][j] * i2 - M[i][j] * i) * 2;
    v2 = (Sum(i, j, i2, j2, GY)
              - M[i2][j2] - M[i][j2] - M[i2][j] - M[i][j]) * (i + i2);
    bool f2 = v1  == v2;
    // printf("%d %d\n",  v1, v2);
     
    // printf("N=%d\n", Sum(i, j, i2, j2, GX));
    return f1 && f2;
           
}
int main()
{
    //freopen("B_S0.in", "r", stdin);freopen("B_S0_tmp.out", "w", stdout);
    freopen("B-large.in", "r", stdin);freopen("B-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;
    scanf("%d", &T);
    while(T--)
    {
       scanf("%d%d%d", &R, &C, &D);
       for(i = 1; i <= R; ++i)
       {
           scanf("%s", S[i] + 1);
           for(j = 1; j <= C; ++j)
              M[i][j] = S[i][j] - '0';
       }   
       memset(FX, 0, sizeof(FX));
       memset(GX, 0, sizeof(GX));
       
        memset(FY, 0, sizeof(FY));
       memset(GY, 0, sizeof(GY));
       
       for(i = 1; i <= R; ++i)       
          for(j = 1; j <= C; ++j)
          {
              FX[i][j] = FX[i-1][j] + FX[i][j-1] - FX[i-1][j-1] + M[i][j]* j;
              FY[i][j] = FY[i-1][j] + FY[i][j-1] - FY[i-1][j-1] + M[i][j] * i;
              
              GX[i][j] = GX[i-1][j] + GX[i][j-1] - GX[i-1][j-1] + M[i][j];
              GY[i][j] = GY[i-1][j] + GY[i][j-1] - GY[i-1][j-1] + M[i][j];
          }
       
       int res = 0;
       
       for(i = 1; i <= R; ++i)
           for(j = 1; j <= C; ++j)
               for(k = max(res + 1, 3); k <= min(R - i, C - j) + 1; ++k)
               {
                   if(Check(i, j, k)) res = k;
               }
       //printf("%d\n", Check(2, 2, 5));
       if(res < 3)
       {
              printf("Case #%d: IMPOSSIBLE\n", ++cs);
       }
       else
       {
        printf("Case #%d: %d\n", ++cs, res);
       }
    }
	return 0;
}

