#include <cstdio>
#include <cstring>
//#include <string>
//#include <vector>
//#include <deque>
//#include <set>
//#include <map>
//#include <numeric>
//#include <algorithm>
//#include <functional>
using namespace std;

#define FOR(i, n) for (i = 0; i < (n); ++i)
#define FOR1(i, n) for (i = 1; i <= (n); ++i)
#define ROF(i, n) for (i = (n) - 1; i >= 0; --i)
#define ROFN(i, n) for (i = (n); i > 0; --i)
//#define debug(what...) fprintf(stderr, what) 
#define debug(what...)

typedef long long llong;
typedef unsigned long long ullong;

void redirect() {
//    freopen("log", "wt", stderr);
//    freopen("B-test.in", "rt", stdin);
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("B-small-attempt0.out", "wt", stdout);
//    freopen("B-large.in", "rt", stdin);
//    freopen("B-large.out", "wt", stdout);
}

//const ullong MOD = 1000000007;

enum {
    NOOP = 0,
    NORTH,
    WEST,
    EAST,
    SOUTH
};

int offset_i[] = { 0, -1, 0, 0, 1};
int offset_j[] = { 0, 0, -1, 1, 0};

short int map[100][100];
char flow[100][100], label[100][100];
char label_char;

char add_label(int i, int j) {
    debug("add_label: %d %d ", i, j);
    int ch;
    ch = label[i][j];
    if (!ch) {
        if (flow[i][j] == NOOP) {
            ch = label_char++;
        }
        else {
            int k = flow[i][j];
            ch = add_label(i + offset_i[k], j + offset_j[k]);
        }
        label[i][j] = ch;
    }
    debug("%c\n", ch);
    return ch;
}

int alt(int i, int j) {
    int k = flow[i][j];
    return map[i + offset_i[k]][j + offset_j[k]];
}

int main() {
    int tn, tt;
    int h, w;
    int i, j, k;
    int x, y;
    redirect();
    scanf("%d", &tn);
    FOR1(tt, tn) {
        scanf("%d%d", &h, &w);
        debug("Case #%d:\n", tt);
        debug("phase 1:\n");
        FOR(i, h) {
            FOR(j, w) {
                scanf("%d", &map[i][j]);
                flow[i][j] = NOOP;
                label[i][j] = '\0';
                if (i > 0) {
                    x = alt(i, j);
                    y = alt(i-1, j);
                    debug("alt(%d, %d) = %d\t", i, j, x);
                    debug("alt(%d, %d) = %d\n", i-1, j, y);
                    if (x > map[i-1][j])
                        flow[i][j] = NORTH;
                    else if (y > map[i][j])
                        flow[i-1][j] = SOUTH;
                    else {
                        //if (flow[i-1][j] > SOUTH)
                        //    flow[i-1][j] = SOUTH;
                        if (flow[i][j] > NORTH)
                            flow[i][j] = NORTH;
                    }
                    debug("dir(%d, %d) = %d\t", i, j, flow[i][j]);
                    debug("dir(%d, %d) = %d\n", i-1, j, flow[i-1][j]);
                }
                if (j > 0) {
                    x = alt(i, j);
                    y = alt(i, j-1);
                    debug("alt(%d, %d) = %d\t", i, j, x);
                    debug("alt(%d, %d) = %d\n", i, j-1, y);
                    if (x > map[i][j-1])
                        flow[i][j] = WEST;
                    else if (y > map[i][j])
                        flow[i][j-1] = EAST;
                    else {
                        if (flow[i][j-1] > EAST)
                            flow[i][j-1] = EAST;
                        if (flow[i][j] > WEST)
                            flow[i][j] = WEST;
                    }
                    debug("dir(%d, %d) = %d\t", i, j, flow[i][j]);
                    debug("dir(%d, %d) = %d\n", i, j-1, flow[i][j-1]);
                }
            }
        }
        debug("phase 2:\n");
        label_char = 'a';
        FOR(i, h) {
            FOR(j, w) {
                if (!label[i][j]) {
                    add_label(i, j);
                }
            }
        }
        printf("Case #%d:\n", tt);
        FOR(i, h) {
            FOR(j, w) {
                putchar(label[i][j]);
                putchar(j < w - 1 ? ' ' : '\n');
            }
        }
    }

    return 0;
}
