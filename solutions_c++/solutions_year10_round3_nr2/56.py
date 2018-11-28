#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    int dp[50];
    dp[0] = 0;
    for (int i = 1; i < 50; i++)
        dp[i] = dp[i / 2] + 1;
    for (int i0 = 1; i0 <= T; i0++)
    {
        long long int l, p;
        long long int c;
        cin >> l;
        cin >> p;
        cin >> c;
        int i = 0;
        long long int w = l * c;
        while (w < p)
        {
            w *= c;
            i++;
        }
        printf("Case #%d: %d\n", i0, dp[i]);
    }
    return 0;
}
