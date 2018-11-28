#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

int n, x, y, x0, y0, x1, y1, x2, y2;
long long ans;

set<pair<int, int> > S;

long long gcd (long long a, long long b) {
    return b? gcd(b, a % b) : a;
    }

long long total (long long x0, long long y0, long long x1, long long y1) {
    long long re = 1000000000;
    
    if (x1 > 0)
        re <?= (x - 1 - x0) / x1 + 1;
    if (x1 < 0)
        re <?= (x0 - 0) / (-x1) + 1;
    if (y1 > 0)
        re <?= (y - 1 - y0) / y1 + 1;
    if (y1 < 0)
        re <?= (y0 - 0) / (-y1) + 1;
    
//    printf("total %I64d %I64d %I64d %I64d: %I64d\n",x0,y0,x1,y1,re);
    
    return re;
    }

void dfs (int x0, int y0) {
    if (x0 < 0 || y0 < 0 || x0 >= x || y0 >= y)
        return ;
    if (S.find(make_pair(x0,y0)) == S.end()) {
        ans ++;
        S.insert(make_pair(x0,y0));
        dfs(x0 + x1, y0 + y1);
        dfs(x0 + x2, y0 + y2);
        }
    }

int main () {
    int ct = 0, t;
    
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    for (scanf("%d", &t); t > 0; t --) {
        scanf("%d%d%d%d%d%d%d%d",&x,&y,&x1,&y1,&x2,&y2,&x0,&y0);
        
        ans = 0;
//        if (x1 * (long long)y2 - x2 * (long long)y1 == 0) {
            S.clear();
            dfs(x0, y0);
//            }
//        else
//            for (int i = total(x0, y0, x1, y1) - 1; i >= 0; i --)
//                ans += total(x0 + x1 * (long long)i, y0 + y1 * (long long)i, x2, y2);
        
        printf("Case #%d: %I64d\n", ++ ct, ans);
        }
   
    return 0;
    }
