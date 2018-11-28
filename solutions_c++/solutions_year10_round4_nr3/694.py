
/*
 * File:   main.cpp
 * Author: GongZhi
 *
 * Created on 2010年6月5日, 下午10:19
 */

#include <stdlib.h>
#include <stdio.h>]
#include <string.h>

/*
 *
 */

int Map[200][200];

int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int kase, n, i, j, k;
    int x1, y1, x2, y2, c = 1;
    scanf("%d", &kase);
    while (kase--) {
        scanf("%d", &n);
        memset(Map,0,sizeof(Map));
        for (i = 0; i < n; i++) {
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            for (j = x1; j <= x2; j++)
                for (k = y1; k <= y2; k++)
                    Map[k][j] = 1;
        }
        bool yes;
        int time = 1;
        do {
            yes = false;
            for (i = 1; i <= 100; i++)
                for (j = 1; j <= 100; j++)
                    if (Map[i-1][j] == time && Map[i][j-1] == time && Map[i][j] != time) {
                        Map[i][j] = time+1;
                        yes = true;
                    }
            for (i = 100; i >= 1; i--)
                for (j = 100; j >= 1; j--)
                    if (Map[i][j] == time && (Map[i-1][j] == time || Map[i][j-1] == time) ) {
                        yes = true;
                        Map[i][j]++;
                    }
            if (yes) time++;
          //  printf("%d %d\n", time, Map[2][5]);
        } while (yes);
        printf("Case #%d: %d\n",c++, time);
    }
    return 0;
}


