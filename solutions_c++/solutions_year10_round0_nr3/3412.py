#include<iostream>
using namespace std;

int main(){
    long long t;
    cin>>t;
    for(long long x=1; x<=t; x++){
        long long R, k, N;
        cin>>R>>k>>N;
        long long g[N];
        for(long long i=0; i<N; i++)
            cin>>g[i];

        long long cost[N+1];
        long long visit[N];
        cost[0]=0;
        for(long long i=0; i<N; i++)
            visit[i]=0;

        long long cur=0, iter=0;
        while(!visit[cur] && iter<R){
            //cout<<cur<<endl;
            visit[cur]=++iter;
            long long cnt = 0, sprint=0;
            while(cnt+g[cur]<=k && sprint++<N){
                cnt+=g[cur];
                cur=(cur+1)%N;
            }
            cost[iter]=cost[iter-1]+cnt;
        }
        long long ans = cost[iter];
        R-=iter;
        long long start = visit[cur], clen = iter - start +1;
        //cout<<cost[iter]<<" "<<cost[start]<<endl;
        long long ccost = cost[iter] - cost[start-1];
        //cout<<R<<" "<<clen<<" "<<ccost<<endl;
        ans+=(R/clen)*ccost;
        ans+=cost[(R%clen)+start-1] - cost[start-1];

        cout<<"Case #"<<x<<": "<<ans<<endl;
    }
    return 0;
}

