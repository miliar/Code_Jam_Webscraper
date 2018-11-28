#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

char a[5][5];
vector<pair<int, int> > b;

int main() {

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T, cnt = 0;
    cin >> T;
    while (T > 0) {
        ++cnt;
        cout << "Case #" << cnt << ": ";
        bool done = true;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++) {
                cin >> a[i][j];
                if (a[i][j] == '.') done = false;
            }
        b.clear();
        for (int i = 1; i <= 4; i++) {
            pair<int, int> t;
            for (int j = 1; j <= 4; j++) {
                if (a[i][j] == 'X' || a[i][j] == 'T') ++t.first;
                if (a[i][j] == 'O' || a[i][j] == 'T') ++t.second;
            }
            b.push_back(t);
        }
        for (int j = 1; j <= 4; j++) {
            pair<int, int> t;
            for (int i = 1; i <= 4; i++) {
                if (a[i][j] == 'X' || a[i][j] == 'T') ++t.first;
                if (a[i][j] == 'O' || a[i][j] == 'T') ++t.second;
            }
            b.push_back(t);
        }
        b.push_back(make_pair(0, 0));
        for (int i = 1; i <= 4; i++) {
            if (a[i][i] == 'X' || a[i][i] == 'T') ++(b.back()).first;
            if (a[i][i] == 'O' || a[i][i] == 'T') ++(b.back()).second;
        }
        b.push_back(make_pair(0, 0));
        for (int i = 1; i <= 4; i++) {
            if (a[i][5 - i] == 'X' || a[i][5 - i] == 'T') ++(b.back()).first;
            if (a[i][5 - i] == 'O' || a[i][5 - i] == 'T') ++(b.back()).second;
        }
        bool draw = true;
        for (int i = 0; i < b.size(); i++)
            if (b[i].first == 4) {
                cout << "X won" << endl;
                draw = false;
                break;
            }
            else if (b[i].second == 4) {
                cout << "O won" << endl;
                draw = false;
                break;
            }
        if (draw)
            if (done)
                cout << "Draw" << endl;
            else
                cout << "Game has not completed" << endl;
        --T;
    }
}
