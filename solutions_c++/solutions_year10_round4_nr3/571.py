#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;
const int MAXN  = 101;
int grid[MAXN][MAXN];
int tempgrid[MAXN][MAXN];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int C;
    cin>>C;
    for(int tc=1;tc<=C;tc++) {
        memset(grid,0,sizeof(grid));
        int R;cin>>R;
        for(int k=0;k<R;k++) {
            int x1,y1,x2,y2;
            cin>>x1>>y1>>x2>>y2;
            for(int i=y1;i<=y2;i++) {
                for(int j=x1;j<=x2;j++) {
                    grid[i][j]=1;
                }
            }
        }

        int ret=0;
        while(1) {
            memset(tempgrid,0,sizeof(tempgrid));
            int total=0;
            for(int r=1;r<MAXN;r++) {
                for(int c=1;c<MAXN;c++) {
                    if(grid[r][c]) {
                        total=1;
                        if(r-1<=0||grid[r-1][c]==0) {
                            if(c-1<=0||grid[r][c-1]==0) {
                                tempgrid[r][c]=0;
                            }
                            else tempgrid[r][c]=1;
                        }
                        else {
                            tempgrid[r][c]=1;
                        }
                    }
                    else {
                        if(r-1>0&&grid[r-1][c]==1) {
                            if(c-1>0&&grid[r][c-1]==1) {
                                tempgrid[r][c]=1;
                            }
                        }
                    }
                }
            }
            if(total==0) break;
            ret++;
            for(int r=1;r<MAXN;r++)for(int c=1;c<MAXN;c++) grid[r][c]=tempgrid[r][c];
        }

         cout<<"Case #"<<tc<<": "<<ret<<endl;
    }
    return 0;
}
