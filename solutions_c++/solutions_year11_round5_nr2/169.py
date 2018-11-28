#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

int n;
int array[1005];

int last[10005];
int prev[1005];

int cnt[10005];

bool mark[1005];

int main() {
//    freopen("B-small.in", "r", stdin); freopen("B-small.out", "w", stdout);
    freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
    int tests; scanf("%d", &tests);
    for (int testId = 1; testId <= tests; ++testId) {
        printf("Case #%d: ", testId);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d", &array[i]);
        sort(array, array + n);
        int mid;
        for (mid = n; mid >= 0; --mid) {
            memset(cnt, 0, sizeof(cnt));
            for (int i = 0; i < n; ++i)
                ++cnt[array[i]];
            memset(last, -1, sizeof(last));
            for (int i = n - 1; i >= 0; --i) {
                prev[i] = last[array[i]];
                last[array[i]] = i;
            }
            bool can = true;
            memset(mark, 0, sizeof(mark));
            for (int i = 0; i < n; ++i) {
                if (mark[i]) continue;
                int pos = i;
                int j;
                bool c = true;
                for (j = 1; j < mid; ++j) {
                    if (last[array[pos] + 1] == -1) {
                        c = false;
                        break;
                    }
                    pos = last[array[pos] + 1];
                }
                if (!c) {
                    can = false;
                    break;
                }
                pos = i;
                mark[i] = true;
                --cnt[array[i]];
                last[array[i]] = prev[i];
                for (j = 1; j < mid || last[array[pos] + 1] != -1 && cnt[array[pos]] + 1 <= cnt[array[pos] + 1]; ++j) {
                    pos = last[array[pos] + 1];
                    mark[pos] = true;
                    --cnt[array[pos]];
                    last[array[pos]] = prev[pos];
                }
            }
            for (int j = 0; j < n; ++j)
                if (!mark[j])
                    can = false;
            if (can) break;
        }
        printf("%d\n", mid);
    }
    return 0;
}
