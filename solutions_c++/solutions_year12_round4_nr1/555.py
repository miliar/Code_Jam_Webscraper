#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int N = 100005;
int f[N], d[N], l[N], n, D;
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int T; cin >> T;
    for (int i = 1; i <= T; i++){
        cin >> n;
        for (int i = 0; i < n; i++)
            scanf("%d%d", &d[i], &l[i]);
        cin >> D;
        memset(f, 0, sizeof(f));
        f[0] = min(d[0], l[0]);
        bool ans = false;
        for (int i = 0; i < n; i++){
            int j = i + 1;
            while (d[i] + f[i] >= d[j] && j < n){
                f[j] = max(f[j], min(l[j], d[j] - d[i]));
                j++;
            }
        }
        for (int i = 0; i < n; i++) if (f[i] + d[i] >= D) ans = true;
        printf("Case #%d: %s\n", i, ans ? "YES" : "NO");
    }
}
