#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>

#define N 510
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

char s[1000];
double a[N][N], a1[N][N], a2[N][N], a3[N][N];

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int R,C,D; scanf("%d%d%d",&R, &C, &D);
        memset(a,0,sizeof(a));
        memset(a1,0,sizeof(a1));
        memset(a2,0,sizeof(a2));
        memset(a3,0,sizeof(a3));
        for (int i=1;i<=R;i++){
          scanf("%s",s);
          for (int j=1;j<=C;j++){
            a[i][j] = D+s[j-1]-48;
            a1[i][j] = a[i][j] + a1[i-1][j] + a1[i][j-1] - a1[i-1][j-1];
            a2[i][j] = (a[i][j])*(i-0.5) + a2[i-1][j] + a2[i][j-1] - a2[i-1][j-1];
            a3[i][j] = (a[i][j])*(j-0.5) + a3[i-1][j] + a3[i][j-1] - a3[i-1][j-1];
          }
        }

        /*
        for (int i=0;i<=R;i++){
          for (int j=0;j<=C;j++){
            printf("%.2lf ", a1[i][j]); 
          }
          puts("");
        }
          puts("");
        for (int i=0;i<=R;i++){
          for (int j=0;j<=C;j++){
            printf("%.2lf ", a2[i][j]); 
          }
          puts("");
        }
        printf("here\n");
*/
        int ans=2;
        for (int i=1;i<=R;i++){
          for (int j=1;j<=C;j++){
            for (int k=ans+1;k<=i && k<=j;k++){
              double v1 = a1[i][j]-a1[i-k][j]-a1[i][j-k]+a1[i-k][j-k] - a[i][j] - a[i][j-k+1] - a[i-k+1][j] - a[i-k+1][j-k+1];
              double v2 = a2[i][j]-a2[i-k][j]-a2[i][j-k]+a2[i-k][j-k] - a[i][j]*(i-0.5) - a[i][j-k+1]*(i-.5) - a[i-k+1][j]*(i-k+.5) - a[i-k+1][j-k+1]*(i-k+.5);
              double v3 = a3[i][j]-a3[i-k][j]-a3[i][j-k]+a3[i-k][j-k] - a[i][j]*(j-.5) - a[i][j-k+1]*(j-k+.5) - a[i-k+1][j]*(j-.5) - a[i-k+1][j-k+1]*(j-k+.5);
              double cx = (i-k*0.5);
              double cy = (j-k*0.5);
              //printf("%d %d %d: %lf %lf, %lf %lf\n",i,j,k,v1*cx,v2, v1*cy,v3);
              if (fequal(v1*cx, v2) && fequal(v1*cy, v3)){
                ans = k;
              }
            }
          }
        }
        if (ans>=3){
        printf("Case #%d: %d\n",ti,ans);
        }else{
          printf("Case #%d: IMPOSSIBLE\n", ti);
        }
    }
    return 0;
}
