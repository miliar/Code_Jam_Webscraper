#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

int a[100000], b[100000];
int n;

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d", &n);
        rep(i, n) {
            scanf("%d%d", &a[i], &b[i]);
        }
        int ret = 0;
        rep(i, n) rep(j, n) {
            if (i >= j) continue;
            if (a[i] < a[j]) {
                if (b[i] > b[j]) ret++;
            } else {
                if (b[i] < b[j]) ret++;
            }
        }
        printf("Case #%d: %d\n", tt + 1, ret);
    }
}
