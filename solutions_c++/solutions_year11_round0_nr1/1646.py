#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

#define File

int abs(int v) { return v>0?v:-v;}

void solve(int cid) {

    int btns, bid;
    cin >> btns;

    int s[4]={0}, t=0, r;
    s[0]=s[2]=1;
    char w;
    for(int i=0; i<btns; ++i) {
        cin >> w >> bid;
        if(w=='O') r=0;else r=2;
        s[r+1]+=abs(s[r]-bid)+1;
        s[r]=bid;

        if(t>=s[r+1]) s[r+1]=++t;
        else t=s[r+1];
    }
    cout << "Case #" << cid << ": " << t << endl;
}

int main() {

#ifdef File
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif

    int cases, cid;
    cin >> cases;

    for(cid=1; cid<=cases; ++cid) {
        solve(cid);
    }

    return 0;
}
