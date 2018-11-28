#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
vector<ll> adj[1005];
int n, k, l;
ll num[1005];
bool cmp(int a, int b) {
     return a > b;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while (T--) {
           scanf("%d%d%d", &n, &k, &l);
           for (int i = 0; i < k; i++)
                adj[i].clear();
           for (int i = 0; i < l; i++)
                scanf("%lld", &num[i]);
           sort(num, num + l, cmp);
           printf("Case #%d: ", ++cnt);
           if (k * n < l) {
               puts("Impossible");
               continue;
           }
           int now = 0;
           for (int i = 0; i < l; i++) {
                //printf("%d %d\n", now, num[i]);
                adj[now].push_back(num[i]);
                now++;
                now %= k;
           }
           ll res = 0;
           for (int i = 0; i < k; i++) {
                for (int j = 0; j < adj[i].size(); j++) {
                     res += adj[i][j] * (j + 1);
                }
           }
           printf("%lld\n", res);
    }
}
