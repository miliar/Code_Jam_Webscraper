#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

bool intersect(int a1, int b1, int a2, int b2)
{
    if ((a1 - a2)*(b1 - b2) < 0) return true;
    return false;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    int a[1000];
    int b[1000];
    for (int i0 = 1; i0 <= T; i0++)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d%d", &a[i], &b[i]);
        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
              if (intersect(a[i], b[i], a[j], b[j])) ans++;
        printf("Case #%d: %d\n", i0, ans);
    }

    return 0;
}
