#include <iostream>
#include <stdio.h>
using namespace std;
string s[5];
int d[4][2] = {{0 , 1}, {1, 0}, {1, 1}, {1, -1}};
bool isComplete(char v) {
    for (int i = 0; i < 4; i++) {
        for (int j =0 ; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                int x = i;
                int y = j;
                int count = 0;
                while (x < 4 && y < 4 && y >=0 &&(s[x][y] == v || s[x][y] == 'T')) {
                    count ++;
                    x += d[k][0];
                    y += d[k][1];
                }
                if (count == 4) {
                    return true;
                }
            }
        }
    }
    return false;
}
bool isFinished() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (s[i][j] == '.') {
                return false;
            }
        }
    }
    return true;
}

string judge() {
    if (isComplete('X')) {
        return "X won";
    } else if (isComplete('O')) {
        return "O won";
    } else if (!isFinished()) {
        return "Game has not completed";
    } else {
        return "Draw";
    }
}

int main() {
    int T, t = 0;
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    while(T--) {
        for (int i = 0; i < 4; i++) {
            cin>>s[i];
        }
        string res = judge();
        cout << "Case #" << ++t << ": " << res << endl;
    }
}

