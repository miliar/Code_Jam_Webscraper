#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
const int MAXN = 1000100;
int prime[MAXN];
int plist[MAXN], pl;

void initp() {
    int i, j;
    for (i = 2 ; i * i < MAXN ; i++) {
        if (prime[i] == 0) {
            for (j = i * i ; j < MAXN ; j += i)
                prime[j] = 1;
            }
    }
    for (i = 2 ; i < MAXN ; i++)
        if (!prime[i]) plist[pl++] = i;
    //for (i = 0 ; i < 20 ; i++)
    //    printf(" %d",plist[i]);
}

int main() {
    freopen("c-large.in","r",stdin);
    freopen("c-klar.out","w",stdout);
    int T, ca, i;
    LL n, tn;
    initp();
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%I64d",&n);
        LL ans = 0;
        for (i = 0 ; (LL)plist[i] * plist[i] <= n && i < pl ; i++) {
            int cnt = 0;
            for (tn = n ; tn >= plist[i] ; tn /= plist[i]) {
                ++cnt;
            }
           // printf("plist:%d cnt:%d\n",plist[i],cnt);
            ans += cnt - 1;
        }
        if (n == 1) ans = -1;
        printf("Case #%d: %I64d\n",ca,ans+1);
    }
    return 0;
}
