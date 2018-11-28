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
ll vs(ll a, ll b, ll c, ll d)
{
    return abs(a * d - b * c);
}
int main() {
    int t; scanf("%d", &t);
    REP(sd,t)
    {
        int n, m; ll a;
        scanf("%d %d %lld", &n, &m, &a);
        printf("Case #%d:", sd+1);
        REP(i,n+1) REP(j,m+1) if (i+j>0)
            REP(k,n+1) REP(l,m+1) if (k+l>0)
        {
            if (vs(i, j, k, l) == a)
            {
                printf(" 0 0 %d %d %d %d\n", i, j, k, l);
                goto dobre;
            }
        }
        printf(" IMPOSSIBLE\n");
        dobre:;
    }
}
