#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for (int cas = 1; cas <= n; cas++) {
        int m, v;
        scanf("%d %d", &m, &v);
        vector<int> g((m-1)/2);
        vector<int> c((m-1)/2);
        for (int i = 0; i < (m-1)/2; i++) {
            scanf("%d %d", &g[i], &c[i]);
        }
        vector<int> val((m+1)/2);
        for (int i = 0; i < (m+1)/2; i++) {
            scanf("%d", &val[i]);
        }
        int numint = (m-1)/2;
        vector<int> change0((m-1)/2, 1000000000);
        vector<int> change1((m-1)/2, 1000000000);
        for (int i = (m-1)/2-1; i >= 0; i--) {
            int left = i * 2 + 1;
            int right = i * 2 + 2;
            int left0, left1, right0, right1;
            if (left >= numint) {
                if (val[left-numint] == 0) {
                    left0 = 0;
                    left1 = 1000000000;
                } else {
                    left1 = 0;
                    left0 = 1000000000;
                }
            } else {
                left0 = change0[left];
                left1 = change1[left];
            }
            if (right >= numint) {
                if (val[right-numint] == 0) {
                    right0 = 0;
                    right1 = 1000000000;
                } else {
                    right0 = 1000000000;
                    right1 = 0;
                }
            } else {
                right0 = change0[right];
                right1 = change1[right];
            }
            if (g[i] == 1) {
                // and gate
                change0[i] = min(min(left0 + right0, left0 + right1), left1 + right0);
                change1[i] = left1 + right1;
                if (c[i] == 1) {
                    change0[i] <?= left0 + right0 + 1;
                    change1[i] <?= min(min(left0 + right1, left1 + right0), left1 + right1) + 1;
                }
            } else {
                // or gate
                change0[i] = left0 + right0;
                change1[i] = min(min(left0 + right1, left1 + right0), left1 + right1);
                if (c[i] == 1) {
                    change0[i] <?= 1+ min(min(left0 + right0, left0 + right1), left1 + right0);
                    change1[i] <?= 1+ left1 + right1;
                }
            }
            change0[i] <?= 1000000000;
            change1[i] <?= 1000000000;
            //printf("%d: 0 = %d, 1 = %d\n", i, change0[i], change1[i]);
        }
        
        if ((v == 0 && change0[0] > 100000000) || (v != 0 && change1[0] > 100000000)) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        } else if (v == 0) {
            printf("Case #%d: %d\n", cas, change0[0]);
        } else {
            printf("Case #%d: %d\n", cas, change1[0]);
        }
    }
}
