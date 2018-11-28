#include <iostream>
using namespace std;

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        int r, c;
        cin >> r >> c;
        char b[r][c];
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                cin >> b[i][j];
        bool can = true;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                if (b[i][j] == '#') {
                    if (j + 1 >= c || i + 1 >= r)
                        can = false;
                    if (can && (b[i][j + 1] != '#' || b[i + 1][j] != '#' || b[i + 1][j + 1] != '#'))
                        can = false;
                    if (can) {
                        b[i][j] = '/';
                        b[i][j + 1] = '\\';
                        b[i + 1][j] = '\\';
                        b[i + 1][j + 1] = '/';
                    }
                }
        cout << "Case #" << cc << ":\n";
        if (!can)
            cout << "Impossible\n";
        else {
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++)
                    cout << b[i][j];
                cout << "\n";
            }
        }
    }
}
