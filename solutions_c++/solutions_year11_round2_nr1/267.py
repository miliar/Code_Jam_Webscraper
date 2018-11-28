#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int N;
char board[105][105];
double wp[100];
double rwp[100][100];
double owp[100];
double rowp[100][100];
double oowp[100];

double getVal(int i, int j, int level) {
    if (board[i][j] == '.')
        return 0;
    if (level == 0)
        return board[i][j] == '1';
    if (level == 1)
        return rwp[j][i];
    return owp[j];
}

int main() {
    int t, T;
    scanf("%d", &T);
    for (t = 0; t < T; t++) {
        int i, j, k;
        scanf("%d", &N);
        double dtotal;
        int total;
        for (i = 0; i < N; i++)
            scanf("%s", board[i]);
        for (i = 0; i < N; i++) {
            dtotal = 0.0;
            total = 0;
            for (j = 0; j < N; j++) {
                total+=board[i][j] != '.';
                dtotal+=getVal(i, j, 0);
            }
            if (total > 0)
                wp[i] = dtotal/total;
            for (j = 0; j < N; j++)
                rwp[i][j] = (dtotal-getVal(i, j, 0))/(total-1);
        }
        for (i = 0; i < N; i++) {
            dtotal = 0.0;
            total = 0;
            for (j = 0; j < N; j++) {
                total+=board[i][j] != '.';
                dtotal+=getVal(i, j, 1);
            }
            if (total > 0)
                owp[i] = dtotal/total;
        }
        for (i = 0; i < N; i++) {
            dtotal = 0.0;
            total = 0;
            for (j = 0; j < N; j++) {
                total+=board[i][j] != '.';
                dtotal+=getVal(i, j, 2);
            }
            if (total > 0)
                oowp[i] = dtotal/total;
        }
        printf("Case #%d:\n", t+1);
        for (i = 0; i < N; i++)
            printf("%.10lf\n", 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]);
        
    }
}
