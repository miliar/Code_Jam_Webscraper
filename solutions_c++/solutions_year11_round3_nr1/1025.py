#include <vector>

#include <string>
#include <cstdio>

#include <algorithm>
#include <utility>
#include <cstring>

#include <map>
#include <set>

#include <cassert>

#include <numeric>
#include <bitset>

#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

#include <cmath>
#include <cstdlib>

#include <list>
#include <deque>
#include <queue>
#include <stack>

#include <functional>
#include <cctype>
#include <ctime>

using namespace std;
typedef long long ll;
typedef pair<int, pair<int, int> > triple;

#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define REP(i,n) for ((i) = 0; int(i) <int(n); ++(i))
#define MP make_pair
#define PB push_back
#define sz size()
#define ln length()
#define fill(f, a) memset(f, a, sizeof(f))
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define for_each(s,container) for (typeof((container).begin()) s = (container).begin(); s != (container).end(); s++)

char c[250];

int main() {
    int t, tCtr, j, i, k;
    scanf("%d", &t);

    REP(tCtr, t) {
        int R, C;
        scanf("%d %d", &R, &C);
        vector<string> v(R);

        REP(i, R) {
            scanf("%s", c);
            v[i] = c;
        }

        REP(i, R - 1) {

            REP(j, C - 1) {
                if (v[i][j] == v[i][j + 1] && v[i + 1][j] == v[i][j] && v[i][j] == v[i + 1][j + 1] && v[i][j] == '#') {
                    v[i][j] = v[i + 1][j + 1] = '/';
                    v[i][j + 1] = v[i + 1][j] = '\\';
                }
            }
        }
        bool flag = false;

        REP(i, R) {

            REP(j, C) {
                flag |= (v[i][j] == '#');
            }
        }
        printf("Case #%d:\n", tCtr + 1);
        if (flag)
            puts("Impossible");
        else {

            REP(i, R) {
                printf("%s\n", v[i].c_str());

            }
        }
    }
    return 0;
}