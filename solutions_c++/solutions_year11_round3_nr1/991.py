#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

#define rep(i, n) for((i)=0; (i)<(int)(n); ++(i))

void solve(int cid) {

    vector<string> mat;
    string str;

    int r, c, i, j;
    bool impossible = false;
    cin >> r >> c;
    rep(i, r) cin >> str, mat.push_back(str);

    rep(i, r) {
        rep(j, c){
            if(mat[i][j]=='#') {
                mat[i][j]='/';
                if(!impossible && i+1<r && mat[i+1][j]=='#') mat[i+1][j]='\\';
                else impossible = true;
                if(!impossible && j+1<c && mat[i][j+1]=='#') mat[i][j+1]='\\';
                else impossible = true;
                if(!impossible && mat[i+1][j+1]=='#') mat[i+1][j+1]='/';
                else impossible = true;
            }
        }
    }
    cout << "Case #" << cid << ":" << endl;
    if(impossible ) cout << "Impossible" << endl;
    else {
        rep(i, r) cout << mat[i] << endl;
    }

    return ;
}

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int cases, cid;

    cin >> cases;
    rep(cid, cases) {
        solve( cid+1 );
    }
    return 0;
}
