#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

void solve()
{
    int n;
    cin >> n;
    int ans = 1 << 30;
    int all = 0;
    int x = 0;
    for (int i = 0; i < n; i++)
    {
        int y;
        cin >> y;
        x ^= y;
        
        all += y;
        if (y < ans)ans = y;
    }
    if (!x)printf("%d\n", all - ans);
    else printf("NO\n");
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
