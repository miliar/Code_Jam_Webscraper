#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int data[510][510];
int c[510][510];

int C(int i,int j) {
    return c[i][j];
}

int dp(int i,int j) {
    if (i <= j) return 0;
    if (j == 1) return data[i][j] = 1;
    if (i == j-1) return data[i][j] = 1;
    if (data[i][j] != -1) return data[i][j];
    int k, ans = 0;
    for (k = j-1; k >= j-(i-j) && k > 0; k--) {
        ans += dp(j,k)*C(i-j-1,j-1-k);
        ans %= 100003;
    }
    return data[i][j] = ans%100003;
}

int main () {
    int kase, i, j, n, h = 1;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("a.out","w",stdout);
    for (i = 0; i <= 500; i++) {
        c[i][0] = 1;
        c[i][i] = 1;
    }
    for (j = 1; j <= 500; j++)
        for (i = j+1; i <= 500; i++)
            c[i][j] = (c[i-1][j-1]+c[i-1][j])%100003;
    scanf("%d", &kase);
    
    memset(data,-1,sizeof(data));
    for (i = 2; i <= 500; i++)
        for (j = 1; j < i; j++)
            data[i][j] = dp(i,j);
    while (kase--) {
          scanf("%d", &n);
          int ans = 0;
          for (i = 1; i < n; i++) {
              ans += data[n][i];
              ans %= 100003;
          }
          printf("Case #%d: %d\n",h++, ans);
    }
    return 0;
}
