#include <stdio.h>

int T;
int row,col;
char map[60][60];
char dx[] = {0,0,1,1};
char dy[] = {0,1,0,1};
char dict[] = "/\\\\/";
bool check(int sx, int sy) {
    int i;
    if (map[sx][sy] != '#') {
        return true;
    }
    if (sx + 1 < row && sy + 1 < col) {
        for (i = 0; i < 4; i++) {
            if (map[sx + dx[i]][sy + dy[i]] != '#') {
                return false;
            }
            map[sx + dx[i]][sy + dy[i]] = dict[i];
        }
        return true;
    }
    return false;
}
int main () {
    int i,j,cs;
    bool flag;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);

    for (cs = 1; cs <= T; cs++) {
        scanf("%d%d",&row,&col);
        flag = true;
        for (i = 0; i < row; i++) {
            scanf("%s",map[i]);
        }
        for (i = 0; flag && i < row; i++) {
            for (j = 0; j < col; j++) {
                if (!check(i,j)) {
                    flag = false;
                    break;
                }
            }
        }
        printf("Case #%d:\n",cs);
        if (flag) {
            for (i = 0; i < row; i++) {
                puts(map[i]);
            }
        } else {
            puts("Impossible");
        }
    }
    return 0;
}
