#include <iostream>
#include <vector>
using namespace std;

long long gcd(long long a, long long b)
{
    if (!b) return a;
    else return gcd(b, a % b);
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int time, n, k;
    vector<int> t;
    scanf("%d", &time);
    for (int i = 0; i < time; ++i) {
        scanf("%d", &n); t.clear();
        for (int j = 0; j < n; ++j) {
            scanf("%d", &k);
            t.push_back(-k);
        }
        sort(t.begin(), t.end());
        k = t[1] - t[0];
        if (n > 2) k = gcd(k, t[2] - t[1]);
        t[0] = t[0] % k;
        if (t[0] < 0) t[0] += k;
        printf("Case #%d: %d\n", i + 1, t[0]);
    }
    
    return 0;
}
