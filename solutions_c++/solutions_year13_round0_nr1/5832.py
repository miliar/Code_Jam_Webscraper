#include<cstdio>

using namespace std;

char data[4][4];

char check() {
    char row[4];
    char col[4];
    char skew[2];
    bool hasDot = false;
    for (int i = 0; i < 4; i++) {
        row[i] = data[i][0];
        if (row[i] == 'T')
            row[i] == data[i][1];
        if (row[i] == '.')
            continue;
        for (int j = 0; j < 4; j++) {
            if (data[i][j] == 'T' || data[i][j] == row[i])
                continue;
            else
                row[i] = '.';
        }
        if (row[i] != '.')
            return row[i];
    }

    for (int j = 0; j < 4; j++) {
        col[j] = data[0][j];
        if (col[j] == 'T')
            col[j] == data[0][j];
        if (col[j] == '.')
            continue;
        for (int i = 0; i < 4; i++) {
            if (data[i][j] == 'T' || data[i][j] == col[j])
                continue;
            else
                col[j] = '.';
        }
        if (col[j] != '.')
            return col[j];
    }

    
    skew[0] = data[0][0];
    if (skew[0] == 'T')
        skew[0] = data[1][1];
    if ((skew[0] != data[2][2] && data[2][2] != 'T') ||
            (data[3][3] != skew[0] && data[3][3] != 'T') ||
            (skew[0] != data[1][1] && data[1][1] != 'T'))
        skew[0] = '.';

    skew[1] = data[3][0];
    if (skew[1] == 'T')
        skew[1] = data[2][1];
    if ((skew[1] != data[2][1] && data[2][2] != 'T') ||
            (data[0][3] != skew[1] && data[0][3] != 'T') ||
            (skew[1] != data[1][2] && data[1][2] != 'T'))
        skew[1] = '.';

    if (skew[0] != '.')
        return skew[0];
    if (skew[1] != '.')
        return skew[1];

    for (int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if (data[i][j] == '.')
                hasDot = true;
            continue;
        }
        if (hasDot)
            continue;
    }

    if (hasDot)
        return '.';
    else
        return 'D';
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%s", data[0]);
        scanf("%s", data[1]);
        scanf("%s", data[2]);
        scanf("%s", data[3]);
        char res = check();
        switch(res) {
            case 'X':
                printf("Case #%d: X won\n", i+1);
                break;
            case 'O':
                printf("Case #%d: O won\n", i+1);
                break;
            case '.':
                printf("Case #%d: Game has not completed\n", i+1);
                break;
            case 'D':
                printf("Case #%d: Draw\n", i+1);
                break;
        }
    }
    return 0;
}
