#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "A"

const string X = "X won";
const string O = "O won";
const string D = "Draw";
const string G = "Game has not completed";
const char T = 'T';

char s[10][10];

int calcEmpty() {
    int r = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            r += s[i][j] == '.';
        }
    }
    return r;
}

bool check(char c) {
    for (int i = 0; i < 4; i++) {
        int q = 0;
        for (int j = 0; j < 4; j++) {
            q += (s[i][j] == c) || (s[i][j] == T);
        }
        if (q == 4) return true;
    }

    for (int i = 0; i < 4; i++) {
        int q = 0;
        for (int j = 0; j < 4; j++) {
            q += (s[j][i] == c) || (s[j][i] == T);
        }
        if (q == 4) return true;
    }

    int q1 = 0;
    for (int i = 0; i < 4; i++) {
        q1 += (s[i][i] == c) || (s[i][i] == T);
    }
    if (q1 == 4) return true;

    int q2 = 0;
    for (int i = 0; i < 4; i++) {
        q2 += (s[i][3-i] == c) || (s[i][3-i] == T);
    }
    if (q2 == 4) return true;

    return false;
}

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);

        for (int i = 0; i < 5; i++) {
            gets(s[i]);
        }

        int em = calcEmpty();

        if (check('X')) cout << X;
        else if (check('O')) cout << O;
        else if (em == 0) cout << D;
        else cout << G;

        printf("\n");
    }

    return 0;
}
