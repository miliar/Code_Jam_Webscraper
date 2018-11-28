#include <iostream>
#include <stdio.h>

using namespace std;

char c[4][4];

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int T;
    cin >> T;
    for(int k = 1; k <= T; k++) {
        bool f = 0;
        cout << "Case #" << k << ": ";
        for(int i = 0; i < 4; i++)
            cin >> c[i];

        for(int i = 0, j = 0; i < 4; i++) {
            char x;
            j = 0;
            while(j < 3 && (c[i][j] == c[i][j + 1] || c[i][j + 1] == 'T' || c[i][j] == 'T')) {
                j++;
                if(c[i][j] != 'T')
                    x = c[i][j];
            }
            if(j == 3 && x != '.') {
                cout << x << " won" << endl;
                f = 1;
                break;
            }
        }
        if(f) continue;
        for(int i = 0, j = 0; j < 4; j++) {
            char x;
            i = 0;
            while(i < 3 && (c[i + 1][j] == c[i][j] || c[i + 1][j] == 'T' || c[i][j] == 'T')) {
                i++;
                if(c[i][j] != 'T')
                    x = c[i][j];
            }
            if(i == 3 && x != '.') {
                cout << x << " won" << endl;
                f = 1;
                break;
            }
        }
        if(f) continue;
        int i = 0, j = 0;
        char x;
        while(i < 3 && (c[i + 1][j + 1] == c[i][j] || c[i + 1][j + 1] == 'T' || c[i][j] == 'T')) {
            i++;
            j++;
            if(c[i][j] != 'T')
                x = c[i][j];
        }
        if(i == 3 && x != '.') {
            cout << x << " won" << endl;
            f = 1;
        }
        if(f) continue;
        i = 0; j = 3;
        while(i < 3 && (c[i + 1][j - 1] == c[i][j] || c[i + 1][j - 1] == 'T' || c[i][j] == 'T')) {
            i++;
            j--;
            if(c[i][j] != 'T')
                x = c[i][j];
        }
        if(i == 3 && x != '.') {
            cout << x << " won" << endl;
            f = 1;
        }
        if(f) continue;
        for(int i = 0; i < 4 && !f; i++)
            for(int j = 0; j < 4 && !f; j++)
                f = f || c[i][j] == '.';
        if(f)
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;
    }
    return 0;
}
