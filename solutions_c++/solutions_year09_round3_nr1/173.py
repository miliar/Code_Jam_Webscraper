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
using namespace std;
typedef long long int64;

string N;
int W[255];

void solve(){
    cin >> N;
    memset(W,-1,sizeof W);
    
    int base=-1;
    W[int(N[0])] = 1;
    for (int i = 1; i < len(N); i++){
        if (W[int(N[i])] != -1) continue;    
        if (base < 0){
            W[int(N[i])] = 0;
            base  = 2;    
        } else {
            W[int(N[i])] = base;
            base++;    
        }
    }
    
    if (base < 0) base = 2;
    
    int64 res = 0;
    for (int i = 0; i < len(N); i++){
        res *= int64(base);
        res += W[int(N[i])];
    }
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
