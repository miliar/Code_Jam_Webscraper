#include<cstdio>
#include<cstdlib>
#include <algorithm>

using namespace std;

typedef long long LL;
LL gcd(LL m, LL n){
    while(true){
        if((m = m%n) == 0) return n;
        if((n = n%m) == 0) return m;
    }
}
int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, d, g;
        scanf("%d%d%d", &n, &d, &g);
        printf("Case #%d: ", cas);
        if(g == 100 && d != 100) puts("Broken");
        else if(g == 0 && d != 0) puts("Broken");
        else if(d == 0) puts("Possible");
        else{
            int tmp = gcd(100, d);
            tmp = 100 / tmp;
            if(tmp <= n) puts("Possible");
            else puts("Broken");
        }
    }
    return 0;
}

