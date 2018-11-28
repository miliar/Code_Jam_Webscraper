
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
int a[15];

int T;

int bestAnswer;
int answer;

bool bit(int n, int i) {
    return n & (1 << i);
}

int sum(int a, int b) {
    return a ^ b;
}

void solve() {
    int N = 1 << n;
    int bits;

    bestAnswer = -1;

    int sum1;
    int sum2;

    forn(mask, N) {
        bits = 0;
        sum1 = 0;
        sum2 = 0;
        forn(i, n) if (bit(mask, i)) {
            bits ++;
            sum1 = sum(sum1, a[i]);
        } else {
            sum2 = sum(sum2, a[i]);
        }
        if (0 < bits && bits < n && sum1 == sum2) {
            answer = 0;
            forn(i, n) if (bit(mask, i)) answer += a[i];
            bestAnswer = max(bestAnswer, answer);
        }
    }
}

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);

    Assert (freopen(FILE_NAME".in", "r", stdin), "cannot creat input-file");
    Assert (freopen(FILE_NAME".out", "w", stdout), "cannot creat output-file");

    cin >> T;

    loop(test, 1, T) {
        cin >> n;
        forn(i, n) cin >> a[i];
        solve();
        cout << "Case #" << test << ": ";
        if (bestAnswer == -1) {
            cout << "NO";
        } else {
            cout << bestAnswer;
        }
        cout << "\n";
    }

    return EXIT_SUCCESS;
}
