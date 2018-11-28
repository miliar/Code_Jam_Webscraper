#include<cstdio>
#include<cstring>
#include<queue>
#include<set>
#include<bitset>
#include<map>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<string>
#include<iostream>


using namespace std;

const double EPS = 1e-8;

int field[505][505];
char str[600];
double X[505][505], Y[505][505];
double fx[505][505], fy[505][505];
long long sum[505][505];

int main()
{
    
//freopen("d:\\in.txt", "r", stdin);
//freopen("d:\\out.txt", "w", stdout);
 
 int T, t = 1;
 for (scanf("%d", &T); T--; )
 {
     printf("Case #%d: ",t++);
     int R,C,D;
     scanf("%d%d%d", &R, &C, &D);
     memset(sum, 0, sizeof sum);
     memset(X, 0, sizeof X);
     memset(Y, 0, sizeof Y);
     for (int i = 1; i <= R; i++){
         scanf("%s",str+1);             
         for (int j = 1; j <= C; j++){             
                  field[i][j] = D + str[j] - '0';
                  sum[i][j] = sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1] + field[i][j];
                  fx[i][j] = (i-0.5)*field[i][j];
                  fy[i][j] = (j-0.5)*field[i][j];
                  X[i][j] = X[i][j-1] + X[i-1][j] - X[i-1][j-1] + fx[i][j];
                  Y[i][j] = Y[i][j-1] + Y[i-1][j] - Y[i-1][j-1] + fy[i][j];
             }
     }
     int ans = -1;
     for (int limit = min(R,C), k=limit; k>=3; k--) {
         bool ok = false;
         for (int i = 0; i + k <= R && !ok; i++){
             for(int j = 0; j+k<= C;j++){
                     double cx = (2*i+k)/2.0, cy = (2*j+k)/2.0;
                     double xx = X[i+k][j+k] - X[i][j+k] - X[i+k][j] + X[i][j] 
                     - fx[i+1][j+1] - fx[i+k][j+1] - fx[i+1][j+k] - fx[i+k][j+k];
                     double yy = Y[i+k][j+k] - Y[i][j+k] - Y[i+k][j] + Y[i][j] 
                     - fy[i+1][j+1] - fy[i+k][j+1] - fy[i+1][j+k] - fy[i+k][j+k];
                     double sm = sum[i+k][j+k] - sum[i][j+k] - sum[i+k][j] + sum[i][j] 
                     - field[i+1][j+1] - field[i+k][j+1] - field[i+1][j+k] - field[i+k][j+k];
                     cx *= sm;
                     cy *= sm;
                     if (fabs(cx - xx) < EPS && fabs(cy-yy) < EPS){
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
           // fprintf(stderr,"IMPOSSIBLE");
            puts("IMPOSSIBLE");
            }
 }
 
 //system("pause");
// while(true);
 return 0;          
}

