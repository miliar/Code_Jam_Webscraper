/*
 * Author: Xay
 * Created Time:  2011/5/7 13:29:30
 * File Name: b.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;

int map[30][30];
int opp[30][30];

int main() {
    freopen("b.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        int c;
        char s[105];
        memset(map, -1, sizeof(map));
        memset(opp, 0, sizeof(opp));
        scanf("%d", &c);
        while (c--) {
            scanf("%s", s);
            int x1 = s[0] - 'A', x2 = s[1] - 'A', x = s[2] - 'A';
            map[x1][x2] = x;
            map[x2][x1] = x;
        }
        scanf("%d", &c);
        while (c--) {
            scanf("%s", s);
            int x1 = s[0] - 'A', x2 = s[1] - 'A';
            opp[x1][x2] = opp[x2][x1] = -2;
        }
        scanf("%d%s", &c, s);
        vector<int> ans;
        for (int i = 0; i < c; ++i) {
            int x = s[i] - 'A';
            if (!ans.empty() && map[ans.back()][x] >= 0) {
                ans[ans.size() - 1] = map[ans.back()][x];
                continue;
            }
            ans.push_back(x);
            for (int j = ans.size() - 2; j >= 0; --j) {
                if (opp[ans[j]][x]) {
                    ans.clear();
                    break;
                }
            }
        }
        printf("[");
        for (int i = 0; i < (int)ans.size(); ++i) {
            if (i) printf(", ");
            printf("%c", ans[i] + 'A');
        }
        printf("]\n");
    }
    return 0;
}

