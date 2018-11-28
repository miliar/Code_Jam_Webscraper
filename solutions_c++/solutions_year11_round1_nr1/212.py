#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORD(i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)

#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

const int MN = 111;
LL minD[MN][MN];

bool verify(int pd, int pg, int d) {
    if ((pd * d) % 100 != 0)
        return false;
    return true;
}

int main() {
    FORQ(pd,0,100)
        FORQ(pg,0,100) {
            if (pg == 0)
                minD[pd][pg] = (pd == 0) ? 1 : (1ll<<62ll);
            else if (pg == 100)
                minD[pd][pg] = (pd == 100) ? 1 : (1ll<<62ll);
            else {
                int d = 1;
                while (!verify(pd, pg, d)) {
                    d++;
                }
                minD[pd][pg] = d;
            }
            //printf("%d %d : %lld\n",pd, pg, minD[pd][pg]);
        }

    int t;
    scanf("%d",&t);
    FORQ(i,1,t) {
        int pd, pg; LL n;
        scanf("%lld%d%d",&n,&pd, &pg);
        printf("Case #%d: ", i);
        if (minD[pd][pg] <= n)
            printf("Possible\n");
        else
            printf("Broken\n");
    }

    return 0;
}
