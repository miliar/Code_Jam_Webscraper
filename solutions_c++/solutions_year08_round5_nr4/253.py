#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

int ret[101][101];

int main() {
    int zzz;
    scanf("%d", &zzz);
    FOR(zz, 1, zzz) {
        int w, h, r;
        scanf("%d %d %d", &h, &w, &r);
        memset(ret, -1, sizeof(ret));
        REP(i, r) {
            int a, b;
            scanf("%d%d", &a, &b);
            ret[a][b] = 0;
        }
        if (ret[1][1]==-1)
            ret[1][1] = 1;
        FOR(i, 1, h) FOR(j, 1, w) if ((i!=1 || j!=1) && ret[i][j]==-1){
            ret[i][j] = 0;
            if (i>1 && j>2)
                ret[i][j] += ret[i-1][j-2];
            if (i>2 && j>1)
                ret[i][j] += ret[i-2][j-1];
            ret[i][j] %= 10007;
        }
        printf("Case #%d: %d\n", zz, ret[h][w]);
    }
    return 0;
}
