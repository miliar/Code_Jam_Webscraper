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


int64 n;
int p[1000005];
bool fil[1000005];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    memset(fil, 0, sizeof(fil));
    fil[1] = 1;
    for (int i = 2; i <= 1000000; ++i)
    if (!fil[i]) {
        p[++p[0]] = i;
        for (int j = i; j <= 1000000 / i; ++j)
        fil[i * j] = 1;
    }

    int Test, tts = 0;
    for (scanf("%d", &Test); Test--; ) {
        printf("Case #%d: ", ++tts);
        scanf("%I64d", &n);

        if (n == 1) {
            puts("0");
            continue;
        }

        int64 ans = 1;
        for (int i = 1; i <= p[0]; ++i) {
            if ((int64)p[i] * p[i] > n) continue;
            for (int64 m = n; m >= p[i]; ans ++, m /= p[i]); --ans;
        }
        printf("%I64d\n", ans);
    }

}
