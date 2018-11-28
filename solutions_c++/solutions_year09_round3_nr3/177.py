#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <string.h>
#include <cstdlib>
#include <stdio.h>
#define inf 1000000000
#define pb push_back
#define len(a) int((a).size())
#define maxq 120
using namespace std;

int P, Q, V[maxq];
int dp[maxq][maxq];

int sub(int a, int b){
    if (a == b-1) return 0;
    
    int &res = dp[a][b];
    if (res != -1) return res;
    res = inf;
    
    for (int i = a+1; i < b; i++){
        int r1 = sub(a,i);
        int r2 = sub(i,b);
        int th = abs(V[b]-V[a])-2;
        
        //cout << a << " " << b << " : " << r1 << " " << r2 << " " << th << endl;
        
        res = min(res, r1+r2+th);
    }   
    return res;
}

void solve(){
    cin >> P >> Q;
    for (int i = 1; i <= Q; i++){
        cin >> V[i];    
    }
    V[0] = 0;
    V[Q+1] = P+1;
    
    sort(V, V+Q+1);
    
    for (int i = 0; i <= Q+1; i++){
        //cout << "::" <<V[i] << endl;    
    }
    
    memset(dp, -1, sizeof dp);
    cout << sub(0, Q+1) << endl;
}

int main(){
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++){
        printf("Case #%d: ",i);    
        solve();
    }
    
    return 0;    
}
