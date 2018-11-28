#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<conio.h>
#define esp 1e-12
using namespace std;
int T,n,s,r,x;
double t;
struct P{
  int l,r,s;
};
P a[3000];
int sum;
int cmp(P p1,P p2){
  if (p1.s<p2.s) return 1;
  else if (p1.s==p1.s&&p1.l<p2.l) return 1;
  return 0;
}
int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int ca=0;
  int i,j,k,ss;
  scanf("%d",&T);
  while (T--){
    ca++;
    printf("Case #%d: ",ca);
    scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
    sum=0;
    int lk=0;
    for (i=0;i<n;i++){
      scanf("%d%d%d",&j,&k,&ss);
      if (lk<j){
         a[sum].l=lk;a[sum].r=j;
         a[sum].s=0;
         sum++;
      }
      a[sum].l=j;a[sum].r=k;
      a[sum].s=ss;
      sum++;
      lk=k;
    }
    if (lk!=x){
       a[sum].l=lk;a[sum].r=x;
       a[sum].s=0;
       sum++;
    }
    sort(a,a+sum,cmp);
    double ans=0;
    for (i=0;i<sum;i++){
       if (fabs(t)>esp){
          double tt=(double)(a[i].r-a[i].l)/(double)(a[i].s+r);
          if (t-tt>esp){
            ans+=tt;
            t=t-tt;
          }
          else{
            double ll=(double)(a[i].s+r)*t;
            ans=ans+t+((double)(a[i].r-a[i].l)-ll)/(double)(a[i].s+s);
            t=0;
          }
      }
      else 
        ans+=(double)(a[i].r-a[i].l)/(double)(a[i].s+s);
    }
    printf("%.8lf\n",ans);
  }
  return 0;
}
