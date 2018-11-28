#include <cassert>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

enum Status { X_WON, O_WON, DRAW, NOT_COMPLETED };

vector< string > field;

Status solve() {
    static vector< vector< pair< int, int > > > groups = {
        {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
        {{1, 0}, {1, 1}, {1, 2}, {1, 3}},
        {{2, 0}, {2, 1}, {2, 2}, {2, 3}},
        {{3, 0}, {3, 1}, {3, 2}, {3, 3}},

        {{0, 0}, {1, 0}, {2, 0}, {3, 0}},
        {{0, 1}, {1, 1}, {2, 1}, {3, 1}},
        {{0, 2}, {1, 2}, {2, 2}, {3, 2}},
        {{0, 3}, {1, 3}, {2, 3}, {3, 3}},

        {{0, 0}, {1, 1}, {2, 2}, {3, 3}},
        {{0, 3}, {1, 2}, {2, 1}, {3, 0}},
    };

    bool completed = true;
    for (auto &group : groups) {
        int x_count = 0,
            o_count = 0;
        for (auto &cell : group)
            switch (field[cell.first][cell.second]) {
                case '.':
                    completed = false;
                    break;
                case 'X':
                    x_count++;
                    break;
                case 'O':
                    o_count++;
                    break;
                case 'T':
                    x_count++;
                    o_count++;
                    break;
            }
        if (x_count == 4)
            return X_WON;
        if (o_count == 4)
            return O_WON;
    }
    return completed ? DRAW : NOT_COMPLETED;
}

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        field.clear();
        field.resize(4);
        cin.ignore();
        for (auto &row : field)
            getline(cin, row);
        auto ans = solve();
        cout << "Case #" << i << ": ";
        switch (ans) {
            case X_WON:
                cout << "X won";
                break;
            case O_WON:
                cout << "O won";
                break;
            case DRAW:
                cout << "Draw";
                break;
            case NOT_COMPLETED:
                cout << "Game has not completed";
                break;
        }
        cout << "\n";
    }
    return 0;
}
