#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <queue>
using namespace std;

const int maxn = 64;
int rt[maxn];
int cases, cas = 1, n;
char line[1024];

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", line);
            rt[i] = -1;
            for (int k = 0; k < n; ++k) if (line[k] == '1') {
                rt[i] = k;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) if (rt[i] > i) {
            int next = -1;
            for (int j = i + 1; j < n; ++j) if (rt[j] <= i) {
                next = j;
                break;
            }
            while (next > i) {
                swap(rt[next], rt[next - 1]);
                ans++;
                next--;
            }
        }

        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}

