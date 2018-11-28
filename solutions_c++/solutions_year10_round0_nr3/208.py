#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int g[2000], prev[2000], n, k;
long long accum[2000], ans[2000];

pair<int, int> next(int i) {
    int j = 0;
    long long ret = 0;
    for(j = 0; j < n; j++) {
        if(g[(i+j)%n] + ret <= k)
            ret += g[(i+j)%n];
        else
            break;
    }
    return make_pair(ret, (i+j)%n);
}

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        int r;
        scanf("%d %d %d", &r, &k, &n);

        memset(prev, -1, sizeof prev);
        for(int i = 0; i < n; i++)
            scanf("%d", &g[i]);

        int cur = 0, eye;
        accum[0] = 0;
        for(eye = 1; prev[cur] == -1 && eye <= r; eye++) {
            prev[cur] = eye;

            pair<int, int> ans = next(cur);
            accum[eye] = accum[eye-1] + ans.first;
            cur = ans.second;
        }

        int length = eye - prev[cur];
        long long a = (long long)((r-eye)/length) *
            (accum[eye-1] - accum[prev[cur]-1]) + accum[eye-1];

        for(int i = 0; i <= (r-eye)%length; i++) {
            pair<int, int> ans = next(cur);
            a += ans.first;
            cur = ans.second;
        }

        printf("Case #%d: %lld\n", z, a);
    }
}

