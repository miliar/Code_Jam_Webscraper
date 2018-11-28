#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    long long int cost[1000];
    int next[1000];
    int c[1000];
    for (int i0 = 1; i0 <= T; i0++)
    {
        int n, k, r;
        scanf("%d%d%d", &r, &k, &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &c[i]);
        for (int i = 0; i < n; i++)
        {
            long long int w = c[i];
            int j = i + 1;
            if (j == n) j = 0;
            while ((w + c[j]  <= k)&&(j != i))
            {
                w += c[j];
                j++;
                if (j == n) j = 0;
            }
            cost[i] = w;
            next[i] = j;
        }
        int a = 0;
        long long int ans = 0;
        for (int i = 0; i < r; i++)
        {
            ans += cost[a];
            a = next[a];
        }
        printf("Case #%d: ", i0);
        cout << ans << endl;
    }
    return 0;
}
