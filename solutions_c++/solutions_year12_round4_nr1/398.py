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

#define rep(i,a,b) for(__typeof(b) i=a; i<(b); ++i)
#define trav(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
int main()
{
    int tt; scanf("%d", &tt);
    rep(sd,0,tt)
    {
        int n; scanf("%d", &n);
        vi hold(n, 1234567890);
        hold[0] = 0;
        vi pos(n), len(n);
        bool ok = false;
        rep(i,0,n)
            scanf("%d %d", &pos[i], &len[i]);
        int D;
        scanf("%d", &D);

        int can_reach = 0;
        rep(i,0,n)
        {
            int max_dist = pos[i] + min(len[i], pos[i] - hold[i]);
            if (max_dist >= D)
                ok = true;
            rep(j,can_reach + 1,n)
            {
                if (max_dist < pos[j])
                    break;
                hold[j] = pos[i];
                can_reach = j;
            }
        }

        printf("Case #%d: %s\n", sd+1, (ok ? "YES" : "NO"));
    }
}
