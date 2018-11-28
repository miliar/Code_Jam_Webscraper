#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<utility>
#include<iostream>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<ctype.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
int dp[200][200],L[200],H[200],E;
int get(int x, int y) {
    return min(L[y] - L[x], H[y]);
}
int main () {
    int i, j, n, m, TC=1,ans,tem,k,N;
    scanf("%d", &N);
    L[0] = 0;
    while (N--) {
        scanf("%d", &n);
        for (i=1; i<=n; i++) scanf("%d%d", &L[i], &H[i]);
        scanf("%d", &E);
        ans = 0;
        memset(dp, 0, sizeof(dp));
        dp[0][1] = 1;
        for (i=0; i<n && ans == 0; i++) for (j=1; j<=n && ans == 0; j++)
            if (dp[i][j]) {
                
                tem = get(i, j);
                //printf("%d %d %d\n",i,j,tem);
                if (L[j] + tem >= E) {
                    ans = 1;
                    break;
                }
                for (k=j+1;k<=n;k++) {
                    if (L[j] + tem < L[k]) break;
                    dp[j][k] = 1;
                }
            }
        printf("Case #%d: %s\n", TC++, ans?"YES":"NO");
    }
    return 0;
}
