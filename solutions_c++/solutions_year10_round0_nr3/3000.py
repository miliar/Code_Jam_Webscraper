#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int ca,T,R,K,N,data,sum,ans,t;
queue<int> Q;
vector<int> in;
int main(){
    freopen("gcj2.in","r",stdin);
    freopen("gcj2.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d",&R,&K,&N);
        while(!Q.empty())   Q.pop();
        int i,j,r;
        for(i=1;i<=N;i++){
            scanf("%d",&data);
            Q.push(data);
        }
        sum=ans=0;
        for(r=1;r<=R;r++){
            sum=0;
            in.clear();
            while(1){
                t=Q.front();
                if(sum+t>K) break;
                Q.pop();
                in.push_back(t);
                sum+=t;
                ans+=t;
                if(Q.empty())   break;
            }
            for(i=0;i<in.size();i++){
                Q.push(in[i]);
            }
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
    return 0;
}
            
    
