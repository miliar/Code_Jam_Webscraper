#include <cstdio>
#include <cstring>

#define maxn 1000
typedef long long ll;
int g[maxn + maxn];
ll s[maxn + maxn];

int f[maxn];
ll tot[maxn];

int n, k;
void go(int start, int &next, ll &gain) {
    if (s[n - 1] <= k) {
        next = start;
        gain = s[n - 1];
        return;
    }

    gain = 0; 
    for (int i = start; i < start + n; ++i) {
        ll total = s[i];
        if (start != 0) total -= s[start - 1];
        if (total > k) {
            next = i;
            break;
        } else {
            gain = total;
        }
    }
    if (next >= n) next -= n;
}

int main() {
    int t;
    scanf("%d", &t);

    for (int kase = 1; kase <= t; ++kase) {
        int r;
        scanf("%d%d%d", &r, &k, &n);

        for (int i = 0; i < n; ++i) {
            scanf("%d", &g[i]);
            g[i + n] = g[i];
        }
        for (int i = 0; i < n + n; ++i) {
            if (i == 0) {
                s[i] = g[i];
            } else {
                s[i] = g[i] + s[i - 1];
            }
        }

        printf("Case #%d: ", kase);
        memset(f, -1, sizeof(f));
        memset(tot, 0, sizeof(tot));

        ll ans = 0; 
        int start = 0;
        int next;
        ll gain;
        bool cut = false;
        for (int i = 0; i < r; ++i) {
            go(start, next, gain); 
            ans += gain;
            if (f[start] != -1) {
                int T = i - f[start]; 
                int x = (r - f[start]) / T;
                ans = tot[start] + x * (ans - tot[start]) - gain;
                r = (r - i) % T;
                cut = true;
                break;
            }
            
            f[start] = i;
            tot[start] = ans;
            start = next;
        } 
        if (cut) {
            for (int i = 0; i < r; ++i) {
                go(start, next, gain);
                ans += gain;
                start = next;
            }
        }
        printf("%I64d\n", ans);
    }

    return 0;
}
