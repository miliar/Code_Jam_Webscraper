#include <cstdio>
#include <vector>

using namespace std;

int get() {
    int x;
    scanf("%d",&x);
    return x;
}

void go() {
    int n = get();
    vector<vector<int> > grid(101, vector<int>(101));
    for(int i=0;i<n;i++) {
        int x1=get();
        int y1=get();
        int x2=get();
        int y2=get();
        for(int i=x1;i<=x2;i++){
        for(int j=y1;j<=y2;j++){
            grid[j][i]=1;
        }
        }
    }
    bool changed=true;
    int t=-1;
    while(changed) {
        changed=false;
        t++;
        for(int i=100;i>=1;i--) {
        for(int j=100;j>=1;j--) {
            if(grid[i][j]) {
                changed=true;
                if(!grid[i][j-1]&&!grid[i-1][j]) {
                    grid[i][j]=0;
                }
            } else {
                if(grid[i][j-1]&&grid[i-1][j]) {
                    grid[i][j]=1;
                }
            }
        }
        }
    }
    printf("%d\n",t);
}

int main() {
    int c = get();
    for(int i=0;i<c;i++) {
        printf("Case #%d: ",1+i);
        go();
    }
}
