#include <cstdio>
#include <cstring>

int map[1005][1005], mark[1005][1005];
int C;

int main() {
//    freopen("input.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    int T, R, test = 1;
    int x1, y1, x2, y2, X, Y;

    for(scanf("%d", &T); T; T --) {
        memset(mark, 0, sizeof(mark));
        for(scanf("%d", &R); R; R --) {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for(int i = x1; i <= x2; i ++)
                for(int j = y1; j <= y2; j ++)
                    if(!map[i][j])
                        map[i][j] = 1, C ++;    
        }
        int step = 0;
        while(C) {
            step ++;
            for(int i = 1; i <= 100; i ++)
                for(int j = 1; j <= 100; j ++) {
                    if(!map[i - 1][j] && !map[i][j - 1])
                        mark[i][j] = 0;
                    else if(map[i - 1][j] && map[i][j - 1])
                        mark[i][j] = 1;
                    else
                        mark[i][j] = map[i][j];
                }
            C = 0;
            for(int i = 1; i <= 100; i ++)
                for(int j = 1; j <= 100; j ++) {
                    C += mark[i][j];
                    map[i][j] = mark[i][j];
                }
        }
        printf("Case #%d: %d\n", test ++, step);
    }
    return 0;
}

