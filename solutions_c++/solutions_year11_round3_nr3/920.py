#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

#define rep(i, n) for((i)=0; (i)<(int)(n); ++(i))

int n, l, h;

void solve(int cid) {

    int i, j, t;
    vector<int> p;

    cin >> n >> l >> h;
    rep(i, n) {
        cin >> t;
        p.push_back(t);
    }

    for(i=l; i<=h; ++i) {
        rep(j, n){
            if(i%p[j]==0 || p[j]%i==0) ;
            else break;
        }
        if(j>=n) {
            cout << "Case #" << cid << ": " << i << endl;
            return;
        }
    }

    cout << "Case #" << cid << ": NO"  << endl;
    return ;
}

int main() {

    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int cases, cid;

    cin >> cases;
    rep(cid, cases) {
        solve( cid+1 );
    }
    return 0;
}
