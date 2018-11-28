#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int note[110];
void solve()
{
    int n, l, h;
    scanf("%d %d %d", &n, &l, &h);
    for(int i = 0; i < n; i++) {
        scanf("%d", &note[i]);
    }
    
    int ans;
    for(ans = l; ans <= h; ans++) {
        bool flag = true;
        for(int i = 0; i < n; i++) {
            if(note[i] == 0) continue;
            if (ans % note[i] == 0 || note[i] % ans == 0) {
                continue;
            }
            flag = false;
            break;
        }
        if (flag) {
            break;
        }
    }
    if (ans > h) {
        printf("NO\n");
    } else {
        printf("%d\n", ans);
    }
}
 
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
