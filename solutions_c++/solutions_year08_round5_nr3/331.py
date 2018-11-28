#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <cstring>

using namespace std;

int table[11][1<<20];

char mapa[128][128];

int M, N;

int solve(int y, int m) {
    int& resp = table[y][m];
    if(resp != -1) return resp;

    if(y == M) { return resp = 0; }

    resp = 0;

    for(int x = 0; x < N; ++x) {
        if((((m >> x) & 1) == 0) && mapa[y][x]=='.') {
            int m1 = m;
            m1 |= (1<<x);
            if(x > 0) {
                m1 |= 1<<(x-1);
                m1 |= 1<<(x-1+N);
            }
            if (x < N-1) {
                m1 |= 1<<(x+1);
                m1 |= 1<<(x+1+N);
            }
            resp = max(resp, 1 + solve(y, m1));
        }
    }

    resp = max(resp, solve(y+1, m >> N));

    return resp;
}


int main(void) {
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d:", t);

        scanf("%d%d", &M, &N);

        for(int i=0;i<M;++i) {
            scanf("%s", mapa[i]);
        }

        memset(table, -1, sizeof(table));

        printf(" %d", solve(0, 0));

        printf("\n");
    }
    return 0;
}
