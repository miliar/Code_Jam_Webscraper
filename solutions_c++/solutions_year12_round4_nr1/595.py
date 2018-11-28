#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define FORALL(a,b) for(typeof((b).begin()) a = (b).begin(); a != (b).end(); ++a)
#define FOR(i,a,b) for(int i = a; i < (int)(b); ++i)

typedef long long LL;

const double EPS = 1e-6;
const int INF = 1<<29;
const int N = 10010;

int d[N], l[N], D;
int f[N];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    int n;
    int cas = 0;

    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d %d", &d[i], &l[i]);
        scanf("%d", &D);
        for (int i = 0; i <= n; ++i) f[i] = 0;
        f[0] = d[0];
        for (int i = 0; i < n; ++i){
            for (int j = i+1; j < n; ++j){
                if (d[j]-d[i] > f[i]) break;
                if (l[j] < d[j]-d[i]){
                    if (f[j] < l[j]) f[j] = l[j];
                }
                else{
                    if (f[j] < d[j]-d[i]) f[j] = d[j]-d[i];
                }
            }
//            printf("f[%d] = %d\n", i, f[i]);
        }
        bool flag = 0;
        for (int i = 0; i < n; ++i) if (d[i]+f[i] >= D) flag = 1;
        printf("Case #%d: %s\n", ++cas, flag ? "YES" : "NO");
    }

    return 0;
}
