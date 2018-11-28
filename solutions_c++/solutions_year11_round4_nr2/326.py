#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
const int N = 510 ;
const int M = 100005 ;
typedef __int64 ll ;
int n , m ;
const double eps = 1e-8;

int kdc[N][N];
char str[1005];
double dp1[N][N], dp2[N][N], t1[N][N], t2[N][N];
ll sum[N][N];
//bool vst[100005] ;

int fun()
{
	int ans = -1, limit ;
	int i, j, k ;
	bool ok = true ;
     for ( limit = min(n,m), k=limit; k>=3; k--) 
	 {
         ok = false;
         for (int i = 0; i + k <= n && !ok; i++)
		 {
             for(int j = 0; j+k<= m ; j++)
			 {
                     double cx = (2*i+k)/2.0, cy = (2*j+k)/2.0;
                     double xx = dp1[i+k][j+k] - dp1[i][j+k] - dp1[i+k][j] + dp1[i][j] 
                     - t1[i+1][j+1] - t1[i+k][j+1] - t1[i+1][j+k] - t1[i+k][j+k];
                     double yy = dp2[i+k][j+k] - dp2[i][j+k] - dp2[i+k][j] + dp2[i][j] 
                     - t2[i+1][j+1] - t2[i+k][j+1] - t2[i+1][j+k] - t2[i+k][j+k];
                     double sm = sum[i+k][j+k] - sum[i][j+k] - sum[i+k][j] + sum[i][j] 
                     - kdc[i+1][j+1] - kdc[i+k][j+1] - kdc[i+1][j+k] - kdc[i+k][j+k];
                     cx *= sm;
                     cy *= sm;
                     if (fabs(cx - xx) < eps && fabs(cy-yy) < eps ){
                                 ok = true;
                                 break;
                        }
             }
         }

         if(ok){
                ans = k;
                break;       
         }
     }
	return ans ;
}

int main()
{
	int t, i, j, k, Q, x , y, cas = 1 ;
	bool flag , ok = true ;
	double x1, x2, y1, y2, tmp, ans = 0 ;
	int R,C,D;

	//freopen("D:\\A-large.in","r",stdin ) ;
	//freopen("D:\\out.txt","w",stdout ) ;

	scanf("%d",&t ) ;
	while ( t-- )
	{
		printf("Case #%d: ",cas++ ) ;
		x1 = x2 = y1 = y2 = 0 ;
		scanf("%d%d%d", &R, &C, &D);
		memset(sum, 0, sizeof sum);
		memset(dp1, 0, sizeof dp1);
		memset(dp2, 0, sizeof dp2);
		for (int i = 1; i <= R; i++)
		{
			scanf("%s", &str[1] );             
			for (int j = 1; j <= C; j++){             
                  kdc[i][j] = D + str[j] - '0';
                  sum[i][j] = sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1] + kdc[i][j];
                  t1[i][j] = (i-0.5)*kdc[i][j];
                  t2[i][j] = (j-0.5)*kdc[i][j];
                  dp1[i][j] = dp1[i][j-1] + dp1[i-1][j] - dp1[i-1][j-1] + t1[i][j];
                  dp2[i][j] = dp2[i][j-1] + dp2[i-1][j] - dp2[i-1][j-1] + t2[i][j];
             }
     }
     int ans = -1;
     for (int limit = min(R,C), k=limit; k>=3; k--) 
	 {
         ok = false;
         for (int i = 0; i + k <= R && !ok; i++)
		 {
             for(int j = 0; j+k<= C;j++)
			 {
                     double x1 = (2*i+k)/2.0, y1 = (2*j+k)/2.0;
                     double xx = dp1[i+k][j+k] - dp1[i][j+k] - dp1[i+k][j] + dp1[i][j] - t1[i+1][j+1] - t1[i+k][j+1] - t1[i+1][j+k] - t1[i+k][j+k];
                     double yy = dp2[i+k][j+k] - dp2[i][j+k] - dp2[i+k][j] + dp2[i][j] - t2[i+1][j+1] - t2[i+k][j+1] - t2[i+1][j+k] - t2[i+k][j+k];
                     double tmp = sum[i+k][j+k] - sum[i][j+k] - sum[i+k][j] + sum[i][j] - kdc[i+1][j+1] - kdc[i+k][j+1] - kdc[i+1][j+k] - kdc[i+k][j+k];
                     x1 *= tmp, y1 *= tmp ;
                     if (fabs( x1 - xx) < eps && fabs( y1 -yy) < eps ){
                                 ok = true;
                                 break;
                        }
             }
         }
         if(ok){
                ans = k;
                break;       
         }
     }
     if(ans != -1){
            printf("%d\n", ans);
     } else {
            puts("IMPOSSIBLE");
     }
 }
	return 0 ;
}