#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <sstream>
using namespace std;



int main (int argc, char const *argv[]) {

    int T;
    cin >> T;
    map<char, char> m;
    m['O'] = 'O';
    m['X'] = 'X';
    m['T'] = 'T';
    m['.'] = '.';
    for (int t = 0; t != T; ++t) {
        vector<vector<char> > v(10, vector<char>(10, '.'));
        for (int i = 0; i != 4; ++i) {
            for (int j = 0; j != 4; ++j) {
                cin >> v[i+3][j+3];
            }
        }
        // for (int i = 3; i != 7; ++i) {
        //     for (int j = 3; j != 7; ++j) {
        //         cout << v[i][j] << " ";
        //     }
        //     cout << endl;
        // }
        char c;
        char win = '.';
        int count = 0;
        for (int i = 3; i != 7; ++i) {
            for (int j = 3; j != 7; ++j) {
                c = v[i][j];
                if (c == '.') {
                    ++count;
                    continue;
                }
                if (c == 'T') {
                    continue;
                }
                m['T'] = c;
                // horizontal
                if (m[v[i][j+1]] == c && m[v[i][j+2]] == c && m[v[i][j+3]] == c) {
                    win = c;
                    i = 6;
                    break;
                }
                if (m[v[i][j-1]] == c && m[v[i][j-2]] == c && m[v[i][j-3]] == c) {
                    win = c;
                    i = 6;
                    break;
                }
                // vertical
                if (m[v[i+1][j]] == c && m[v[i+2][j]] == c && m[v[i+3][j]] == c) {
                    win = c;
                    i = 6;
                    break;
                }
                if (m[v[i-1][j]] == c && m[v[i-2][j]] == c && m[v[i-3][j]] == c) {
                    win = c;
                    i = 6;
                    break;
                }
                // diagnal
                if (m[v[i+1][j+1]] == c && m[v[i+2][j+2]] == c && m[v[i+3][j+3]] == c) {
                    win = c;
                    i = 6;
                    break;
                }
                if (m[v[i+1][j-1]] == c && m[v[i+2][j-2]] == c && m[v[i+3][j-3]] == c) {
                    win = c;
                    i = 6;
                    break;
                }
            }
        }
        cout << "Case #" << t+1 << ": ";
        if (win == '.' && count == 0) {
            cout << "Draw" << endl;
        } else if (win == '.' && count != 0) {
            cout << "Game has not completed" << endl;
        } else {
            cout << win << " won" << endl;
        }
    }
    return 0;
}
