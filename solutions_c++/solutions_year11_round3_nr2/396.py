#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#define ii pair<long long int,long long int>

using namespace std;

int main()
{
   int T;
   cin>>T;
   for(int it=0;it<T;it++){
      long long ans=0;
      long long int L, t, N, C;
      long long int ai[1004];
      cin>>L>>t>>N>>C;
      long long tp=0;
      long long ppt=0;
      long long int fp=(N)/C;
      long long int pe=(N)%C;
    //  printf("%d %d %d %d\n",N,C,fp,pe);
      
      for(int i=0;i<C;i++){
         cin>>ai[i];
         tp+=ai[i];
         if(i<pe)
            ppt+=ai[i];
      }
     
     
      
    //  printf("tp:%lld fp:%d ppt:%lld\n",tp,fp,ppt);
      ans=2*(tp*fp+ppt);
    //  printf("tans:%d\n",ans);
      long long int dpn=0;
      ii dp[1005];
      
      long long fpr=t/(tp*2);
      //printf()
      
      if(t<ans){
         fp-=fpr;
         dpn=C;
         long long t2=(t/2)%tp;
         //if(t2){
            //fp--;
         //}
         for(int i=0;i<C;i++){
            dp[i]=ii(ai[i],fp);
            if(i<pe)
               dp[i].second++;
         }
         
         if(t2){
            long long int tt=0;
            for(int i=0;i<C;i++){
               if(tt<t2){
                  dp[i].second--;
                  tt+=ai[i];
                  if(tt>t2){
                     dpn++;
                     dp[C]=ii(tt-t2,1);
                  }
                  
               }
            }
         }
         
        // for(int i=0;i<dpn;i++){
        //    printf("dp[%d]={%d,%d}\n",i,dp[i].first,dp[i].second);
        // }
        sort(dp,dp+dpn);
         long long int cp=dpn;long long int ll=L;
         while(cp>=0 && ll>0){
            ii cr=dp[cp];
            long long int nus=min(ll,cr.second);
            ans-=(long long)cr.first*nus;
            ll-=nus;
            cp--;
         }
      }
      
      cout<<"Case #"<<(it+1)<<": "<<ans<<endl;
   }
     return 0;
}
