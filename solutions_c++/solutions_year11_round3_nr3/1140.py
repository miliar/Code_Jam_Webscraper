#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

long long findHcf(long long a,long long b){
       if(b==0) return a;
       else return findHcf(b,a%b);
}
int main(){
    freopen("C-small-attempt2.in","r",stdin);
    freopen("ankit.txt","w",stdout);
       int T,N;
       long long L,H,ans;
       scanf("%d",&T);
       for(int I=1;I<=T;I++){
               scanf("%d%lld%lld",&N,&L,&H);
               long long inp[N];
               long long hcf[N],lcm[N];
               for(int i=0;i<N;i++) scanf("%lld",&inp[i]);
               hcf[0]=lcm[0]=inp[0];

               bool con=false;
               /*for(int i=1;i<N;i++){
                       hcf[i]=findHcf(hcf[i-1],inp[i]);
                       lcm[i]=(lcm[i-1]*inp[i])/hcf[i];
               }

               for(int i=L;i<=hcf[N-1] && i<=H;i++){
                       if(hcf[N-1]%i==0){
                               con=true;
                               ans=i;
                               break;
                       }
               }
               for(int i=L/lcm[N-1];i*lcm[N-1]<=H;i++){
                       if(i*lcm[N-1]>=L){
                               con=true;
                               ans=i*lcm[N-1];
                               break;
                       }
               }//cout<<hcf[N-1]<<" "<<lcm[N-1]<<endl;
               */
               for(int i=L;i<=H;i++){
                       bool c=true;
                       for(int j=0;j<N && c;j++) if(i%inp[j]!=0 && inp[j]%i!=0) c=false;
                       if(c){
                               con=true;
                               ans=i;
                               break;
                       }
               }
               printf("Case #%d: ",I);
               if(!con) printf("NO\n");
               else printf("%lld\n",ans);

       }
       return 0;
}
