#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
#define N 1100
  using namespace std;
  int a[N],n,ans;
  bool f[N];
int main(){
  freopen("d.in","r",stdin);freopen("d.out","w",stdout);
  int tc,tt;
  int i,j,k,x,y;
  scanf("%d",&tc);
  for(tt=1;tt<=tc;tt++){
     printf("Case #%d: ",tt);
     scanf("%d",&n);
     for(i=1;i<=n;i++)scanf("%d",&a[i]);
     memset(f,true,sizeof(f));
     ans=0;
     for(i=1;i<=n;i++)
       if(f[i]){
         k=0;
         x=i;
         while(f[x]){
            k++;
            f[x]=false;
            x=a[x];
            }
         if(k>1)ans=ans+k;
       }
     printf("%d.000000\n",ans);
     }
   return 0;
} 
