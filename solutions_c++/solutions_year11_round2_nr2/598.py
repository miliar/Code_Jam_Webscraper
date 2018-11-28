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

#define N 100010
int a[N];

int main(){
    int tt; scanf("%d",&tt);

    for (int ti=1;ti<=tt;ti++){
        int C,D,p,v;
        scanf("%d%d",&C,&D);
        int n = 0;
        for (int i=0;i<C;i++){
          scanf("%d%d",&p, &v);
          for (int j=0;j<v;j++){
            a[n++] = p;
          }
        }
        
        double l = 0, r = 1e40;
        double ans;
        while (r-l>1e-6){
          double m = (r+l)/2, tmp;
          double pos = a[0]-m; // first
          bool valid = true;
          //printf("m=%lf: ", m);
          for (int i=1;i<n && valid;i++){
            tmp = max(min(pos+D, a[i]+m), a[i]-m);

            if (fless(tmp, pos+D)){
              valid = false;
            }
            //printf("%lf ",pos);
            pos = tmp;
          }
          if (valid){
            ans = m;
            r = m;
          }else{
            l = m;
          }
          //puts("");
        }

        printf("Case #%d: %lf\n",ti,ans);
    }
    return 0;
}


