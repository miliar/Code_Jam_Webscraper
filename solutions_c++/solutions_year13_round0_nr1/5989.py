#include <iostream>
#include <cstdio>
using namespace std;

int nr_case = 1;
char board[10][10];

char check_row() {
    int count[3];

    for (int i = 0; i < 4; i++) {
        count[0] = count[1] = count[2] = 0;
        for (int j = 0; j < 4; j++)
            switch (board[i][j]) {
                case 'X':count[0]++; break;
                case 'O':count[1]++; break;
                case 'T':count[2]++; break;
            }
        if ((count[0] == 3 && count[2] == 1) || count[0] == 4)
            return 'X';
        if ((count[1] == 3 && count[2] == 1) || count[1] == 4)
            return 'O';
    }

    return 'U';
}

char check_column() {
    int count[3];

    for (int j = 0; j < 4; j++) {
        count[0] = count[1] = count[2] = 0;
        for (int i = 0; i < 4; i++)
            switch (board[i][j]) {
                case 'X':count[0]++; break;
                case 'O':count[1]++; break;
                case 'T':count[2]++; break;
            }
        if ((count[0] == 3 && count[2] == 1) || count[0] == 4)
            return 'X';
        if ((count[1] == 3 && count[2] == 1) || count[1] == 4)
            return 'O';
    }

    return 'U';
}

char check_diagonal() {
    int i, j;
    int count[3];

    i = 0;
    j = 0;
    count[0] = count[1] = count[2] = 0;
    while (true) {
        switch (board[i][j]) {
                case 'X':count[0]++; break;
                case 'O':count[1]++; break;
                case 'T':count[2]++; break;
            }
        i++;
        j++;
        if (i == 4)
            break;
    }
    if ((count[0] == 3 && count[2] == 1) || count[0] == 4)
        return 'X';
    if ((count[1] == 3 && count[2] == 1) || count[1] == 4)
        return 'O';

    i = 0;
    j = 3;
    count[0] = count[1] = count[2] = 0;
    while (true) {
        switch (board[i][j]) {
                case 'X':count[0]++; break;
                case 'O':count[1]++; break;
                case 'T':count[2]++; break;
            }
        i++;
        j--;
        if (i == 4)
            break;
    }
    if ((count[0] == 3 && count[2] == 1) || count[0] == 4)
        return 'X';
    if ((count[1] == 3 && count[2] == 1) || count[1] == 4)
        return 'O';
    return 'U';
}

bool isFinished() {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (board[i][j] == '.')
                return false;
    return true;
}

void output(char res) {
    if (res == 'X' || res == 'O')
        printf("Case #%d: %c won\n", nr_case, res);
    if (res == 'D')
        printf("Case #%d: Draw\n", nr_case);
    if (res == 'N')
        printf("Case #%d: Game has not completed\n", nr_case);
    nr_case++;
}

void solve() {
    char res;

    res = check_row();
    if (res != 'U') {
        output(res);
        return;
    }
    res = check_column();
    if (res != 'U') {
        output(res);
        return;
    }
    res = check_diagonal();
    if (res != 'U') {
        output(res);
        return;
    }
    if (isFinished()) {
        res = 'D';
        output(res);
        return;
    }
    res = 'N';
    output(res);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;

    scanf("%d", &T);
    while (T--) {
        for (int i = 0; i < 4; i++)
            scanf("%s", board[i]);
        solve();
    }
    return 0;
}
