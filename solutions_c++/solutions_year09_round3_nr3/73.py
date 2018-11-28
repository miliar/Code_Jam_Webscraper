#include <stdio.h>
#include <string>

int T, C, n, m, i, j, k, l;
int a[10100], b[110], d[110][110], s[110];

int main()
{
    freopen("c_in.txt", "r", stdin);
    freopen("c_out.txt", "w", stdout);
    scanf("%d", &T);
    for (C=1; C<=T; C++)
    {
        scanf("%d %d", &n, &m);
        memset(a, 0, sizeof(a)); memset(b, 0, sizeof(b)); memset(d, 0, sizeof(d));
        for (i=0; i<m; i++) { scanf("%d", &k); a[k] = 1; }
        k = 1;
        for (i=1; i<=n; i++) if (a[i]) { s[k] = i; k ++; } else b[k] ++;
        s[m + 1] = n + 1;
        for (j=0; j<=m; j++) for (i=1; i+j<=m; i++)
        {
            if (j==0) { d[i][i] = b[i] + b[i + 1]; continue; }
            l = -1;
            for (k=i; k<=i+j; k++) if (l<0 || d[i][k-1]+d[k+1][i+j]<l) l = d[i][k - 1] + d[k + 1][i + j];
            d[i][i + j] = l + s[i + j + 1] - 2 - s[i - 1];
        }
        printf("Case #%d: %d\n", C, d[1][m]);
    }
}

