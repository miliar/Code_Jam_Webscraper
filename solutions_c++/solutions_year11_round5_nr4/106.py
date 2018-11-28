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

char ss[100];
int pp[21];
int n;
char ans[100];
bool check(long long x)
{
    long long y = (long long)sqrt(double(x));
    for (int i = -10; i <= 10; ++i)
        if ((y + i) * (y + i) == x) return true;
    return false;
}
bool getit(int k, long long x)
{
    if (k >= n) {
        if (check(x)) {
            strcpy(ans, ss);
            return true;
        }
        return false;
    }
    if (ss[k] == '?') {
        ss[k] = '0';
        if (getit(k + 1, x * 2)) return true;
        ss[k] = '1';
        if (getit(k + 1, x * 2 + 1)) return true;
        ss[k] = '?';
    } else {
        return getit(k + 1, x * 2 + ss[k] - '0');
    }
    return false;
}
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%s", ss);
        n = strlen(ss);
        getit(0, 0);
        printf("Case #%d: %s\n", ca, ans);
    }
    return 0;
}
