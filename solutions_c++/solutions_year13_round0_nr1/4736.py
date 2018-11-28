#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int solve() {
    char a[4][4];
    for (int i = 0; i < 4; i++)
        scanf("%c%c%c%c\n", &a[i][0], &a[i][1], &a[i][2], &a[i][3]);
    for (int i = 0; i < 4; i++) {
        bool h = 1, v = 1;
        for (int j = 0; j < 4; j++) {
            h = h && ((a[i][j] == 'T') || (a[i][j] == 'X'));
            v = v && ((a[j][i] == 'T') || (a[j][i] == 'X'));
        }
        if (h || v)
            return 1;
    }
    for (int i = 0; i < 4; i++) {
        bool h = 1, v = 1;
        for (int j = 0; j < 4; j++) {
            h = h && ((a[i][j] == 'T') || (a[i][j] == 'O'));
            v = v && ((a[j][i] == 'T') || (a[j][i] == 'O'));
        }
        if (h || v)
            return 2;
    }
    bool x1, x2, o1, o2;
    x1 = x2 = o1 = o2 = 1;
    for (int i = 0; i < 4; i++) {
        x1 = x1 && ((a[i][i] == 'T') || (a[i][i] == 'X'));
        x2 = x2 && ((a[i][3 - i] == 'T') || (a[i][3 - i] == 'X'));
        o1 = o1 && ((a[i][i] == 'T') || (a[i][i] == 'O'));
        o2 = o2 && ((a[i][3 - i] == 'T') || (a[i][3 - i] == 'O'));
    }
    if (x1 || x2)
        return 1;
    if (o1 || o2)
        return 2;
    bool f = 0;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            f = f || (a[i][j] == '.');
    if (!f)
        return 3;
    else
        return 4;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        int p = solve();
        if (p == 1)
            cout << "X won\n";
        else if (p == 2)
            cout << "O won\n";
        else if (p == 3)
            cout << "Draw\n";
        else if (p == 4)
            cout << "Game has not completed\n";
        scanf("\n");
    }
    return 0;
}
