#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    long long r,k,n;
    scanf("%lld%lld%lld\n",&r,&k,&n);
    long long g[n], p[n], q[n];
    for (int i=0;i<n;i++){
      scanf("%lld",&g[i]);
    }
    for (int i=0;i<n;i++){
      p[i]=g[i]; q[i]=0;
      for (int j=1;j<n;j++){
        int t = (i+j)%n;
        if (p[i]+g[t] <= k){
          p[i] = p[i]+g[t];
          q[i] = j;
        }else{
          break;
        }
      }
    }
    long long head=0, ans=0;
    for (int i=0;i<r;i++){
      ans += p[head];
      head = (head+q[head]+1)%n;
    }
    printf("Case #%d: %lld\n", ti, ans);
  }


  return 0;
}
