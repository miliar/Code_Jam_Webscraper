#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
    int nTests;
    cin >> nTests;
    for (int test = 0; test < nTests; test++)
    {
        int n;
        cin >> n;

        vector<int> c(n);
        for (int i = 0; i < n; i++) cin >> c[i];

        int ans = -1;
        for (int mask = 1; mask + 1 < (1 << n); mask++)
        {
            int s = 0, p1 = 0, p2 = 0;
            for (int i = 0; i < n; i++) if (mask & (1 << i))
            {
                s += c[i];
                p1 ^= c[i];
            }    
            else
                p2 ^= c[i];

            if (p1 == p2) ans = max(ans, s);
        }

        printf("Case #%d: ", test + 1);
        if (ans >= 0)
            printf("%d\n", ans);
        else
            printf("NO\n");
    }

    return 0;
}    