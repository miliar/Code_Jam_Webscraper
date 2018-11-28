#include <stdio.h>
#include <string.h>
int mat[555][555];
int h,w;
char ans[555][555],c='a';
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int dfs(int a, int b) {
    if(ans[a][b] != 0) return ans[a][b];
    int d = -1;
    int at = 0;
    for(int i=0; i<4; i++) {
        int x = a+dir[i][0];
        int y = b+dir[i][1];
        if(x >= 0 && x < h && y >= 0 && y < w) {
            if(mat[x][y] < mat[a][b] && at < mat[a][b]-mat[x][y]) {
                d = i;
                at = mat[a][b]-mat[x][y];
            }
        }
    }
    if(d == -1) {
        ans[a][b] = c;
        c++;
        return ans[a][b];
    }
    ans[a][b] = dfs(a+dir[d][0],b+dir[d][1]);
    return ans[a][b];
}
int main() {
    freopen("out.txt", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for(int v=1; v<=ca; v++) {
        scanf("%d%d", &h, &w);
        for(int i=0; i<h; i++) for(int j=0; j<w; j++) {
            scanf("%d", &mat[i][j]);
        }
        memset(ans, 0, sizeof(ans));
        c='a';
        for(int i=0; i<h; i++) for(int j=0; j<w; j++) {
            if(ans[i][j] == 0) {
                dfs(i,j);
            }
        }
        printf("Case #%d:\n", v);
        for(int i=0; i<h; i++) for(int j=0; j<w; j++) {
            printf("%c", ans[i][j]);
            if(j != w-1) printf(" ");
            else printf("\n");
        }
    }
    return 0;
}
