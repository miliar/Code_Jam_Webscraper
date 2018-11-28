#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int pp[1001];
int nn[1001];
int pn;
int n;
bool ispp(int x)
{
    for (int i = 2; i * i <= x; ++i)
        if (x % i == 0) return false;
    return true;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    pn = 0;
    for (int i = 2; i <= 1000; ++i)
        if (ispp(i)) pp[pn++] = i;
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d", &n);
        if (n == 1) {
            printf("Case #%d: 0\n", ca);
            continue;
        }
        memset(nn, 0, sizeof(nn));
        int a = 1, b = 0;
        for (int i = 0; i < pn && pp[i] <= n; ++i) {
            int x = pp[i];
            while (x <= n) {
                nn[i]++;
                x *= pp[i];
            }
            a += nn[i];
            b++;
        }
        printf("Case #%d: %d\n", ca, a - b);
    }
    return 0;
}
