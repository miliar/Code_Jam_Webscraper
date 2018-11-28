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

bool ff;
int n;
char s[1000];

    void dfs(int u)
    {
        if (ff) return;
        if (u > n) {
            int64 tmp = 0;
            for (int i = 1; i <= n; ++i)
            tmp = tmp * 2 + s[i] - '0';
            int64 w = (int64)sqrt((double)tmp);
            if (w * w == tmp || (w + 1) * (w + 1) == tmp || (w - 1) * (w - 1) == tmp) {
                //for (int i = 1; i <= n; ++i) printf("%c", s[i]);puts("");
                puts(s + 1);
                ff = 1;
                return;
            }
            return;
        }
        if (s[u] != '?') {
            dfs(u + 1);
            if (ff) return;
        }
        else {
            s[u] = '1';
            dfs(u + 1);
            s[u] = '?';
            if (ff) return;

            s[u] = '0';
            dfs(u + 1);
            s[u] = '?';
            if (ff) return;
        }
    }

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int Test, tts = 0;
    for (scanf("%d", &Test); Test--; ) {
        printf("Case #%d: ", ++tts);
        scanf("%s", s + 1);
        n = strlen(s + 1);
        ff = 0;
        dfs(1);
    }
    return 0;
}
