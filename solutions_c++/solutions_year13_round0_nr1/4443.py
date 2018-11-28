#include <algorithm>

#include <deque>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#include <iostream>

using namespace std;

int readInt() {
    string str;
    getline(cin, str);
    int i = stoi(str);
    return i;
}

bool someWin(const vector<string>& v, char pl) {
    bool d1 = true;
    bool d2 = true;

    vector<bool> hor(4, true), ver(4, true);

    for (size_t i = 0; i < 4; ++i) {
        for (size_t j = 0; j < 4; ++j) {
            if (v[i][j] != pl && v[i][j] != 'T') {
                hor[i] = false;
            }

            if (v[j][i] != pl && v[j][i] != 'T') {
                ver[i] = false;
            }
        }

        if (v[i][i] != pl && v[i][i] != 'T') {
            d1 = false;
        }

        if (v[i][4 - i - 1] != pl && v[i][4 - i - 1] != 'T') {
            d2 = false;
        }
    }

    if (d1 || d2)
        return true;

    for (size_t i = 0; i < 4; ++i) {
        if (ver[i] || hor[i]) {
            return true;
        }
    }

    return false;
}

int main(int argc, char* argv[]) {
    int numTests = readInt();
    const char* answers[] = {
        "X won",
        "O won",
        "Draw",
        "Game has not completed"
    };

    enum res {XW, OW, DR, UNK};

    for (int test = 1; test <= numTests; ++test) {
        res ans = UNK;

        vector<string> m(4);
        for (size_t i = 0; i < 4; ++i) {
            getline(cin, m[i]);
        }

        string empty;
        getline(cin, empty);

        if (someWin(m, 'X')) {
            ans = XW;
        } else if (someWin(m, 'O')) {
            ans = OW;
        } else {
            bool completed = true;
            for (const string& s: m) {
                for (char c: s) {
                    if (c == '.') {
                        completed = false;
                    }
                }
            }

            ans = completed ? DR : UNK;
        }

        cout << "Case #" << test << ": " << answers[ans] << endl;
    }

    return 0;
}
