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

vector<string> v,w;
int n, k;

int main () {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        cin >> n >> k;
        v=w=vector<string> (n,string(n,'.'));
        for (int i=0;i<n;++i) cin >> v[i];
        for (int i=n-1;i>=0;--i) { //fila a v, columna a w
            int wpos=n-1;
            for (int vpos=n-1;vpos>=0;--vpos) if (v[i][vpos]!='.') {
                w[wpos][n-i-1]=v[i][vpos];
                --wpos;
            }
        }
        
        int di[4]={1,0,1,1};
        int dj[4]={0,1,1,-1};
        
        int win[2]={0,0};
        for (int col=0;col<2 and !win[col];++col) REP(i,n) REP(j,n) {
            if (win[col]) continue; //poda
            
            char c = 'B';
            if (col==1) c='R';
            for (int d=0;d<4;++d) {
                bool okdir=1;
                for (int r=0;okdir and r<k;++r) {
                    if (i+r*di[d]>=0 and i+r*di[d]<n and j+r*dj[d]>=0 and j+r*dj[d]<n) {
                        if (w[i+r*di[d]][j+r*dj[d]]!=c) okdir=0;
                    }
                    else okdir=0;
                }
                if (okdir) win[col]=1;
            }
        }
        
        //for (int i=0;i<n;++i) cout << w[i] << endl;
        cout <<"Case #" <<cas << ": ";
        if (win[0] and win[1]) cout << "Both" << endl;
        else if (win[0]) cout << "Blue" << endl;
        else if (win[1]) cout << "Red" << endl;
        else cout << "Neither" << endl;
    }
}
