#include <iostream>
#include <vector>
using namespace std;

bool dfs(int now,int len,const vector<int> &dv,const vector<int> &lv,int d) {
    if(d-dv[now] <= len) return true;
    for(int i=now+1; i<dv.size(); ++i) {
        if(dv[i]-dv[now] > len) break;
        if(dfs(i, min(dv[i]-dv[now], lv[i]), dv, lv, d)) return true;
    }
    return false;
}

int main() {
    int t;
    cin>>t;

    int d,n;
    for(int tc=1; tc<=t; ++tc) {
        cin>>n;
        vector<int> dv(n), lv(n);
        for(int i=0; i<n; ++i) cin>>dv[i]>>lv[i];
        cin>>d;
        if(dfs(0, dv[0], dv, lv, d)) cout<<"Case #"<<tc<<": YES"<<endl;
        else cout<<"Case #"<<tc<<": NO"<<endl;
    }
}
