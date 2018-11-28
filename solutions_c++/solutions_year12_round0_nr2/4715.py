#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iomanip>
#define eps 1e-6
#define pi acos(-1.0)

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    char alpf[] = "abcdefghijklmnopqrstuvwxyz";
    char tran[] = "yhesocvxduiglbkrztnwjpfmaq";
    int cas;
    while (scanf("%d", &cas) == 1) {
        char str[200];
        for (int i = 0; i < cas; i++) {
            int n, s, p;
            int num[120];
            scanf("%d%d%d", &n, &s, &p);
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                scanf("%d", &num[i]);
                if ((num[i] + 2) / 3 >= p) cnt++;
                else if (num[i] % 3 != 1 && (num[i] + 2) / 3 == p - 1 && num[i] != 0 && s > 0){
                    cnt++;
                    s--;
                }
            }
            printf("Case #%d: %d\n", i + 1, cnt);
        }
    }
    return 0;
}
