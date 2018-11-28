#include <iostream>

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define foreach(c, i) \
    for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

void run(int caseId) {
    int rows, cols;
    cin >> rows >> cols;

    int numBlues = 0;
    char** tiles = new char*[rows];


    REP(i, rows) {
        tiles[i] = new char[cols];
        REP(j, cols) {
            char c;
            cin >> c;
            tiles[i][j] = c;
            if (c == '#') {
                ++numBlues;
            }
        }
    }

    bool possible = true;

    if (numBlues % 4 != 0) {
        possible = false;
    }

    REP(i, rows) {
        REP(j, cols) {
            char tile = tiles[i][j];
            if (tile == '#') {
                if (i + 1 < rows
                        && j + 1 < cols
                        && tiles[i][j + 1] == '#'
                        && tiles[i + 1][j] == '#'
                        && tiles[i + 1][j + 1] == '#') {
                    tiles[i][j] = '/';
                    tiles[i][j + 1] = '\\';
                    tiles[i + 1][j] = '\\';
                    tiles[i + 1][j + 1] = '/';
                }
                else {
                    possible = false;
                }
            }
        }
    }

    cout << "Case #" << (caseId + 1) << ": ";
    cout << endl;
    if (!possible) {
        cout << "Impossible";
    }
    else {
        REP(i, rows) {
            REP(j, cols) {
                cout << tiles[i][j];
            }
            cout << endl;
        }
    }
    cout << endl;
}

int main(int argc, char** argv) {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        run(i);
    }
    return 0;
}
