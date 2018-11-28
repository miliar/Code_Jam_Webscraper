#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
//#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int, pii> pip;
typedef pair<pii, int> ppi;
typedef pair<int64, int64> pii64;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
//typedef complex<double> point;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define left huyleft
#define right huyright
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "A"
#define RR 151

int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};

const int n = 4;
char a[8][8];

inline bool ok(int x, int y) {
    return x >= 0 && y >= 0 && x < n && y < n;
}

inline bool eq(char x, char y) {
    return x == y || x == 'T' || y == 'T';
}

void solve () {
    for (int i = 0; i < n; ++i)
        gets(a[i]);
    gets(new char);
    bool has_empty = false;
    bool X = false;
    bool O = false;
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < n; ++y) {
            if (a[x][y] == '.') {
                has_empty = true;
                continue;
            }
            if (a[x][y] == 'T')
                continue;
            char ch = a[x][y];
            for (int i = 0; i < 8; ++i) {
                int cnt = 0;
                for (int j = 0, tx = x, ty = y; ok(tx, ty) && j < 4; ++j, tx += dx[i], ty += dy[i]) {
                    cnt += eq(ch, a[tx][ty]);
                }
                if (cnt == 4) {
                    X |= ch == 'X';
                    O |= ch == 'O';
                }
            }
        }
    }
    if (X && O) {
        cerr << "FAIL" << endl;
        return;
    }
    if (X)
        puts("X won");
    else if (O)
        puts("O won");
    else if (has_empty)
        puts("Game has not completed");
    else
        puts("Draw");
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int T;
	char buf[32];
	gets(buf);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
