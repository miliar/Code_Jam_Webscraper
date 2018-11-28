#include <iostream>
#include <set>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <string.h>
#include <cstdlib>
#include <stdio.h>
#define inf 1000000000
#define pb push_back
#define len(a) int((a).size())
using namespace std;

string tx;
bool used[40];
int A;

int sub(int p){
    bool all = true;    
    int res = inf;

    for (int i = 0; i < len(tx); i++){
        if (used[i]) continue;
        used[i] = true;
        int w = int(tx[i]-'0');    
        int r = sub(10*p+w);
        if (r > A && res > r) res = r;
        used[i] = false;
        all = false;
    }
    
    if (all) {
        if (p > A) return p;  
    }

    return res;
}

void solve(){
    cin >> tx;
    istringstream ss(tx);
    ss >> A;
    memset(used, 0, sizeof used);
    int res = sub(0);
    tx.pb('0');
    memset(used, 0, sizeof used);
    res = min(res, sub(0));
    cout << res << endl;    
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
