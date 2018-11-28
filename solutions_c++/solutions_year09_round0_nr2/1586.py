#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)
#define id(x,y) ((x)*c+(y))
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int fa[100000];
char mw[100000];
int mp[200][200], nw;
int nk, r, c;


int root(int x) {
    if (fa[x] < 0) return x;
    fa[x] = root(fa[x]);
    return fa[x];
}    

void merge(int a, int b) {
    if (root(a) == root(b)) return;
    a = root(a);
    b = root(b);
    fa[a] = b;
}    

void solve() {
    for (int i = 0; i < r; i++) 
        for (int j = 0; j < c; j++) {
            nw = 1000000000;
            nk = -1;
            int nx, ny;
            for (int k = 0; k < 4; k++) {
                nx = i + dx[k];
                ny = j + dy[k];
                if (nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
                if (mp[nx][ny] < mp[i][j]) {
                    if (mp[nx][ny] < nw) {
                        nw = mp[nx][ny];
                        nk = k;
                    }    
                }                                            
            }    
            if (nk < 0) continue;
            merge(id(i,j),id(i+dx[nk],j+dy[nk]));
        }    
}    

int main() {
    int cas;
    cin >> cas;
    for (int tt = 0; tt < cas; tt++) {
        cout << "Case #" << tt + 1 << ":" << endl;
        cin >> r >> c;
        for (int i = 0; i < r; i++) 
            for (int j = 0; j < c; j++) cin >> mp[i][j];
            
        for (int i = 0; i < r; i++) 
            for (int j = 0; j < c; j++) {
                fa[i * c + j] = -1;
                mw[i * c + j] = i * c + j;
            }
        solve();    
        memset(mw,0,sizeof(mw));
        int tot = 'a';
        for (int i = 0; i < r; i++) 
            for (int j = 0; j < c; j++) {
                if (mw[root(id(i,j))] == 0) mw[root(id(i,j))] = tot++;                
            }
                
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (j) cout << " ";
                cout << mw[root(id(i,j))];                                
            }    
            cout << endl;
        }    
    }    
}    
