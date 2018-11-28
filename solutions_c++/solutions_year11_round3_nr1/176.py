#include <memory.h>
#include <iostream>
#include <cstdio>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FOR1(i,n) for(__typeof(n) i=1;i<=(n);i++)
using namespace std;

char mmap[60][60];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;cin>>t;
    FOR1(cno, t) {
        memset(mmap, 0, sizeof mmap);
        int r, c;cin>>r>>c;
        FOR(i, r) cin>>mmap[i];
        bool possible=true;
        FOR(i, r) {
            FOR(j, c) {
                if(mmap[i][j] != '#') continue;
                if(mmap[i][j+1] != '#' ||
                   mmap[i+1][j] != '#'||
                   mmap[i+1][j+1] != '#') {
                       possible = false;
                       break;
                   }
                mmap[i][j] = '/';       mmap[i][j+1] = '\\';
                mmap[i+1][j] = '\\';    mmap[i+1][j+1] = '/';

            }
            if(!possible) break;
        }
        cout<<"Case #"<<cno<<":"<<endl;
        if(!possible) {
            cout<<"Impossible"<<endl;
        } else {
            FOR(i, r) cout<<mmap[i]<<endl;
        }
    }
    return 0;
}
