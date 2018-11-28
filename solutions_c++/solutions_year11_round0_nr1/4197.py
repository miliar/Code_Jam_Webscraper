
//  Copyright(c) 2009-2011, all rights reserved.
//  written by ZHUMAZHANOV ADLET.

#include <iostream>
#include <iterator>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <bitset>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#define FILE_NAME       "a"
#define SZ(v)           static_cast<int>(v.size())

#define sqr(x)          ((x) * (x))
#define all(v)          v.begin(), v.end()

#define Assert(cond, msg) {\
    if (! (cond)) {\
        fprintf(stderr, "%s:%d: Error: %s", __FILE__, __LINE__, msg);\
        exit(EXIT_FAILURE);\
    }\
}

#define loop(i, a, b)   for (int i = static_cast<int>(a); i <= static_cast<int>(b); ++ i)
#define clr(a, b)       memset(a, (b), sizeof(a))

#define printx(x)       cerr << #x << " = " << x << "\n"
#define sign(a)         ((a) > 0 ? +1 : (a) < 0 ? -1 : 0)

#define forn(i, n)      loop(i, 0, n - 1)
#define forv(i, v)      forn(i, SZ(v))

typedef unsigned int uint;
typedef unsigned long long ui64;

typedef long long i64;

using namespace std;

int n;
pair<char, int> a[100];

int T;

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);

    Assert (freopen(FILE_NAME".in", "r", stdin), "cannot creat input-file");
    Assert (freopen(FILE_NAME".out", "w", stdout), "cannot creat output-file");

    cin >> T;

    int cur_o;
    int cur_b;

    int pos_o;
    int pos_b;

    int timer;

    loop(test, 1, T) {
        cin >> n;
        forn(i, n) cin >> a[i].first >> a[i].second;

        cur_o = 1;
        cur_b = 1;

        timer = 0;
        
        forn(i, n) {
            pos_o = 0;
            pos_b = 0;
            forn(j, n) if (i <= j && a[j].first == 'O') {
                pos_o = a[j].second;
                break;
            }
            forn(j, n) if (i <= j && a[j].first == 'B') {
                pos_b = a[j].second;
                break;
            }
            if (a[i].first == 'O') {
                while (cur_o != pos_o) {
                    if (cur_o < pos_o) {
                        cur_o ++;
                    } else {
                        cur_o --;
                    }
                    if (cur_b < pos_b) {
                        cur_b ++;
                    } else if (cur_b > pos_b) {
                        cur_b --;
                    }
                    timer ++;
                }
                timer ++;
                if (cur_b < pos_b) {
                    cur_b ++;
                } else if (cur_b > pos_b) {
                    cur_b --;
                }
            } else {
                while (cur_b != pos_b) {
                    if (cur_b < pos_b) {
                        cur_b ++;
                    } else {
                        cur_b --;
                    }
                    if (cur_o < pos_o) {
                        cur_o ++;
                    } else if (cur_o > pos_o) {
                        cur_o --;
                    }
                    timer ++;
                }
                timer ++;
                if (cur_o < pos_o) {
                    cur_o ++;
                } else if (cur_o > pos_o) {
                    cur_o --;
                }
            }
        }
        cout << "Case #" << test << ": " << timer << "\n";
    }

    return EXIT_SUCCESS;
}
