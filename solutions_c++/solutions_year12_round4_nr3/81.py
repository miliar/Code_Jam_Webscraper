#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int maxn = 2000 + 5;

int n, a[maxn], h[maxn];

void work(int l, int r, int H, int k)
{
    for (int i = l; i != r; i = a[i])
        h[i] = H - (r - i) * k;
    h[r] = H;
    for (int i = l; i != r; i = a[i])
        work(i + 1, a[i], h[a[i]], k + 1);
}

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        cin >> n;
        for (int i = 1; i < n; ++i)
            cin >> a[i];
        bool ok = true;
        for (int i = 1; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                if (j < a[i] && a[j] > a[i])
                    ok = false;
        if (!ok)
            cout << "Impossible";
        else {
            memset(h, 0, sizeof(h));
            work(1, n, int(1e9), 0);
            for (int i = 1; i <= n; ++i)
                cout << h[i] << " ";
        }
        printf("\n");
    }
    
    return 0;
}
