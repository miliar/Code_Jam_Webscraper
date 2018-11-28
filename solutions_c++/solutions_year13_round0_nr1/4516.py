#include <cstdio>
#include <string>
#define infile "tictactoe.in"
#define outfile "tictactoe.out"

using namespace std;

char h[13][13];
string res;

void read() {
    for (int i = 0; i < 4; ++i) {
        scanf("%s\n", h[i]);
    }
}

bool check(int ls, int cs, int ld, int cd, char ch) {

    for (int i = 0; i < 4; ++i, ls += ld, cs += cd) {
        if (h[ls][cs] != ch && h[ls][cs] != 'T') {
            return false;
        }
    }

    return true;
}

bool isWinner(char c) {

    for (int i = 0; i < 4; ++i) {
        if (check(i, 0, 0, 1, c)) { //win line i
            return true;
        }
        if (check(0, i, 1, 0, c)) { //win column i
            return true;
        }
    }

    if (check(0, 0, 1, 1, c)) { //first diagonal
        return true;
    }

    if (check(0, 3, 1, -1, c)) { //second diagonal
        return true;
    }

    return false;
}

bool isFull() {

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (h[i][j] == '.') {
                return false;
            }
        }
    }

    return true;
}

void solve() {
    res = "Game has not completed";

    if (isWinner('X')) {
        res = "X won";
    } else if(isWinner('O')) {
        res = "O won";
    } else if(isFull()) {
        res = "Draw";
    }
}

void write(int test) {
    printf("Case #%d: %s\n", test, res.c_str());
}

int main() {
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);

    int n;
    scanf("%d\n", &n);

    for (int i = 0; i < n; ++i) {
        read();
        solve();
        write(i+1);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
