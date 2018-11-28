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

const int maxn = 20005;

int n, d[maxn], a[maxn], f[maxn];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int Tests, tts = 0;
    for (scanf("%d", &Tests); Tests--; ) {
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d%d", &d[i], &a[i]);
        scanf("%d", &d[n + 1]);
        ++n;

        for (int i = 1; i <= n; ++i) f[i] = -1;
        f[1] = d[1];
        for (int i = 1; i <= n - 1; ++i) {
            int l = f[i];
            for (int j = i + 1; j <= n; ++j)
            if (d[j] - d[i] <= l && f[j] < min(d[j] - d[i], a[j])) f[j] = min(d[j] - d[i], a[j]);
        }
        printf("Case #%d: ", ++tts);
        if (f[n] != -1) puts("YES"); else puts("NO");
    }
    return 0;
}
