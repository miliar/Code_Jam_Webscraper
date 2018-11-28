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

int n, a, b[10005], c[10005];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int Test, tts = 0;
    for (scanf("%d", &Test); Test--; ) {
        printf("Case #%d: ", ++tts);
        scanf("%d", &n);
        if (n == 0) {
            puts("0");
            continue;
        }
        memset(b, 0, sizeof(b));
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &a);
            ++b[a];
        }

        for (int k = n; k > 0; --k) {
            for (int i = 1; i <= 10000; ++i) c[i] = b[i];
            bool ff = 1;
            for ( ; ; ) {
                int j;
                for (j = 1; j <= 10000 && !c[j]; ++j) {}
                if (j > 10000) break;
                int ct = 0;
                for ( ; ; ) {
                    if (c[j] < 0) {
                        ff = 0;
                        break;
                    }
                    --c[j];
                    if (++ct >= k && c[j + 1] <= c[j]) break;
                    ++j;
                }
                if (!ff) break;
            }
            if (ff) {
                printf("%d\n", k);
                break;
            }
        }
    }

    return 0;
}
