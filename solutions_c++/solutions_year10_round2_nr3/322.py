#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
using namespace std;
const int MOD = 100003;

int c[505][505], f[505][505], res[505];

int main(){
    freopen("C-small.in","r",stdin);
    freopen("c.out","w",stdout);
    
    int ntest;
    cin>>ntest;
    
    // calculate pascal triangle
    c[0][0] = 1;
    c[1][0] = 1;
    c[1][1] = 1;
    for (int i = 2; i < 500; i++){
        c[i][0] = 1;
        c[i][i] = 1;
        for (int j = 1; j<i; j++){
            c[i][j] = (c[i-1][j-1] + c[i-1][j])%MOD;
        }
    }
    
    // calculate the dynamic programming function
    int n = 500;
    //init
    for (int i=2;i<=n; i++) f[i][1] = 1;
    for (int i=3; i<=n; i++){
        for (int j=2; j<i; j++)
            for (int k=j-1; k>=1 && j-k-1<= i-j; k--){
                f[i][j] += f[j][k] * c[i-j-1][j-k-1];
                f[i][j] %= MOD;
            }
    }
    // res
    for(int i=2;i<=n;i++)
        for (int j=1;j<=i;j++) res[i] = (res[i] + f[i][j])%MOD;

    for(int test=1;test<=ntest;test++){

        cin>>n;
        cout<<"Case #"<<test<<": "<<res[n]<<endl;
    }
    
    return 0;
}

