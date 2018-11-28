#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <queue>
#include <bitset>
#include <utility>
#include <list>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> PI;
int main() {
    int t; scanf("%d", &t);
    REP(sd,t)
    {
        int h, w, r;
        scanf("%d %d %d", &h, &w, &r);
        ll q[h+1][w+1];
        memset(q, 0x00, sizeof(q));
        q[0][0]=1;
        int mod = 10007;
        REP(i,r){
            int a, b; scanf("%d %d", &a, &b);
            a--; b--;
            q[a][b] = -47*mod;
        }
        REP(i,h) REP(j,w) if (q[i][j] > 0)
        {
            q[i][j] %= mod;
            if (i+2<h && j+1<w) q[i+2][j+1] += q[i][j];
            if (i+1<h && j+2<w) q[i+1][j+2] += q[i][j];
        }

        printf("Case #%d: %lld\n", sd+1, q[h-1][w-1]);

    }
}
