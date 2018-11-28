#include <functional>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cmath>
#include <ctime>

#include <numeric>
#include <iomanip>
#include <complex>
#include <float.h>
#include <cfloat>

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <cstdio>

#include <cstring>
#include <string>

#include <iterator>
#include <vector>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

// typedefs
typedef long long LL;
typedef long double LD;
typedef vector < int > VI;
typedef vector < string > VS;
typedef vector < long long > VLL;
typedef vector < long double > VLD;
typedef vector < vector < int > > VVI;
typedef vector < vector < string > > VVS;
typedef vector < vector < long long > > VVLL;
typedef vector < vector < long double > > VVLD;

// defines
#define FOREACH(it, v, type) for( type::iterator it = v.begin(); it != v.end() ; ++ it )
#define FORN(i, st, en) for( int i = (int)(st); i <= (int)(en); ++ i )
#define FORDN(i, en, st) for( int i = (int)(en); i >= (int)(st); -- i )
#define ZERO(a, w) memset(a, w, sizeof(a))
#define ALL(A) A.begin(), A.end()
#define SIZE(X) ((int) (X.size()))
#define LENGTH(X) ((int) (X.length()))
#define MP(X, Y) make_pair(X, Y)
#define TWOP(X) (1<<(X))
#define TWOLP(X) (((LL)(1))<<(X))
#define CONTAINB(MASK, X) (((MASK) & TWOP(X)) != 0)
#define CONTAINLB(MASK, X) (((MASK) & TWOLP(X)) != 0)
#define MSG(X) cout << #X << " = " << X << endl;

// templates
template<class T> inline void checkMin(T A, T & B) { if(A < B) B = A; }
template<class T> inline void checkMax(T A, T & B) { if(B > A) B = A; }
template<class T> inline T sqr(T X) { return X * X; }

template<class T> inline T GCD(T A,T B)	{
    if(A < 0) return GCD(-A, B); 
    if(B < 0) return GCD(A, -B);
    return (B == 0) ? A : GCD(B, A % B);
}

template<class T> inline T LCM(T A, T B) {
    if(A < 0) return LCM(-A, B);
    if(B < 0) return LCM(A, -B);
    return A * (B / GCD(A, B));
}

template<class T> inline T euclideExt(T A, T B, T & X, T & Y) {
    if(A < 0) {
        T D = euclideExt(-A, B, X, Y);
        X = -X; 
        return D;
    }
    if(B < 0) {
        T D = euclideExt(A, -B, X, Y);
        Y = -Y;
        return D;
    }
    if(B == 0) {
        X = 1, Y = 0;
        return A;
    } else {
        T D = euclideExt(B, A % B, X, Y);
        T Z = X; 
        X = Y, Y = Z - (A / B) * Y;
        return D;
    }
}

template<class T> string toString(T N) {
    ostringstream oSS;
    oSS << N; 
    oSS.flush();
    return oSS.str();
}

// pre functions
bool isUpperCase(char C) { return C >= 'A' && C <= 'Z'; }
bool isLowerCase(char C) { return C >= 'a' && C <= 'z'; }
bool isLetter(char C) { return (C >= 'A' && C <= 'Z') || (C >= 'a' && C <= 'z'); }
bool isDigit(char C) { return C >= '0' && C <= '9'; }
char toLowerCase(char C) { return (isUpperCase(C)) ? (C + 32) : C; }
char toUpperCase(char C) { return (isLowerCase(C)) ? (C - 32) : C; }
double toDouble(string S) { double N = 0; istringstream iSS(S); iSS >> N; return N; }
long long toLongLong(string S) { LL N = 0; istringstream iSS(S); iSS >> N; return N; }
long double toLongDouble(string S) { LD N = 0; istringstream iSS(S); iSS >> N; return N; }
int toInt(string S) { int N = 0; istringstream iSS(S); iSS >> N; return N; }

// consts
const string inputFileName = "input.txt";
const string outputFileName = "output.txt";

const LD PI = acos(-1.0);
const LD EPS = 1e-7;

// variables
char board[5][5];

bool win(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4, char who) {
    char state[5];
    state[0] = board[x1][y1];
    state[1] = board[x2][y2];
    state[2] = board[x3][y3];
    state[3] = board[x4][y4];

    int O = 0, T = 0, X = 0;

    for (int i = 0; i < 4; ++ i) {
        if (state[i] == 'O') {
            ++ O;
            continue;
        }
        if (state[i] == 'X') {
            ++ X;
            continue;
        }
        if (state[i] == 'T') {
            ++ T;
            continue;
        }
        return false;
    }

    if (who == 'X' && X >= 3 && O == 0) {
        return true;
    } else if (who == 'X') {
        return false;
    }

    if (who == 'O' && O >= 3 && X == 0) {
        return true;
    } else if (who == 'O') {
        return false;
    }

    return false;
}

// main functions
void checkWin(int iTest) {

    // win: r
    for (int i = 0; i < 4; ++ i) {
        if (win(i, 0, i, 1, i, 2, i, 3, 'X')) {
            printf("Case #%d: X won", iTest);
            return;
        }

        if (win(i, 0, i, 1, i, 2, i, 3, 'O')) {
            printf("Case #%d: O won", iTest);
            return;
        }
    }

    // win: c
    for (int j = 0; j < 4; ++ j) {
        if (win(0, j, 1, j, 2, j, 3, j, 'X')) {
            printf("Case #%d: X won", iTest);
            return;
        }

        if (win(0, j, 1, j, 2, j, 3, j, 'O')) {
            printf("Case #%d: O won", iTest);
            return;
        }
    }

    // win: d1
    if (win(0, 0, 1, 1, 2, 2, 3, 3, 'X')) {
        printf("Case #%d: X won", iTest);
        return;
    }

    if (win(0, 0, 1, 1, 2, 2, 3, 3, 'O')) {
        printf("Case #%d: O won", iTest);
        return;
    }

    // win: d2
    if (win(0, 3, 1, 2, 2, 1, 3, 0, 'X')) {
        printf("Case #%d: X won", iTest);
        return;
    }

    if (win(0, 3, 1, 2, 2, 1, 3, 0, 'O')) {
        printf("Case #%d: O won", iTest);
        return;
    }

    // not completed
    for (int i = 0; i < 4; ++ i)
        for (int j = 0; j < 4; ++ j)
            if (board[i][j] == '.') {
                printf("Case #%d: Game has not completed", iTest);
                return;
            }

    // draw
    printf("Case #%d: Draw", iTest);
}


int main() {
    freopen(inputFileName.c_str(), "r", stdin);
    freopen(outputFileName.c_str(), "w", stdout);

    // Main soultion :: begin

    int nTest;

    scanf("%d\n", &nTest);

    for (int iTest = 1; iTest <= nTest; ++ iTest) {
        for (int i = 0; i < 4; ++ i) {
            for (int j = 0; j < 4; ++ j) {
                scanf("%c", &board[i][j]);
            }
            scanf("\n");
        }
        scanf("\n");

        checkWin(iTest);
        printf("\n");

    }

    // Main solution :: end

    return 0;
}

