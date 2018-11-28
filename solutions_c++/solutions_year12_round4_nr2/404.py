#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

const int maxn = 2000;

int A, B, n;
int r[maxn], id[maxn], ansx[maxn], ansy[maxn];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int Tests, tts = 0;
    for (scanf("%d", &Tests); Tests--; ) {
        printf("Case #%d:", ++tts);

        scanf("%d%d%d", &n, &A, &B);
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &r[i]);
            id[i] = i;
        }
        bool ff = 1;
        if (A > B) {
            ff = 0;
            swap(A, B);
        }

        for (int i = 1; i <= n; ++i)
        for (int j = i + 1; j <= n; ++j)
        if (r[i] < r[j]) {
            swap(r[i], r[j]);
            swap(id[i], id[j]);
        }

        int x = 0, y = 0, nr = r[1];
        for (int o = 0; o < n && x <= B; ) {
            if (y == 0 && y >= A || y > 0 && y + r[o + 1] >= A) {
                x += nr + r[o + 1];
                nr = r[o + 1];
                y = 0;
            } else {
                if (y == 0) {
                    ansx[id[o + 1]] = x;
                    ansy[id[o + 1]] = y;
                    y += r[o + 1];
                } else {
                    y += r[o + 1];
                    ansx[id[o + 1]] = x;
                    ansy[id[o + 1]] = y;
                    y += r[o + 1];
                }
                ++o;
            }
        }

        for (int i = 1; i <= n; ++i)
        if (!ff) printf(" %d %d", ansx[i], ansy[i]); else printf(" %d %d", ansy[i], ansx[i]);

        puts("");
    }
    return 0;
}
