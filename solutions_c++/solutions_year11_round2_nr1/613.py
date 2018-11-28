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
        int n; scanf("%d",&n);
        char s[n+1][n+1];
        for (int i=0;i<n;i++){
          scanf("%s",s[i]);
        }
        double wp[n], owp[n], oowp[n];
        int match[n], winmatch[n];
        for (int i=0;i<n;i++){
          int win = 0, cnt = 0;
          for (int j=0;j<n;j++){
            if (s[i][j]=='.')continue;
            cnt ++;
            if (s[i][j]=='1')win++;
          }
          match[i]=cnt;
          winmatch[i]=win;
          wp[i]=win*1./cnt;
        }
        for (int i=0;i<n;i++){
          double tmp = 0;
          int cnt = 0;
          for (int j=0;j<n;j++){
            if (s[i][j]=='.')continue;
            if (s[i][j]=='1'){
              tmp += winmatch[j]*1./(match[j]-1);
            }else{
              tmp += (winmatch[j]-1)*1./(match[j]-1);
            }
          }
          owp[i] = tmp/match[i];
        }
        for (int i=0;i<n;i++){
          double tmp = 0;
          int cnt = 0;
          for (int j=0;j<n;j++){
            if (s[i][j]=='.')continue;
            tmp += owp[j];
            cnt ++;
          }
          oowp[i] = tmp/cnt;
        }
        printf("Case #%d:\n",ti);
        for (int i=0;i<n;i++){
          printf("%.10lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
        }

    }
    return 0;
}


