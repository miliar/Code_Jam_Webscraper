#include<iostream>
using namespace std;

typedef long long LL;

LL T;
LL R,K;
LL N;
LL a[1010];
LL last[1010];
LL next[1010];
LL profit[1010];


int main(){
    LL i,j;
    long long s1,s2;
    LL cas = 0;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>T;
    while(T--){
        cin>>R>>K>>N;
        for(i=0;i<N;++i) cin>>a[i];
        memset(last,-1,sizeof(last));
        for(i=0;i<N;++i){
            profit[i]=0;
            j=i;
            LL c1 = 0;
            while(profit[i]+a[j]<=K&&c1<N){
                profit[i]+=a[j];
                j=(j+1)%N;
                c1++;
            }
            next[i] = j;
        }
        LL t1 = 0;
        LL cnt = 0;
        long long tot = 0;
        while(last[t1]==-1&&cnt<R){
            last[t1] = cnt;
            ++cnt;
            tot+=profit[t1];
            t1 = next[t1];
        }
        LL rest = R-cnt;
        s1 = 0;s2=0;
        if(rest){
            LL cycle = cnt-last[t1];
            j=t1;
            for(i=0;i<cycle;++i){
                s1+=profit[j];
                j=next[j];
            }
            j=t1;
            for(i=0;i<(rest%cycle);++i){
                s2+=profit[j];
                j=next[j];
            }
            tot = tot+s1*(rest/cycle)+s2;
        }
        cas++;
        cout<<"Case #"<<cas<<": ";
        cout<<tot<<endl;
        
    }
   
    return 0;
}
