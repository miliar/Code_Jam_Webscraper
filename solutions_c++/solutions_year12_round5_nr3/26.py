#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
using namespace std;

const int MAXN = 210;
int tot, n;
long long money, fee;
long long p[MAXN], s[MAXN];
int f[MAXN], len;
long long ans;

int cmp(int x, int y) {
    return p[x] < p[y] || (p[x] == p[y] && s[x] > s[y]);
}

long long calc(long long d) {
    long long tmp = money;
    long long ans = 0;
    tmp -= d*fee;
    for (int i = 1; i <= len; ++i)
        if (tmp < 0)
            break;
        else if (tmp/p[f[i]]/(s[f[i]]-s[f[i-1]]) >= d) {
            tmp -= p[f[i]] * (s[f[i]]-s[f[i-1]]) * d;
            ans += d*(s[f[i]]-s[f[i-1]]);
        } else {
            ans += tmp / p[f[i]];
            break;
        }
    return ans;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> tot;
    int now = 0;
    while (now < tot) {
        ++now;
        cin >> money >> fee >> n;
        for (int i = 1; i <= n; ++i) {
            cin >> p[i] >> s[i];
            f[i] = i;
        }
        s[0] = -1;
        sort(f+1, f+n+1, cmp);
        len = 1;
        long long top = s[f[1]];
        for (int i = 2; i <= n; ++i) {
            if (s[f[i]] > top) {
                f[++len] = f[i];
                top = s[f[i]];
            }
        }
        f[0] = 0;
        long long left, right, mid1, mid2;
        left = 1;
        right = money / fee;
        while (left < right-1) {
            mid1 = (2*left+right)/3;
            mid2 = (2*right+left)/3;
            if (calc(mid1) >= calc(mid2))  right = mid2;
            else  left = mid1+1;
        }
        ans = calc(left);
        long long tmp = calc(right);
        if (ans < tmp)
            ans = tmp;
        cout << "Case #" << now << ": " << ans << endl;
    }
}
