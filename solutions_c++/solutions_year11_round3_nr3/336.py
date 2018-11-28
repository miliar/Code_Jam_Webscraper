// author: amit
#include <cstdio>
#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define TR(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define REP(i, n) for(int i = 0; i<(n); i++)
#define REPSE(i, s, e) for(int i = s; i <(e); i++)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define FILL(x, c) memset(x, c, sizeof(x))
#define ALL(x) x.begin(), x.end()
#define FIN(x, c) (x.find(c)!=x.end())
#define IN(x, c) (find(x.begin(), x.end(), c)!=x.end())

#define SORT(x) sort(x.begin(), x.end())
#define SS {int t; scanf("%d", &t), t}
//

int a[11111];
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t;
    scanf("%d", &t);

    for(int testcase = 1; testcase <= t; testcase++) {
        int n, l, h;
        scanf("%d%d%d", &n, &l, &h);

        REP(i, n) scanf("%d", &a[i]);

        int ans = -1;
        for(int i = l; i <= h; i++) {
            bool ok = true;
            REP(j, n) {
                if((a[j]%i!=0) && (i%a[j]!=0)) ok = false;
            }
            if(ok) {
                ans = i;
                break;
            }
        }


        printf("Case #%d: ", testcase);
        if(ans==-1) printf("NO\n");
        else printf("%d\n", ans);
    }
}
