#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <cstring>

using namespace std;

int evil[100][100];
int table[100][100];

int W, H;

#define MOD 10007

int solve(int x, int y) {
    int& resp = table[y][x];
    if(resp !=- 1) return resp;

    resp = 0;
    if(x-2 < W and y-1 < H) {
        resp = (resp + solve(x+2, y+1)) % MOD;
    }

    if(x-1 < W and y-2 < H) {
        resp = (resp + solve(x+1, y+2)) % MOD;
    }

    return resp;
}

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d:", t);

        scanf("%d%d",&H, &W);

        int R;

        scanf("%d", &R);

        memset(table, -1, sizeof(table));
        for(int i=0;i<R;++i) {
            int r, c;
            scanf("%d%d", &r, &c);
            table[r-1][c-1] = 0;
        }

        table[H-1][W-1] = 1;

        printf(" %d", solve(0, 0));

        printf("\n");
    }
    return 0;
}
