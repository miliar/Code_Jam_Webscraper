#include <iostream>
#include <vector>
#include <algorithm>

#define INF 100000000

using namespace std;

int main(){
    int n;
    cin>>n;
    for (int cn=0;cn<n;++cn){
        int m,val;
        cin>>m>>val;
        vector<int> tree(m+1),change(m+1,0);
        for (int i=1;i<=m;++i){
            cin>>tree[i];
            if (i<=(m-1)/2) cin>>change[i];
        }
        vector<vector<int> > dp(m+1,vector<int>(2,INF));
        for (int i=(m-1)/2+1;i<dp.size();++i) dp[i][tree[i]]=0;
        for (int i=(m-1)/2;i>=1;--i){
            if (tree[i]){
                dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0];
                dp[i][0]<?=dp[i*2][0]+dp[i*2+1][1];
                dp[i][0]<?=dp[i*2][1]+dp[i*2+1][0];
                dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1];
                if (change[i]){
                    dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0]+1;
                    dp[i][1]<?=dp[i*2][0]+dp[i*2+1][1]+1;
                    dp[i][1]<?=dp[i*2][1]+dp[i*2+1][0]+1;
                    dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1]+1;
                }
            }
            else{
                dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0];
                dp[i][1]<?=dp[i*2][0]+dp[i*2+1][1];
                dp[i][1]<?=dp[i*2][1]+dp[i*2+1][0];
                dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1];
                if (change[i]){
                    dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0]+1;
                    dp[i][0]<?=dp[i*2][0]+dp[i*2+1][1]+1;
                    dp[i][0]<?=dp[i*2][1]+dp[i*2+1][0]+1;
                    dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1]+1;
                }
            }
        }
        cout<<"Case #"<<cn+1<<": ";
        if (dp[1][val]==INF) cout<<"IMPOSSIBLE"<<endl;
        else cout<<dp[1][val]<<endl;
    }
}
            
