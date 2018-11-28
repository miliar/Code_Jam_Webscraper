#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define x first
#define y second
#define c first
vector<vector<ll> > m(501,vector<ll> (1001,-1));
vector<vector<ll> > c(501,vector<ll>(501));
int rec(ll n, ll r){
    if(r <= 0) return 0;
    if(r == 1){ return 1; }
    if(r >= n) return 0;
    if(m[n][r]!=-1) return m[n][r];
    
    ll sol = 0;
    for(int i=2;i<n;i++){
            for(int j=0; j < n-i;j++){
                    if((j+1) + (r-1-j-1) != i-1) continue;
                    sol += ((rec(i, r - j - 1)%100003) * ((c[n-i-1][j])%100003))%100003;
            }
    }
    return m[n][r] = sol%100003;
}

int main(){
    c[0][0] = 1;
    for(int i=1;i<=500;i++) for(int j=0;j<=i;j++){
            c[i][j] = 0;
            if(j!=0) c[i][j] += c[i-1][j-1];
            if(j!=i) c[i][j] = (c[i][j]+c[i-1][j])%100003;
    }
    
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
            int N;
            cin >> N;
            ll sol = 1;
            
            for(int i=2;i<N;i++){
                    for(int j=0; j < N-i;j++){
                        // if((j+1) + (r-1-j-1) != i-1) continue;
                        sol += ((rec(i, i-1-j)%100003) * c[N-i-1][j])%100003;
                    }
            }
            cout << "Case #" << t << ": " << sol%100003 << endl;
    }
}
