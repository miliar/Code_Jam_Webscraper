#include <iostream>
#include <string>
using namespace std;
string grid[50];
int R,C;
int T;

bool paint(int i, int j) {
    if (i >= R-1 || j >= C-1) {
        return false;
    }
    if (!(grid[i][j] == '#'  && grid[i+1][j] == '#'
                && grid[i][j+1] == '#' && grid[i+1][j+1] == '#'))
        return false;
    grid[i][j] = '/';
    grid[i+1][j] = 'Z'+2;
    grid[i][j+1] = 'Z'+2;
    grid[i+1][j+1] = '/';
    return true;
}

bool solve() {
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (grid[i][j] == '#') {
                if (!paint(i,j)) {
                    return false;
                }
            }
        }   
    }
    return true;
}

int main() {
    cin >> T;
    int cas = 0;
    while (T--) {
        ++cas;
        cin >> R >> C; cin.ignore();
        for (int i = 0; i < R; ++i) {
            getline(cin,grid[i]);
        }

        cout << "Case #" << cas << ":\n";
        if (solve()) {
            for (int i = 0; i < R; ++i) {
                cout << grid[i] << "\n";
            }   
        } else {
            cout << "Impossible\n";
        }
    }
}
