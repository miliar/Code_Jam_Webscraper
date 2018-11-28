#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int IMPOSSIBLE = 100000000;

int v_l[10001];
int v_g[10001];
int v_c[10001];
int dp[10001][2];

int calc(int pos, int val)
{
    int ret, tmp;

    if(dp[pos][val] < IMPOSSIBLE)
        return dp[pos][val];

    if (v_l[pos] >= 0) {
        if (v_l[pos] == val)
            return 0;
        else
            return IMPOSSIBLE;
    }

    ret = IMPOSSIBLE;
    if (v_g[pos] == 1 || (v_g[pos] == 0 && v_c[pos])) {
        // AND
        if (val) {
            tmp  = calc(pos*2, 1);
            tmp += calc(pos*2+1, 1);
        } else {
            tmp = calc(pos*2, 0);
            tmp = min(tmp, calc(pos*2+1, 0));
        }
        if (v_g[pos] == 0) {
            tmp++;
        }
        ret = min(ret, tmp);
    }

    if (v_g[pos] == 0 || (v_g[pos] == 1 && v_c[pos])) {
        // OR
        if (val) {
            tmp = calc(pos*2, 1);
            tmp = min(tmp, calc(pos*2+1, 1));
        } else {
            tmp  = calc(pos*2, 0);
            tmp += calc(pos*2+1, 0);
        }
        if (v_g[pos] == 1) {
            tmp++;
        }
        ret = min(ret, tmp);
    }

    dp[pos][val] = ret;

    return ret;
    
}


int
main(void)
{
    int N;
    int M, V;
    int G, C, L;
    int i, j;
    int ans;

    cin >> N;

    for(i=1;i<=N;i++) {
        cin >> M >> V;
        for(j=1;j<=(M-1)/2;j++) {
            cin >> G >> C;
            v_g[j] = G;
            v_c[j] = C;
            v_l[j] = -1;
            dp[j][0] = IMPOSSIBLE;
            dp[j][1] = IMPOSSIBLE;
        }
        for(;j<=M;j++) {
            cin >> L;
            v_l[j] = L;
            dp[j][0] = IMPOSSIBLE;
            dp[j][1] = IMPOSSIBLE;
        }

        ans = calc(1, V);

        if (ans >= IMPOSSIBLE) {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << i << ": " << ans << endl;
        }
    }
    
    return 0;
}
