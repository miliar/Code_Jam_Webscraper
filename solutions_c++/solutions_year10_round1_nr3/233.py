#include <iostream>
using namespace std;

int f[1000001], t, a1, a2, b1, b2;

bool check(const int &i, const int &j)
{
     int w = i % j + j;
     if (w <= j) w += j;
     if (w < i && f[w] < j) return 1;
     if (f[j] < w - j) return 1;
     return 0;
}

int main()
{
    f[1] = 0;
    for (int i = 1; i <= 1000000; ++i) {
        int l = 1, r = i, mid;
        while (l < r) {
              mid = l + r >> 1;
              if (check(i, mid)) l = mid + 1;
              else r = mid;
        }
        f[i] = r - 1;
    }
    
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        long long ans = 0;
        cin >> a1 >> a2 >> b1 >> b2;
        printf("Case #%d: ", i + 1);
        for (int j = a1; j <= a2; ++j)
            if (f[j] >= b2) ans += b2 - b1 + 1;
            else if (f[j] >= b1) ans += f[j] - b1 + 1;
        for (int j = b1; j <= b2; ++j)
            if (f[j] >= a2) ans += a2 - a1 + 1;
            else if (f[j] >= a1) ans += f[j] - a1 + 1;
        printf("%I64d\n", ans);
    }
    return 0;
}
