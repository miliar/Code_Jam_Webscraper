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
int dx[2]={-1,0},dy[2]={0,-1};
typedef vector<string> VS;

VS pas(VS v) {
    int n = v.size(),m=v[0].size();
    VS ans(n,string(m,'0'));
    REP(i,n) REP(j,m) {
        int te[2]={0,0};
        REP(d,2) {
            int ni=i+dx[d],nj=j+dy[d];
            if (ni>=0 and nj>=0 and ni<n and nj<m) {
                if (v[ni][nj]=='1') te[d]=1;
            }
        }
        if (v[i][j]=='1'){
            if (te[0]==0 and te[1]==0) ans[i][j]='0';
            else ans[i][j]='1';
        }
        else {
            if (te[0]==1 and te[1]==1) ans[i][j]='1';
            else ans[i][j]='0';
        }
    }
    return ans;
}

int main () {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        cout << "Case #" << cas << ": ";
        int r;
        cin >> r;
        vector<int> xs(r),ys(r);
        vector<int> xe(r),ye(r);
        
        int n=0,m=0;
        REP(i,r) {
            int a,b,c,d;
            cin >> a >> b >> c >> d;
            xs[i]=a;
            xe[i]=c;
            ys[i]=b;
            ye[i]=d;
            n=max(n,max(a,c));
            m=max(m,max(b,d));
        }
        vector<string> v(n,string(m,'0'));
        REP(k,r) {
            FOR(i,xs[k],xe[k]) FOR(j,ys[k],ye[k]) 
                v[i-1][j-1]='1';
        }
        VS w=v;
        int ans=0;
        bool fi=1;
        while(1) {
            fi=1;
            for (int i=0;fi and i<n;++i) if (w[i]!=string(m,'0')) fi=0;
            if (fi) break;
            ++ans;
            w = pas(w);
        }
        cout << ans << endl;
    }
}
