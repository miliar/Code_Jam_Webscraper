#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 60;

char board[MAXN][MAXN];
char boardr[MAXN][MAXN];
int T, N, K;

int dx[] = {1, 1, 0, -1};
int dy[] = {0, 1, 1, 1};

int main(void) {
    scanf("%d", &T);
    for(int t = 0; t < T; ++t) {
        memset(board, 0, sizeof(board));
        memset(boardr, 0, sizeof(boardr));
        scanf("%d %d", &N, &K);
        for(int i = 0; i < N; ++i) {
            scanf("%s", board[i]);
        }

        for(int i = 0; i < N; ++i) for(int j = 0; j < N; ++j) {
            boardr[j][N-i-1] = board[i][j];
        }

        for(int j = 0; j < N; ++j) {
            int k = N-1;
            for(int i = N-1; i >= 0; --i) {
                if(boardr[i][j] != '.') {
                    boardr[k][j] = boardr[i][j];
                    --k;
                }
            }
            while(k>=0) boardr[k--][j] = '.';
        }

        int resp = 0;

        for(int i = 0; i < N; ++i) for(int j = 0; j < N; ++j) {
            for(int d = 0; d < 4; ++d) {
                char last = '.';
                int conta = 0;
                for(int i2 = i, j2 = j; i2 < N and j2 < N and j2 >= 0; i2 += dy[d], j2 += dx[d]) {
                    if(boardr[i2][j2] != last) {
                        last = boardr[i2][j2];
                        conta = 0;
                    }
                    if(last != '.') conta ++;
                    if(conta == K) {
                        if(last == 'R') resp|= 1;
                        if(last == 'B') resp|= 2;
                    }
                }
            }
        }
        const char* resps[] = {"Neither", "Red", "Blue", "Both"};
        printf("Case #%d: %s\n", t+1, resps[resp]);
    }
    return 0;
}
