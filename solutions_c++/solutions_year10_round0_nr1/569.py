/*
 * Author: xay
 * Created Time:  2010-5-8 19:05:35
 * File Name: a.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;

int main() {
    freopen("a.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        int n, k;
        scanf("%d%d", &n, &k);
        bool flag = true;
        for (int i = 0; i < n; ++i) {
            if (((1<<i)&k)==0) {
                flag = false;
                break;
            }
        }
        if (flag) printf("ON\n");
        else printf("OFF\n");
    }
    return 0;
}

