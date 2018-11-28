#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <cstdio>
using namespace std;

#define ii pair<int,int>
//#define iii pair<int,ii>

int main()
{
   int T;
   cin>>T;
   for(int it=0;it<T;it++){
      float ans=0;
      int x,s,r,t,n;
      ii p[1002];
      cin>>x>>s>>r>>t>>n;
      float tl=t;
      int tB;
      int tE;
      int twi;
      for(int i=0;i<n;i++){
         cin>>tB>>tE>>twi;
         int l=tE-tB;
         x-=l;
         p[i]=ii(twi,l);
      }
      p[n]=ii(0,x);
      sort(p,p+n+1);
      for(int i=0;i<=n;i++){
         if(tl>0){
            float tr=(float)p[i].second/(float)(r+p[i].first);
            if(tr<tl){
               ans+=tr;
               tl-=tr;
            }else{
               float a2=p[i].second;
               a2-=(float)(p[i].first+r)*tl;
               ans+=a2/(float)(s+p[i].first);
               ans+=tl;
               tl=0;
            }
         }else{
            ans+=(float)p[i].second/(float)(s+p[i].first);
         }
      }
      printf("Case #%d: %.6f\n",it+1,ans);
      //cout<<"Case #"<<(it+1)<<": "<<ans<<endl;
   }
   return 0;
}
