#include <cstdio>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;
const ll inf = (1ll<<60);
char str[100];
int len;
ll res;
bool check(ll num) {
     return (num % 2 == 0) ||(num % 3 == 0)||(num % 5 == 0)||(num % 7 == 0);
}
void dfs(int d, ll pre, ll sum) {
     if (d == len) {
         if (check(sum + pre)) {
             res++;
         }
         return;
     }
     else {
         dfs(d+1,(pre*10+str[d]-'0'), sum);
         if (d > 0) {
             dfs(d+1, (ll)(str[d] - '0'), sum - pre);
             dfs(d+1, (ll)(str[d] - '0'), sum + pre);
         }
     }
}
int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    int cnt = 0;
    scanf("%d", &T);
    getchar();
    while (T--) {
           gets(str);
           len = strlen(str);
           res = 0;
           dfs(0, 0, 0);
           printf("Case #%d: %lld\n", ++cnt, res);
    }
}
