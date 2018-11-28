#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;

//BEGIN TEMPLATE HERE
typedef long long int64;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
//END TEMPLATE HERE

const int maxn = 1000 + 5;

//map <vector <int>, int> M;
//double f[maxn]
int a[maxn], u[maxn], n;
int factorial[maxn];

int main() {
    freopen("D-large.in", "r", stdin); freopen("D-large.out", "w", stdout);
    //freopen("D-small-attempt2.in", "r", stdin); freopen("D-small-attempt2.out", "w", stdout);
    //freopen("D-small-attempt1.in", "r", stdin); freopen("D-small-attempt1.out", "w", stdout);
    //freopen("D-small-attempt0.in", "r", stdin); freopen("D-small-attempt0.out", "w", stdout);
    //freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    //precalc();
    int T;
    scanf("%d", &T);
    factorial[0] = 1;
    for (int i = 1; i <= 10; i ++) {
       factorial[i] = factorial[i - 1] * i;
    } 
    for (int caseId = 1; caseId <= T; caseId ++) {
        printf("Case #%d: ", caseId);
        scanf("%d", &n);
        for (int i = 1; i <= n; i ++) {
            scanf("%d", &a[i]);
        }
        int ans = 0;
        memset(u, 0, sizeof u);
        for (int i = 1; i <= n; i ++) {
            if (!u[i]) {
                int L = 0;
                for (int x = i; !u[x]; x = a[x]) {
                    L ++;
                    u[x] = 1;
                }
                if (L > 1) {
                    ans += L;
                }
            }
        }
        printf("%d.000000\n", ans);
    }
    return 0;
}

