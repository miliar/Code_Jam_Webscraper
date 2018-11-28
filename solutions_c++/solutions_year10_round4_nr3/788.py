#include <stdio.h>
#include <string.h>

int map[110][110];

int main()
{
    int T, n, maxx, minx, maxy, miny, i, j, k, time, cnt, re = 1;
    int x1, y1, x2, y2;
    freopen("C-small-attempt0.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    maxx = maxy = -1;
    minx = miny = 1000;
    while(T--) {
        memset(map, -1, sizeof(map));
        scanf("%d", &n);
        cnt = 0;
        for(k = 0; k < n; ++k) {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            if(x1 > maxx)
                maxx = x1;
            if(x2 > maxx)
                maxx = x2;
            if(x1 < minx)
                minx = x1;
            if(x2 < minx)
                minx = x2;
            if(y1 > maxy)
                maxy = y1;
            if(y2 > maxy)
                maxy = y2;
            if(y1 < miny)
                miny = y1;
            if(y2 < miny)
                miny = y2;
            for(i = x1; i <= x2; ++i)
                for(j = y1; j <= y2; ++j) {
                    if(map[i][j] == -1) {
                        map[i][j] = 0;
                        ++cnt;
                    }
                }
        }
        time = 1;
        while(cnt) {
            //printf("%d\n", time);
            for(i = maxx; i >= minx; --i) {
                for(j = maxy; j >= miny; --j) {
                    if(map[i][j] != -1)
                        continue;
                    if(map[i][j - 1] != -1 &&
                        map[i - 1][j] != -1) {
                        map[i][j] = time;
                        ++cnt;
                       // printf("%d %d\n", i, j);
                    }
                }
            }
            //printf("*********\n");
            for(i = maxx; i >= minx; --i) {
                for(j = maxy; j >= miny; --j) {
                    //if(map[i][j] != time - 1)
                    //    continue;
                    if(map[i][j] == -1)
                        continue;
                    if((map[i][j - 1] == -1 || map[i][j - 1] == time)&&
                        (map[i - 1][j] == -1 || map[i - 1][j] == time)) {
                        map[i][j] = -1;
                        --cnt;
                    //    printf("%d %d\n", i, j);
                    }
                }
            }
            //printf("********\n");
            ++time;
            //if(time == 6)
            //    while(1);
        }
        printf("Case #%d: %d\n", re++, time - 1);
    }
    return 0;
}
