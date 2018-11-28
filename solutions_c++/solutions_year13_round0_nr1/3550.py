//
//  A.cpp
//  Problem A. Tic-Tac-Toe-Tomek
//
//  Created by McKrisch on 2013-04-13.
//

#include <iostream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <assert.h>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)

inline void cinclean() {
    string s;
    getline(cin, s, '\n');
}

//#define TEST
//#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "A-test.in";
#else
#ifdef SMALL
const char *kIn  = "A-small.in";
const char *kOut = "A-small.out";
#else
const char *kIn  = "A-large.in";
const char *kOut = "A-large.out";
#endif
#endif

typedef set<int> cont;
typedef cont::iterator iter;
typedef cont::reverse_iterator riter;
typedef cont::const_iterator citer;
typedef cont::const_reverse_iterator criter;

enum GameState {
    NotCompleted,
    Draw,
    Xwon,
    Owon
};

char b[4][5];

inline int winTest(char c, char w) {
    if (c == w || c == 'T') return 1;
    return 0;
}

bool checkWinner(char w) {
    int cnt = 0;
    rep(i, 4) {
        cnt = 0;
        for (char *c = b[i]; *c; c++) {
            cnt += winTest(*c, w);
        }
        if (cnt == 4) return true;
        
        cnt = 0;
        rep(j, 4) {
            cnt += winTest(b[j][i], w);
        }
        if (cnt == 4) return true;
    }

    cnt = 0;
    rep(i, 4) {
        cnt += winTest(b[i][i], w);
    }
    if (cnt == 4) return true;

    cnt = 0;
    rep(i, 4) {
        cnt += winTest(b[i][3-i], w);
    }
    if (cnt == 4) return true;

    return false;
}

void workCase() {
    GameState s = Draw;
    rep (i, 4) {
        cin >> b[i];
    }

    // check NotEnded
    for (int i = 0; i < 4 && s == Draw; i++) {
        char *c = b[i];
        while (*c) {
            if (*c == '.') {
                s = NotCompleted;
                break;
            }
            c++;
        }
    }
    
    // check winner
    if (checkWinner('X')) {
        s = Xwon;
    } else if (checkWinner('O')) {
        s = Owon;
    }

    const char *res = 0;
    switch (s) {
        case NotCompleted:
            res = "Game has not completed";
            break;
        case Draw:
            res = "Draw";
            break;
        case Xwon:
            res = "X won";
            break;
        case Owon:
            res = "O won";
            break;
    }
    cout << res << endl;
}

int main(int argc, const char * argv[]) {
    if (!freopen(kIn, "rt", stdin)) {
        return 1;
    }
#if !defined(COUT) && !defined(TEST)
    if (!freopen(kOut, "wt", stdout)) {
        return 2;
    }
#endif
    int T;
    cin >> T;
    rep (i, T) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
