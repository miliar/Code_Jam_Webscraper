#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<memory>
#include<functional>

using namespace std;


int f(int h, int w, int r, pair<int,int>* p) {
    
    int dp[105][105] = {{0}};
    
    for(int i=0; i<r; i++) {
        dp[p[i].first-1][p[i].second-1] = -1;
    }
    dp[0][0] = 1;
    
    for(int i=0; i<h; i++) {
        for(int j=0; j<w; j++) {
            if(dp[i][j] < 0) continue;
            if(i>=1 and j>=2 and dp[i-1][j-2]>=0)
                dp[i][j] += dp[i-1][j-2];
            if(i>=2 and j>=1 and dp[i-2][j-1]>=0)
                dp[i][j] += dp[i-2][j-1];
            dp[i][j] %= 10007;
        }
    }
    
    return dp[h-1][w-1];
    
}


int main() {
    int N;
    pair<int, int> p[10];
    cin >> N;
    for(int t=1; t<=N; t++) {
        int h ,w , r;
        cin >> h >> w >> r;
        for(int i=0; i<r; i++) cin >> p[i].first >> p[i].second;
        
        cout << "Case #" << t << ": " ;
        cout << f(h, w, r, p) << endl;
    }
}
