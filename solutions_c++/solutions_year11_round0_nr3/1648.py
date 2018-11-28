#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int n;
int a[1001];
int m[1048576];

void solve() {

    int s=0, tmp=0, t, m=1000004;
    cin >> n;
    for(int i=0; i<n; ++i) {cin >> t; tmp^=t; s+=t; if(t<m) m=t;}
    if(tmp) cout << "NO" << endl;
    else cout << (s-m) << endl;
}

int main() {

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int cases,cid;
    cin >> cases;

    for(cid=1; cid<=cases; ++cid) {
        cout << "Case #" << cid << ": ";
        solve();
    }

    return 0;
}

