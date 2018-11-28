#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cassert>
using namespace std;

int R, C;
char grid[55][55];


void work() {
    scanf("%d %d\n", &R, &C);
    for (int i = 0; i < R ; i++) {
        for (int j = 0; j < C ; j++) {
            scanf("%c", &grid[i][j]);
            assert(grid[i][j] == '#' || grid[i][j] == '.');
        }
        char x;
        scanf("\n", &x);
    }
    bool p = true;
    for (int i = 0 ; i < R && p; i++) {
        for (int j = 0 ; j < C && p; j++) {
            if (grid[i][j] == '#') {
                if ( i + 1 >= R || j + 1 >= C || grid[i+1][j] != '#' || grid[i][j+1] != '#' || grid[i+1][j+1] != '#' ) {
                    p = false;
                    continue;
                }
                grid[i][j] = '/';
                grid[i][j+1] = '\\';
                grid[i+1][j] = '\\';
                grid[i+1][j+1] = '/';
            }
        }
    }
    if (!p) {
        printf("Impossible\n");
    }
    else {
        for (int i =0 ; i < R ; i++) {
            for (int j = 0 ; j < C ; j++) {
                printf("%c", grid[i][j]);
            }
            printf("\n");
        }
    }
}

/////////////////////////////////////////////////////////////

int main() {
    int T;
    scanf("%d\n", &T);
    for (int tt = 1 ; tt <= T ; tt++) {
        printf("Case #%d:\n", tt);
        work();
    }
}
