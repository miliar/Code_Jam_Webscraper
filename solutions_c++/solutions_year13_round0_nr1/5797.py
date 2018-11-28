#include <iostream>
#include <cstdio>

char map[5][5];

bool win(char p) {
    bool flag;
    for (int i = 0; i < 4; i++) {
        flag = true;
        for (int j = 0; j < 4; j++) {
            if (map[i][j] != p && map[i][j] != 'T') flag = false;
        }
        if (flag) return true;
        flag = true;
        for (int j = 0; j < 4; j++) {
            if (map[j][i] != p && map[j][i] != 'T') flag = false;
        }
        if (flag) return true;
    }
    flag = true;
    for (int i = 0; i < 4; i++) {
        if (map[i][i] != p && map[i][i] != 'T') flag = false;
    }
    if (flag) return true;
    flag = true;
    for (int i = 0; i < 4; i++) {
        if (map[i][3 - i] != p && map[i][3 - i] != 'T') flag = false;
    }
    if (flag) return true;
    return false;
}

void proc() {
    if (win('X')) {
        printf("X won\n");
        return;
    }
    if (win('O')) {
        printf("O won\n");
        return;
    }
    int count = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (map[i][j] == '.') count++;
        }
    }
    if (count == 0) {
        printf("Draw\n");
        return;
    } else {
        printf("Game has not completed\n");
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    scanf("%d\n", &tc);
    for (int t = 1; t <= tc; t++) {
        for (int i = 0; i < 4; i ++) {
            scanf("%s", map[i]);
        }
        scanf("\n");
        printf("Case #%d: ", t);
        proc();
    }    
    return 0;
}
