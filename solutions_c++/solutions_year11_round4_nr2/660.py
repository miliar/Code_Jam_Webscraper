#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <queue>
using namespace std;

int r,c,d;

int grid[501][501];

bool ok(int y1, int x1, int y2, int x2) {
    //cout<<endl;
    double centerx=1.0*(x1+x2)/2;
    double centery=1.0*(y1+y2)/2;

    double diffx=0, diffy=0;
    for(int y=y1;y<y2;y++) {
        for(int x=x1;x<x2;x++) {
            //cout<<grid[y][x];
            if((y1==y&&x1==x)||(y1==y&&x2-1==x)||(y2-1==y&&x1==x)||(y2-1==y&&x2-1==x)) {
                continue;
            }
            int realmass=d+grid[y][x];
            double cy=1.0*(y+y+1)/2;
            double cx=1.0*(x+x+1)/2;
            diffx+=(cy-centery)*realmass;
            diffy+=(cx-centerx)*realmass;
        }
       // cout<<endl;
    }
    return (diffx==0&&diffy==0);
}

bool ok(int k) {
    for(int i=0;i+k<=r;i++) for(int j=0;j+k<=c;j++) {
        if(ok(i,j,i+k,j+k)) return true;
    }
    return false;
}

void solve() {
    cin>>r>>c>>d;
    char cc;
    for(int i=0;i<r;i++) for(int j=0;j<c;j++) {
        cin>>cc;
        grid[i][j]=cc-'0';
    }
    //ok(1,1,1+5,1+5);
    //return;
    for(int k=min(r,c);k>2;k--) {
        if(ok(k)) {
            cout<<k<<endl;
            return;
        }
    }
    cout<<"IMPOSSIBLE"<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int cnum=1;cnum<=cases;cnum++) {
        cout<<"Case #"<<cnum<<": ";
        solve();
    }
}
