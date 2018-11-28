#include <cstdio>
#include <cstring>
#include <climits>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    
    int T,N;
    int d[10002],l[10002];
    int dp[10002],D;
    
    cin >> T;
    
    for(int tc = 1;tc <= T;++tc){
        cin >> N;
        
        d[0] = 0;
        
        for(int i = 1;i <= N;++i)
            cin >> d[i] >> l[i];
        
        cin >> D;
        
        bool found = false;
        
        memset(dp,0,sizeof dp);
        dp[1] = d[1];
        
        if(2 * d[1] >= D) found = true;
        
        for(int i = 1;i <= N && !found;++i){
            for(int j = 1;j < i;++j){
                if(d[j] + dp[j] >= d[i]){
                    //cout << i << " " << j << endl;
                    dp[i] = max(dp[i],min(d[i] - d[j],l[i]));
                }
            }
            
            if(d[i] + dp[i] >= D) found = true;
            
            //cout << i << " " << dp[i] << endl;
        }
        
        cout << "Case #" << tc <<": " << (found? "YES" : "NO") << '\n';
    }
    
    return 0;
}
