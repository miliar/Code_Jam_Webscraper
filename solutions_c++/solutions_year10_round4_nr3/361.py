#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

const int MAX=101;

int grid[MAX][MAX];
int ngrid[MAX][MAX];

bool done() {
    for(int i=0;i<MAX;i++) for(int j=0;j<MAX;j++) if(grid[i][j]) return false;
    return true;
}

void iterate() {
    for(int i=0;i<MAX;i++) for(int j=0;j<MAX;j++) ngrid[i][j]=grid[i][j];
    for(int i=0;i<MAX;i++) for(int j=0;j<MAX;j++) {
        if((i>0&&j>0)&&(grid[i][j]&&!grid[i-1][j]&&!grid[i][j-1])) ngrid[i][j]=0;
        else if((i>0&&j>0)&&(!grid[i][j]&&grid[i-1][j]&&grid[i][j-1]))
            ngrid[i][j]=1;
    }
    for(int i=0;i<MAX;i++) for(int j=0;j<MAX;j++) grid[i][j]=ngrid[i][j];
}

int solve() {
    int r;
    int x1, y1, x2, y2;
    cin>>r;
    for(int i=0;i<r;i++) {
        cin>>x1>>y1>>x2>>y2;
        for(int x=x1;x<=x2;x++) for(int y=y1;y<=y2;y++) grid[y][x]=1;
    }
    int ret=0;
    while(!done()) {
        ret++;
        iterate();
    }
    return ret;
}

int main() {
    int cases;
    cin>>cases;
    for(int c=1;c<=cases;c++) {
        int ret=solve();
        cout<<"Case #"<<c<<": "<<ret<<endl;
    }
}
