#include <stdio.h>
#include <string.h>

int a[200];
int p;
int d[110][110][110];

bool dp(int i,int n,int m) {
    if (i == 0 && n == 0 && m == 0) return true;
    if (i < 0 || m < 0 || n < 0) return false;
    if (i < m || i < n) return false;
    if (d[i][n][m] != -1) return d[i][n][m];
    if (a[i] > 3*(p-1) ) {
       if (dp(i-1,n-1,m))
          return d[i][n][m]=true;
       if (a[i]>=2&&dp(i-1,n-1,m-1))
          return d[i][n][m]=true;
    } 
    else if (a[i] == 3*(p-1)) {
       if ( a[i]>=2 && dp(i-1,n-1,m-1) ) {
           return d[i][n][m]=true;
       }
       if (dp(i-1,n,m)) return d[i][n][m]=true;
    }
    else if (a[i] == 3*(p-1)-1) {
       if ( a[i]>=2 && dp(i-1,n-1,m-1) )
          return d[i][n][m]=true;
       if ( dp(i-1,n,m) ) return d[i][n][m]=true;
    }
    else {
        if ( dp(i-1,n,m) ) return d[i][n][m]=true;
        if (a[i] >= 2 && dp(i-1,n,m-1)) return d[i][n][m]=true;
    }
    return d[i][n][m]=false;
}

int main() {
    int kase, n, m;
    int count = 1;
    freopen("B-large.in","r",stdin);
    freopen("yy.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
        scanf("%d %d %d", &n, &m, &p);
        memset(d,-1,sizeof(d));
        for (int i = 1; i <= n; ++i) {
            scanf("%d",&a[i]);
        }
        int i;
        for (i = n; i > 0; --i) {
            if ( dp(n,i,m) ) break;
        }
        printf("Case #%d: %d\n",count++,i);
    }
    return 0;
}
