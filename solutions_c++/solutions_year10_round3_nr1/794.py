#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <cstring>
#include <vector>
#include <map>
#include <cmath>

#define oo 2000000000
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define debug(x) cout << #x << " " << x << endl;

using namespace std;

int a[1100], b[1100], belum[1100][1100];

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tcc;
    scanf("%d", &tcc);
    for (int i = 0; i < tcc; ++i) {
        memset(belum, 0, sizeof(belum));
        int N;
        scanf("%d", &N);
        for (int j = 0; j < N; ++j)
            scanf("%d%d", &a[j], &b[j]);
        
        int ans = 0;
        for (int j = 0; j < N - 1; ++j) {
            for (int k = j + 1; k < N; ++k)
                if (belum[j][k] != 1) {
                   if ((a[j] > a[k] && b[j] < b[k]) || (a[j] < a[k] && b[j] > b[k])) {
                      ans++;
                      belum[j][k] = 1;
                      belum[k][j] = 1;
                   }
                }
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    return 0;
}
