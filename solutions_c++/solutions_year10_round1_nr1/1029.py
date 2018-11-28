#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int T, N, K;
char grid[52][52];
char grid0[52][52];
bool red, blue;

void copy() {
    int i, j;
    for (i = 0; i < N + 2; i++) {
        for (j = 0; j < N + 2; j++) {
            grid[i][j] = grid0[i][j];
        }
    }
}

void test(int t) {
    int i, j, k, s, p;
    if (t == 1) {
        for (i = 1; i <= N; i++) {
            p = 1;
            for (j = 1; j <= N; j++) {
                if (grid[i][j] != '.') {
                    if (p != j) grid[i][p] = grid[i][j];
                    p++;
                }
            }
            while (p <= N) {
                grid[i][p] = '.';
                p++;
            }
        }
    }
    else if (t == 2) {
        for (i = 1; i <= N; i++) {
            p = N;
            for (j = N; j >= 1; j--) {
                if (grid[i][j] != '.') {
                    if (p != j) grid[i][p] = grid[i][j];
                    p--;
                }
            }
            while (p >= 1) {
                grid[i][p] = '.';
                p--;
            }
        }
        
    }
    else if ( t== 3) {
        for (i = 1; i <= N; i++) {
            p = 1;
            for (j = 1; j <= N; j++) {
                if (grid[j][i] != '.') {
                    if (p != j) grid[p][i] = grid[j][i];
                    p++;
                }
            }
            while (p <= N) {
                grid[p][i] = '.';
                p++;
            }
        }
    }
    /*
        for (i = 0; i <= N + 1; i++) {
          
            for (j = 0; j <= N + 1; j++) {
                printf("%c", grid[i][j]);
            }
            putchar(10);
        }
    
    
    */
    int dx[] = {1, 1, 1, -1, -1, -1, 0, 0};
    int dy[] = {0, 1, -1, 0, 1, -1, 1, -1};
    
    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N; j++) {
            if (grid[i][j] == 'R' || grid[i][j] == 'B') {
                for (k = 0; k < 8; k++) {
                    s = 1;
                    while (grid[i + s * dx[k]][j + s * dy[k]] == grid[i][j]) s++;
                    //printf("%d\n", s);
                    if (s >= K) {
                        
                        if (grid[i][j] == 'R') red = true;
                        else blue = true;
                    }
                }
            }
        }
    }
}

int main() {
    int i, j, c = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &N, &K);
        memset(grid, 0, sizeof(grid));
        memset(grid0, 0, sizeof(grid0));
        for (i = 1; i <= N; i++) {
            scanf("%s", grid0[i] + 1);
        }
        
        
        blue = red = false;
        for (i = 2; i <= 2; i++) {
            copy();
            test(i);
        }
        if (blue) {
            if (red) printf("Case #%d: Both\n", c);
            else printf("Case #%d: Blue\n", c);
        }
        else {
            if (red) printf("Case #%d: Red\n", c);
            else printf("Case #%d: Neither\n", c);
        }
        
        c++;
    }
    return 0;
}
