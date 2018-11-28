#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    vector < string > field;
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int r, c;
        cin >> r >> c;
        field.resize(r);
        for (int i = 0; i < r; i++) {
            cin >> field[i];
        }
        
        for (int i = 0; i < r - 1; i++) {
            for (int j = 0; j < c - 1; j++) {
                if (field[i][j] == '#' && field[i + 1][j] == '#' && field[i][j + 1] == '#' && field[i + 1][j + 1] == '#') {
                    field[i][j] = '/';  field[i][j + 1] = '\\';
                    field[i + 1][j] = '\\'; field[i + 1][j + 1] = '/';
                }
            }
        }
        bool not_ok = false;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                not_ok |= (field[i][j] == '#');
            }
        }
        
        if (not_ok) {
            cout << "Case #" << tc << ":\nImpossible\n";
        } else {
            cout << "Case #" << tc << ":\n";
            for (int i = 0; i < r; i++) {
                cout << field[i] << endl;
            }
        }
    }
    return 0;
}
