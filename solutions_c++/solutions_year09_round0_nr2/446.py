#include <iostream>
using namespace std;
int grid[100][100];
char ans[100][100];
int delta[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int H,W;
char solve(int x, int y, char alter) {
   while (true) {
        if (ans[x][y]) return ans[x][y];
        if (alter) ans[x][y]=alter;
        int best = grid[x][y];
        int bx, by;
        for (int k=0; k<4; k++) {
            int ii = x+delta[k][0];
            int jj = y+delta[k][1];
            if (ii<0 || jj<0 || ii>=H || jj>=W) continue;
            if (grid[ii][jj]<best) {
                best = grid[ii][jj];
                bx=ii;
                by=jj;                    
            }
        }
        if (best<grid[x][y]) {
            x=bx;
            y=by;
        } else break;
    }    
    return ans[x][y];
}
int main() {
    int t = 0;
    int T; scanf("%d",&T); while (T--) {t++;
    printf("Case #%d:\n",t);
        scanf("%d %d",&H,&W);
        for (int i=0; i<H; i++)
        for (int j=0; j<W; j++) scanf("%d",&grid[i][j]);
        memset(ans,0,sizeof(ans));
        char next = 'a';
        for (int i=0; i<H; i++) {
            for (int j=0; j<W; j++) {
                if (!ans[i][j]) {
                    char ret = solve(i,j,0);
                    if (!ret) ret = next++;

                    solve(i,j,ret);               
                }
                if (j!=0) printf(" ");
                printf("%c",ans[i][j]);
            }
            printf("\n");
        }
    }
}
