#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <limits.h>

#define  F first
#define  S second

using namespace std;
typedef long long ll;

int n,a[10010],l,r;
ll gcd(ll x,ll y){
    return (x % y == 0 ? y : gcd(y,x % y));   
}
void solve(){
        cin >> n >> l >> r;
         int i;        
        for(int i = 0; i<n;i++) cin >> a[i];
        for(i = l;i<=r;i++){
            bool ok = true;
           for(int j = 0;j<n;j++)
              if (i % a[j] &&  a[j] % i) {
                    ok = false;
                    break;   
                }
            if (ok) {
                    cout << i << endl;
                    return;
            }   
        }       
        cout << "NO" << endl;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);      
    int ntest;
    cin >> ntest;
    for(int run = 0;run<ntest;run++){
        cout << "Case #"<< run+1 <<": " ; 
        solve();
    }
    return 0;
}
