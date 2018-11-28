#include "iostream"
#include "stdio.h"
#include "string.h"

using namespace std;

#define D_1 0
#define D_2 1
#define N   4

#define DOT 0
#define O   1
#define T   2
#define X   3

int code(char mark) {
    switch (mark) {
        case 'X':
            return X;
        case 'O':
            return O;
        case '.':
            return DOT;
        case 'T':
        default:
            return T;
    }
}
int main(int argc, char const *argv[])
{
    char game[N][N];
    int horizontal[N][N];
    // 0-3 horizontal
    int vertical[N][N];
    // 4-7 vertical
    int diagonal[2][N];
    // 8-9 diagonal
    int id, dots;
    char msg [256];
    int n;

    // number of games
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) { // for every game
        //  new game
        stpcpy(msg, "Draw");
        dots = 0;
        memset(horizontal,  0, N * N * sizeof(int));
        memset(vertical,    0, N * N * sizeof(int));
        memset(diagonal,    0, N * 2 * sizeof(int));

        // receive input
        for (int j = 0; j < N; ++j) {
            scanf("%s", game[j]);
            // printf("%s\n", game[j]);
            for (int k = 0; k < N; ++k) { // count values in game
                id = code(game[j][k]);
                dots += (id == DOT);
                horizontal[j][id]++;
                vertical[k][id]++;
                if (j == k) {
                    diagonal[D_1][id]++;
                } else if (j + k == N - 1) {
                    diagonal[D_2][id]++;
                }
            }
        }

        // determine winner
        for (int j = 0; j < N; ++j) {
            if (horizontal[j][O] + horizontal[j][T] == N)   {stpcpy(msg, "O won"); break;}
            if (horizontal[j][X] + horizontal[j][T] == N)   {stpcpy(msg, "X won"); break;}
            if (vertical[j][O] + vertical[j][T] == N)       {stpcpy(msg, "O won"); break;}
            if (vertical[j][X] + vertical[j][T] == N)       {stpcpy(msg, "X won"); break;}
            if (j < 2) {
                if (diagonal[j][O] + diagonal[j][T] == N)   {stpcpy(msg, "O won"); break;}
                if (diagonal[j][X] + diagonal[j][T] == N)   {stpcpy(msg, "X won"); break;}
            }
        }
        // printf("%d %d\n", diagonal[0][O], diagonal[1][O]);
        if (strstr(msg, "won") == NULL && dots > 0) {
            stpcpy(msg, "Game has not completed");
        }
        // print output
        printf("Case #%d: %s\n", i + 1, msg);
    }
    printf("\n");
    return 0;
}