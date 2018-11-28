
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

int T;
int n;

int l;
int h;

int a[100];

bool check(int answer) {
    forn(i, n) if ((a[i] % answer != 0) && (answer % a[i] != 0)) {
        return false;
    }
    return true;
}

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int lcm(int a, int b) {
    return a * (b / gcd(a, b));
}

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);

    Assert (freopen(FILE_NAME".in", "r", stdin), "cannot creat input-file");
    Assert (freopen(FILE_NAME".out", "w", stdout), "cannot creat output-file");

    cin >> T;

    loop(test, 1, T) {

        cin >> n
            >> l >> h;

        forn(i, n) cin >> a[i];
        int answer;

        for (answer = l; answer <= h; ++ answer) {
            if (check(answer)) break;
        }

        cout << "Case #" << test << ": ";
        if (answer <= h) {
            cout << answer;
        } else {
            cout << "NO";
        }
        cout << "\n";
    }

    return EXIT_SUCCESS;
}
