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

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
const double pi = acos(-1.0);
const double eps = 1E-7;
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

struct TWay {
    int x, y, z;
} P[10005];

double ans;
int L, v1, v2, T, n, m;

inline bool cmp1(TWay a, TWay b)
{
    return a.x < b.x;
}

inline bool cmp2(TWay a, TWay b)
{
    return a.z < b.z;
}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int Test, tts = 0;
    for (scanf("%d", &Test); Test--; ) {
        printf("Case #%d: ", ++tts);
        scanf("%d%d%d%d%d", &L, &v1, &v2, &T, &n);
        for (int i = 1; i <= n; ++i)
        scanf("%d%d%d", &P[i].x, &P[i].y, &P[i].z);

        sort(P + 1, P + n + 1, cmp1);
        int now = 0; m = n;
        for (int i = 1; i <= n; ++i) {
            if (P[i].x > now) {
                P[++m].x = now; P[m].y = P[i].x; P[m].z = 0;
            }
            now = P[i].y;
        }
        if (now < L) {
            P[++m].x = now; P[m].y = L; P[m].z = 0;
        }
        n = m;
        sort(P + 1, P + n + 1, cmp2);

        double ut = T; ans = 0;
        for (int i = 1; i <= n; ++i) {
            double len = P[i].y - P[i].x;
            double nv = v2 + P[i].z;
            double nowt = len / nv;
            nowt = min(ut, nowt);
            ut -= nowt;
            ans += nowt;
            ans += (len - nowt * nv) / (double)(v1 + P[i].z);
        }

        printf("%.7lf\n", ans);
    }

    return 0;
}
