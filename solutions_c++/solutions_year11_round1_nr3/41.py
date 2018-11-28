#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int solve(int n,vector<int> &c,vector<int> &s,vector<int> &t,vector<int> used,int turn) {
    int nmax=c.size();
    int pt=0;
    if (turn==0)return 0;
    n=min(nmax,n);
    for (int i=0; i<n; i++) {
        if (used[i]==1)continue;
        if (t[i]>0) {
            used[i]=1;
            turn+=t[i]-1;
            n+=c[i];
            pt+=s[i];
        }
        n=min(nmax,n);
    }
    int ms=0,ms1=0,msi=-1,ms1i=-1;
    n=min(nmax,n);
    for (int i=0; i<n; i++) {
        if (used[i]==1)continue;
        if (s[i]>ms) {
            ms=s[i];
            msi=i;
        }
        if (c[i]==1) {
            if (s[i]>ms1) {
                ms1=s[i];
                ms1i=i;
            }
        }
    }
    if (msi==-1)return pt;
    if (ms==ms1) {
        used[ms1i]=1;
        n+=c[ms1i];
        pt+=s[ms1i];
        return pt+solve(n,c,s,t,used,turn-1);
    } else if (ms1i==-1) {
        used[msi]=1;
        n+=c[msi];
        pt+=s[msi];
        return pt+solve(n,c,s,t,used,turn-1);        
    } else {
        vector<int> usedc=used;
        used[msi]=1;
        usedc[ms1i]=1;
        return pt+max(s[msi]+solve(n+c[msi],c,s,t,used,turn-1),s[ms1i]+solve(n+c[ms1i],c,s,t,usedc,turn-1));
    }
}

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int n,m;
        vector<int> c,s,t,used;
        cin >> n;
        for (int j=0; j<n; j++) {
            int ct,st,tt;
            cin >> ct >> st >> tt;
            c.push_back(ct);
            s.push_back(st);
            t.push_back(tt);
            used.push_back(0);
        }
        cin >> m;
        for (int j=0; j<m; j++) {
            int ct,st,tt;
            cin >> ct >> st >> tt;
            c.push_back(ct);
            s.push_back(st);
            t.push_back(tt);
            used.push_back(0);
        }
        cout << "Case #" << i+1 << ": " << solve(n,c,s,t,used,1) << endl;
    }
    return 0;
}
