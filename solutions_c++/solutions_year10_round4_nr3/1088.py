#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int ans = 0;
        int R; scanf("%d",&R);
        int a[150][150], b[150][150];
        int n =150;
        memset(a,0,sizeof(a));
        for (int i=0;i<R;i++){
          int t1,t2,t3,t4;
          scanf("%d%d%d%d",&t1,&t2,&t3,&t4);
          for (int i=t1;i<=t3;i++){
            for (int j=t2;j<=t4;j++){
              a[i][j]=1;
            }
          }
        }
        while (true){
          bool done=true;
          for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
              if (a[i][j])done=false;
            }
          }
          if (done)break;
          ans++;

          for (int i=1;i<n;i++){
            for (int j=1;j<n;j++){
              if (a[i][j]==0){
                if (a[i-1][j] && a[i][j-1])b[i][j]=1;
                else b[i][j]=a[i][j];
              }else{
                if (a[i-1][j]==0 && a[i][j-1]==0)b[i][j]=0;
                else b[i][j]=a[i][j];
              }
            }
          }
          for (int i=0;i<n;i++){
            for (int j=0;j<n;j++)a[i][j]=b[i][j];
          }
        }
        printf("Case #%d: %d\n",ti,ans);
    }
    return 0;
}
