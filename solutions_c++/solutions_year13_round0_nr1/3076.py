#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool checkWinCondition(char map[4][4], char c)
{
    for (int i = 0; i < 4; ++i) {
        bool match = true;
        for (int j = 0; j < 4; ++j) {
            if (map[i][j] != c && map[i][j] != 'T') {
                match = false;
                break;
            }
        }
        if (match) return true;
    }

    for (int j = 0; j < 4; ++j) {
        bool match = true;
        for (int i = 0; i < 4; ++i) {
            if (map[i][j] != c && map[i][j] != 'T') {
                match = false;
                break;
            }
        }
        if (match) return true;
    }

    bool match = true;
    for (int i = 0; i < 4; ++i) {
        if (map[i][i] != c && map[i][i] != 'T') {
            match = false;
            break;
        }
    }
    if (match) return true;

    match = true;
    for (int i = 0; i < 4; ++i) {
        if (map[i][3-i] != c && map[i][3-i] != 'T') {
            match = false;
            break;
        }
    }
    if (match) return true;

    return false;
}

bool checkNotComplete(char map[4][4])
{
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (map[i][j] == '.') return true;
        }
    }

    return false;
}

void solve(int caseNum)
{
    // SOLVE TASK HERE!

    // read input
    char map[4][4];
    for (int i = 0; i < 4; ++i) {
        scanf("%s\n", map[i]);
    }
    scanf("\n");

    if (checkWinCondition(map, 'X')) {
        printf("Case #%d: X won\n", caseNum);
        return;
    }

    if (checkWinCondition(map, 'O')) {
        printf("Case #%d: O won\n", caseNum);
        return;
    }

    if (checkNotComplete(map)) {
        printf("Case #%d: Game has not completed\n", caseNum);
    } else {
        printf("Case #%d: Draw\n", caseNum);
    }
}

int main()
{
    int T;
    scanf("%d\n", &T);

    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        solve(caseNum);
    }

    return 0;
}

