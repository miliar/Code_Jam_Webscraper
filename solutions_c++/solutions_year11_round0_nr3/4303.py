#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
int main(){
  // freopen("C:\C-small-attempt0.in","r",stdin);
  // freopen("C:\out","w",stdout);
   int T,n;
   scanf("%d",&T);
   int cases=1;
   while(T--){
       scanf("%d",&n);
       int m=(1<<29);
       int cnt=0,a;
       double sum=0;
       for(int i=1;i<=n;i++){
         scanf("%d",&a);
         cnt=(cnt^a);
         m=min(m,a);
         sum+=a;
       }
       if(cnt!=0){
        printf("Case #%d: NO\n",cases++);
       }else{
         printf("Case #%d: %.0lf\n",cases++,sum-m);
       }
   }
}
