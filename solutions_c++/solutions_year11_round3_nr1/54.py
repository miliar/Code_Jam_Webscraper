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

int r,c;

char grid[51][51];

bool ok(int row, int col) {
    if(!(row+1<r&&col+1<c)) return false;
    return( grid[row][col]=='#'&&grid[row][col+1]=='#'&&
           grid[row+1][col]=='#'&&grid[row+1][col+1]=='#');
}

void paint(int row, int col) {
    grid[row][col]='/';
    grid[row][col+1]='\\';
    grid[row+1][col]='\\';
    grid[row+1][col+1]='/';
}

void solve() {
    cin>>r>>c;
    bool bad=false;
    for(int i=0;i<r;i++) for(int j=0;j<c;j++) cin>>grid[i][j];
    for(int i=0;i<r&&!bad;i++) for(int j=0;j<c&&!bad;j++) if(grid[i][j]=='#') {
        if(ok(i,j)) {
            paint(i,j);
        } else {
            bad=true;
            break;
        }
    }
    if(bad) {
        cout<<"Impossible"<<endl;
        return;
    }
    for(int i=0;i<r;i++) {
        for(int j=0;j<c;j++) cout<<grid[i][j];
        cout<<endl;
    }
}

int main() {
    int cases;
    cin>>cases;
    for(int cnum=1;cnum<=cases;cnum++) {
        cout<<"Case #"<<cnum<<":"<<endl;
        solve();
    }
}
