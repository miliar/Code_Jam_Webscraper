#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int X,S,R,T,N;
int sum[205];

void solve(){
     scanf("%d%d%d%d%d",&X,&S,&R,&T,&N);
     R-=S;
     if (R<0) R=0;
     memset(sum,0,sizeof(sum));
     sum[S]=X;
     for (int i=1,b,e,w;i<=N;i++) {
         scanf("%d%d%d",&b,&e,&w);
         sum[S]-=e-b;
         sum[w+S]+=e-b;
     }
     double remain=T;
     double ans=0;
     for (int i=0;i<=202;i++) 
         if (sum[i]) {
            double dis=sum[i];
            double nowv=i+R;
            double thistime=dis/nowv;
            if (thistime<=remain) {
               remain-=thistime;
               ans+=thistime;
            }  else {
               ans+=remain;
               dis-=nowv*remain;
               ans+=dis/double(i);
               for (int j=i+1;j<=200;j++)
                   ans+=double(sum[j])/double(j);
               break;
            }
         }
     printf("%.8f\n",ans);
}

int main(){
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    int test;
    scanf("%d",&test);
    for (int tot=1;tot<=test;tot++) {
        printf("Case #%d: ",tot);
        solve();
    }
    
    
    return 0;
}
