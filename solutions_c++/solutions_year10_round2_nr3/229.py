#include <iostream>
#include <sstream>
#include <cmath>
#include <cstring>
#include <map>
#define inf 1000000000
#define len(a) int((a).size())
#define pb push_back
#define M int64(100003)
#define maxn 510
using namespace std;
typedef long long int64;
int N;

int64 dp[maxn][maxn], com[maxn][maxn];

int64 comb(int64 n, int64 k){
    if (n == k) return 1;
    if (k > n) return 0;
    if (n <= 1 || k < 1) return 1;
    if (k == 1) return n;
    
    int64 &res = com[n][k];
    if (res != -1){
        return res;    
    }
    res = comb(n-1, k-1) + comb(n-1, k);
    res %= M;
    //cout << "COMB " << n << " " << k <<  " = " << res << endl;
    return res;
}

int64 sub(int a, int n){
    if (n == 1){
        return 1;    
    }    
    int64 &res = dp[a][n];
    if (res != -1){
        return res;    
    }
    res = 0;
    for (int i = 1; i < n; i++){
        int v = n-i-1;
        int k = a-n-1;
        if (v > k) continue;
        int combi = comb(k, v);
        //cout << a << " " << n << " -> " << n << " " << i << " :: " << combi << endl;
        res += combi*sub(n, i);   
        res %= M; 
    }
    return res;
}

int64 solve(){
    memset(dp, -1, sizeof dp);
    cin >> N;
    int64 res = 0;
    for (int i = 1; i < N; i++){
        int64 r = sub(N, i);
        res += r;
        res %= M;
        //cout << "Kohal " << i << ": " << r << endl;
    }
    return res;
}

int main(){
    memset(com, -1, sizeof com);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        int64 r = solve();
        cout << "Case #" << t << ": " << r << endl;
    }
    return 0;    
}
