#include <iostream>
#include <sstream>
#include <cmath>
#include <cstring>
#include <map>
#include <vector>
#define inf 1000000000
#define len(a) int((a).size())
#define pb push_back
#define maxn 55
using namespace std;

int N, K, B, T;
int X[maxn], V[maxn];

void input(){
    cin >> N >> K >> B >> T;
    
    for (int i = 0; i < N; i++){
        cin >> X[i];        
    }

    for (int i = 0; i < N; i++){
        cin >> V[i];        
    }    
}

bool reach(int x, int v, int t){
    return v*t + x >= B;    
}

int solve(){
    bool re[maxn];
    int dp[maxn];
    
    memset(re, 0, sizeof re);
    
    for (int i = 0; i < N; i++){
        re[i] = reach(X[i], V[i], T);    
    }

    vector<int> r;    
    dp[N] = 0;
    for (int i = N-1; i >= 0; i--){
        dp[i] = dp[i + 1];
        if (!re[i]){
            dp[i]++;   
        } else {
            r.pb(dp[i]);    
        }    
    }
    
    sort(r.begin(), r.end());
    if (len(r) < K){
        return -1;    
    }
    
    int res = 0; 
    for (int i = 0; i < K; i++){
        res += r[i];
    }

    return res;        
}

int main(){
    int C;
    cin >> C;
    for (int t = 1; t <= C; t++){
        input();
        int r = solve();
        if (r >= 0){
            cout << "Case #" << t << ": " << r << endl;
        } else {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;    
}
