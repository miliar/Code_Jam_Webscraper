#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>

using namespace std;

#define MAXN 10050

int d[MAXN], len[MAXN];
int i, j, t, T, N, D;
int dp[MAXN];

int solve() {
    memset(dp, 0, sizeof(dp));
    dp[0] = d[0];
    for(i = 0; i < N; i++)
        for(j = i + 1; j < N; j++) {
            if(dp[i] < d[j] - d[i]) continue;
            int swing = min(d[j] - d[i], len[j]);
            dp[j] = max(dp[j], swing);
        }
    for(i = 0; i < N; i++)
        if(dp[i] + d[i] >= D)
            return 1;
    return 0;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);
#endif
	cin >> T;
	for(t = 1; t <= T; t++) {
        cin >> N;
        for(i = 0; i < N; i++)
            cin >> d[i] >> len[i];
        cin >> D;
        int res = solve();
        cout << "Case #" << t << ": " << (res ? "YES" : "NO") << "\n";
	}
	return 0;
}
