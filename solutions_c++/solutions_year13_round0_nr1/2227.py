#include <cstdio>
using namespace std;

char grid[5][5];
int qx, qo;
int x, o;

bool check() {
    int qx, qo;
    for (int i = 0; i < 4; i++) {
        qx = qo = 0;
        for (int j = 0; j < 4; j++) {
            if (grid[i][j] == 'X')
                qx++;
            else if (grid[i][j] == 'O')
                qo++;
            else if (grid[i][j] == 'T')
                qx++, qo++;
        }
        if (qx == 4)
            return x = 1;
        if (qo == 4)
            return o = 1;
    }
    for (int j = 0; j < 4; j++) {
        qx = qo = 0;
        for (int i = 0; i < 4; i++) {
            if (grid[i][j] == 'X')
                qx++;
            else if (grid[i][j] == 'O')
                qo++;
            else if (grid[i][j] == 'T')
                qx++, qo++;
        }
        if (qx == 4)
            return x = 1;
        if (qo == 4)
            return o = 1;
    }
    qx = qo = 0;
    for (int i = 0; i < 4; i++) {
        if (grid[i][i] == 'X')
            qx++;
        else if (grid[i][i] == 'O')
            qo++;
        else if (grid[i][i] == 'T')
            qx++, qo++;
    }
    if (qx == 4)
        return x = 1;
    if (qo == 4)
        return o = 1;
    qx = qo = 0;
    for (int i = 0; i < 4; i++) {
        if (grid[i][3-i] == 'X')
            qx++;
        else if (grid[i][3-i] == 'O')
            qo++;
        else if (grid[i][3-i] == 'T')
            qx++, qo++;
    }
    if (qx == 4)
        return x = 1;
    if (qo == 4)
        return o = 1;
    return 0;
}

void solve(int i, int j) {
    if (check())
        return;
    if (i == 4)
        return;
    int ni = i, nj = j+1;
    if (nj == 4) {
        nj = 0;
        ni++;
    }
    if (grid[i][j] != '.') {
        solve(ni, nj);
        return;
    }
    grid[i][j] = 'X';
    solve(ni, nj);
    grid[i][j] = 'O';
    solve(ni, nj);
    grid[i][j] = '.';
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        qx = qo = 0;
        for (int i = 0; i < 4; i++) {
            scanf("%s", grid[i]);
            for (int j = 0; j < 4; j++) {
                if (grid[i][j] == 'X')
                    qx++;
                else if (grid[i][j] == 'O')
                    qo++;
            }
        }
        x = o = -1;
        solve(0, 0);
        printf("Case #%d: ", t);
        if (x == -1 && o == -1)
            puts("Draw");
        else if (x == 1 && o == 1)
            puts("Game has not completed");
        else if (x == 1)
            puts("X won");
        else
            puts("O won");
    }
}
