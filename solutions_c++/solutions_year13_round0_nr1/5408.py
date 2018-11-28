#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cctype>

using namespace std;

char b[8][8];

char verticals() {
    for (int j = 0; j < 4; ++j) {
        char winner = b[0][j];

        if (b[0][j] == '.') continue;
        if (b[0][j] == 'T') winner = b[1][j];
        if (winner == '.') continue;

        bool ok = true;
        for (int i = 1; i < 4 && ok; ++i) {
            if (b[i][j] != winner && b[i][j] != 'T') ok = false;
        }

        if (ok) return winner;
    }

    return 0;
}

char horizontals() {
    for (int i = 0; i < 4; ++i) {
        char winner = b[i][0];

        if (b[i][0] == '.') continue;
        if (b[i][0] == 'T') winner = b[i][1];
        if (winner == '.') continue;

        bool ok = true;
        for (int j = 1; j < 4 && ok; ++j) {
            if (b[i][j] != winner && b[i][j] != 'T') ok = false;
        }

        if (ok) return winner;
    }

    return 0;
}

char diagonals(int i, int j, int ii, int ij) {
    if (b[i][j] == '.') return 0;

    char winner = b[i][j];
    if (b[i][j] == 'T') winner = b[i+ii][j+ij];

    bool ok = true;
    for (i += ii, j += ij; i < 4 && ok; i += ii, j += ij) {
        if (b[i][j] != winner && b[i][j] != 'T') ok = false;
    }

    if (ok) return winner;
    return 0;
}

int main () {
    int casos;
    scanf ("%d", &casos);

    for (int caso = 1; caso <= casos; ++caso) {
        bool full = true;
        char winner = 0;

        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf (" %c", &b[i][j]);
                
                if (b[i][j] == '.')
                    full = false;
            }
        }

        winner = verticals();
        if (winner) {
            printf ("Case #%d: %c won\n", caso, winner);
            continue;
        }

        winner = horizontals();
        if (winner) {
            printf ("Case #%d: %c won\n", caso, winner);
            continue;
        }

        winner = diagonals(0, 0, 1, 1);
        if (winner) {
            printf ("Case #%d: %c won\n", caso, winner);
            continue;
        }

        winner = diagonals(0, 3, 1, -1);
        if (winner) {
            printf ("Case #%d: %c won\n", caso, winner);
            continue;
        }

        if (full) {
            printf ("Case #%d: Draw\n", caso);
        } else {
            printf ("Case #%d: Game has not completed\n", caso);
        }
    }

    return 0;
}

