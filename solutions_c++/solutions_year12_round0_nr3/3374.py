#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <climits>
#include <cstdio>
#include <algorithm>




using namespace std;

const int MAXN = 11000;
int A, B;
int T;
bool vis[MAXN];
int getlen(int x)
{
    int n = 0;
    while(x)
    {
        n++;
        x /= 10;
    }
    return n;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);


    for(int i = 0; i < T; i++)
    {
        int ans = 0;
        scanf("%d %d", &A, &B);
        for(int n = A; n <= B; n++)
        {
            memset(vis, false, sizeof(vis));
            int len = getlen(n);
            int base = 10;
            int maxBase = 1;
            for(int j = 0; j < len; j++)
            {
                maxBase *= 10;
            }
            for(int j = 0; j < len - 1; j++)
            {
                int tmp = n / base + (n % base) * maxBase / base;
                if(tmp > n && tmp <= B && !vis[tmp])
                {
                    vis[tmp] = true;
                    ans++;
                }
                base *= 10;
            }
        }

        printf("Case #%d: %d\n", i + 1, ans);

    }











    return 0;
}
