#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <complex>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string.h>
using namespace std;

#define REP(i,n) for(int i=0;i<int(n);++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define SZ(v) int(v.size())
#define x first
#define y second
typedef pair<int,int> PII;

int n,p;
int memo[1050][25];
vector<int> m, v;

const int INF = 1000000000;
int dp(int pr, int k) { //partit, agafats
    if (pr>=n) {//si estic al jugador
        if (p-k>m[pr-n]) return INF;
        return 0;
    }
    else {
        int &ans = memo[pr][k];
        if (ans>=0) return ans;
        ans=INF;
        ans=min(ans, v[pr] + dp(2*pr,k+1) + dp(2*pr+1,k+1)); //agafo
        ans=min(ans, dp(2*pr,k) + dp(2*pr+1,k)); //no agafo
        return ans;
    }
}

int main () {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        cout << "Case #" << cas << ": ";
        cin >> p;
        m=vector<int> (1<<p);
        for (int i=0;i<(1<<p);++i) cin >> m[i];
        
        
        vector<vector<int> > price(p);
        n = (1<<p);
        v = vector<int> (2*n,0);
        for (int k=p-1;k>=0;--k) {
            price[k]=vector<int> (1<<k);
            for (int i=0;i<(1<<k);++i) cin >> price[k][i];
        }
        int pos=1;
        for (int i=0;i<p;++i) {
            for (int j=0;j<price[i].size();++j) v[pos++]=price[i][j];
        }
        
        memset(memo,-1,sizeof(memo));
        cout << dp(1, 0) << endl;
    }
}
