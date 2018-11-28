#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair
#define A first
#define B second
#define eps 1e-8

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int t, n, d[10010], d1[10010], l[10010], dt;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A2.out","w",stdout);
    scanf("%d", &t);
    for (int i = 1; i <= t; i ++ ) {
        scanf("%d", &n);
        for (int j = 0; j < n; j ++ )
            scanf("%d%d", &d[j], &l[j]);
        scanf("%d", &dt);
        memset(d1, 0, sizeof(d1));
        d1[0] = d[0];
        bool flag = false;
        if (d1[0] + d[0] >= dt) flag = true;
        for (int j = 1; j < n; j ++ ) {
            d1[j] = 0;
            for (int k = j - 1; k >= 0; k -- )
                if (d1[k] + d[k] >= d[j])
                    d1[j] = max(d1[j], min(d[j] - d[k], l[j]));
            if (d[j] + d1[j] >= dt) {
                flag = true;
                break;
            }
        }
        if (flag) printf("Case #%d: YES\n", i);
        else printf("Case #%d: NO\n", i);
    }

    return 0;
}
