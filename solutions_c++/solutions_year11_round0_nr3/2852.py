//*****************
// LAM PHAN VIET **
// Google Code Jam - Problem C. Candy Splitting
// Time limit:
//********************************
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define For(i, a, b) for (int i=a; i<=b; i++)
#define maxN 1001
int n, a[maxN], ans;
bool Free[maxN];

void Choose(int k, int stt, int Sum, int num) {
    if (num==n) return;
    if (num) {
        int stt2 = 0, Sum2 = 0;
        For (i, 1, n)
            if (Free[i]) {
                stt2 ^= a[i];
                Sum2 += a[i];
            }
        if (stt2 == stt) ans = max(ans, Sum);
    }
    For (i, k+1, n) {
        Free[i] = false;
        Choose(i, stt ^ a[i], Sum + a[i], num+1);
        Free[i] = true;
    }
}

main() {
//    freopen("cc.inp", "r", stdin); freopen("cc.out", "w", stdout);
    int Case;
    scanf("%d", &Case);
    For (kk, 1, Case) {
        scanf("%d", &n);
        For (i, 1, n) {
            scanf("%d", &a[i]);
            Free[i] = true;
        }
        ans = 0;
        Choose(0, 0, 0, 0);
        printf("Case #%d: ", kk);
        if (ans) printf("%d\n", ans);
        else puts("NO");
    }
}

/* lamphanviet@gmail.com - 2011 */
