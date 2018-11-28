#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
int main(){
   //freopen("C:\D-small-attempt0.in","r",stdin);
   //freopen("C:\dout","w",stdout);
   int T,n;
   scanf("%d",&T);
   int cases=1;
   while(T--){
       scanf("%d",&n);
       int m=(1<<29);
       int cnt=0,a;
       for(int i=1;i<=n;i++){
         scanf("%d",&a);
         if(a!=i) cnt++;
       }
       printf("Case #%d: %.6f\n",cases++,cnt*1.0);

   }
}
