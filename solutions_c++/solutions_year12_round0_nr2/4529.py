#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

int a[50];
    
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int k = 1; k <= T; k++) {
        int n, s, p;
        scanf("%d %d %d", &n, &s, &p);
        memset(a, 0, sizeof(a));
        while (n--) {
            int tmp;
            scanf("%d", &tmp);
            a[tmp]++;
        }
        for (int i = 1; i <= 30; i++)
            a[i] += a[i-1];  
        int res = 0;
        if (a[30] - a[1] < s) {
            res = 0;
        }else if (p == 0) {
            res = a[30];
        }else if (p == 1) {
            res = a[30] - a[0];
        }else {
            int pp = p * 3 - 3;
            res = a[30] - a[pp];
            res += min(a[pp] - a[pp-2], s);
        }
                       
        printf("Case #%d: %d\n", k, res, a[30]);
    }
//    system("pause");
    return 0;
}
