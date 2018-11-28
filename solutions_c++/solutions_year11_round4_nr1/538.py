#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define EPS 1e-10
typedef long long LL;

struct Dat{
  LL x,y,w;
  bool operator < (const Dat &a)const{ return w<a.w; }
} a[2000];

int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    double t;
    LL X,S,R,n;
    scanf("%lld%lld%lld%lf%lld",&X,&S,&R,&t,&n);
    FOR(i,0,n){
      scanf("%lld%lld%lld",&a[i].x,&a[i].y,&a[i].w);
    }

    a[n].x = 0;
    a[n].y = X;
    a[n].w = 0;
    FOR(i,0,n) a[n].y -= a[i].y-a[i].x;
    n++;

    sort(a,a+n);

    double ans = 0;
    FOR(i,0,n){
      if (t<EPS){
        ans += ((double)(a[i].y-a[i].x)) / (S + a[i].w);
      }else{
        double use = ((double)(a[i].y-a[i].x)) / (R + a[i].w);
        if (use <= t){
          ans += use;
          t -= use;
        }else{
          double d = (R+a[i].w)*t;
          ans += t + ((double)a[i].y-a[i].x-d)/(S+a[i].w);
          t = 0;
        }
      }
    }
    printf("Case #%d: %.8f\n",ca,ans);
  }
  return 0;
}
