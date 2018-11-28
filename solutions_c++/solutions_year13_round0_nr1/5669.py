#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

char a[5][5];
int hx[5], vx[5];
int hy[5], vy[5];

void solve () {
    bool end = 1;
    for (int i = 0; i < 4; i++) {
        char x = a[i][0];
        if (x == 'T') x = a[i][1];
        if (x == '.') x = '@';
        for (int j = 1; j < 4; j++) { 
            if (a[i][j] == '.') end = 0;
            if (a[i][j] == 'T') continue;
            if (x != a[i][j]) x = '@';
        }
        if (x != '@') {
            cout << x << " won\n";
            return;
        }
        x = a[0][i];
        if (x == 'T') x = a[1][i];
        if (x == '.') x = '@';
        for (int j = 1; j < 4; j++) {
            if (a[j][i] == 'T') continue;
            if (x != a[j][i]) x = '@';
        }
        if (x != '@') {
            cout << x << " won\n";
            return;
        }
    }
    char x = a[0][0];
    if (x == 'T') x = a[1][1];
    if (x == '.') x = '@';
    for (int i = 1; i < 4; i++) {
        if (a[i][i] == 'T') continue;
        if (a[i][i] != x) x = '@';
    }
    if (x != '@') {
        cout << x << " won\n";
        return;
    }
    x = a[0][3];
    if (x == 'T') x = a[1][2];
    if (x == '.') x = '@';
    for (int i = 1; i < 4; i++) {
        if (a[i][3-i] == 'T') continue;
        if (a[i][3-i] != x) x = '@';
    }
    if (x != '@') {
        cout << x << " won\n";
        return;
    }
    if (end) cout << "Draw";
    else     cout << "Game has not completed";
    cout << endl;
}

int main ()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        for (int i = 0; i < 4; i++)
                scanf ("%s", a[i]);
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}

