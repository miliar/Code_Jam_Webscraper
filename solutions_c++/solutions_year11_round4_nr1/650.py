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
        int X,S,R,N;
        double T;
        scanf("%d%d%d%lf%d",&X,&S,&R,&T,&N);
        vector<pair<int, int> > a;
        int sum=0;

        for (int i=0;i<N;i++){
          int b,e,tmp;
          scanf("%d%d%d",&b,&e,&tmp);
          sum += e-b;
          a.push_back(make_pair(tmp, e-b));
        }
        if (X>sum){
          a.push_back(make_pair(0, X-sum));
        }
        
        int M = a.size();
        sort(a.begin(), a.end());

        double ans = 0;
        for (int i=0;i<M;i++){
          if (T<1e-10){
            ans += a[i].second*1. / (S+a[i].first);
          }else{
            double v = R+a[i].first;
            double time = a[i].second / v;
            if (time <= T){
              T -= time;
              ans += time;
            }else{
              ans += T + (a[i].second-(v*T))/(S+a[i].first);
              T = 0;
            }
          }
          //printf("~%lf %lf %d %d\n",ans,T,a[i].first,a[i].second);
        }
        printf("Case #%d: %.10lf\n",ti,ans);
    }
    return 0;
}
