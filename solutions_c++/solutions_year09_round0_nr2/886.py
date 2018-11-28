#include <stdio.h>
#include <algorithm>

using namespace std;

const int aa[4][2] = {-1,0,  0,-1,  0,1,  1,0};

int T, C, n, m, i, j, k, x, y, r, c, Min, l, s;
int a[110][110], b[11000], g[11000], d[11000];

bool cmp(int x, int y)
{
    return a[x/m][x%m]<a[y/m][y%m];
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.ans", "w", stdout);
    scanf("%d", &T);
    for (C=1; C<=T; C++)
    {
        scanf("%d %d", &n, &m);
        for (i=0; i<n; i++) for (j=0; j<m; j++) scanf("%d", &a[i][j]);
        for (i=0; i<n*m; i++) g[i] = b[i] = i;
        sort(b, b + n * m, cmp);
        for (i=0; i<n*m; i++)
        {
        	x = b[i] / m; y = b[i] % m; Min = a[x][y]; l = b[i];
        	for (j=0; j<4; j++)
        	{
             	r = x + aa[j][0]; c = y + aa[j][1];
             	if (r<0 || r>=n || c<0 || c>=m) continue;
             	if (a[r][c]<Min) { Min = a[r][c]; l = r * m + c; }
        	}
        	g[b[i]] = g[l];
        }
        memset(d, 0, sizeof(d));
        printf("Case #%d:\n", C);
        s = 0;
        for (i=0; i<n; i++)
            for (j=0; j<m; j++)
            {
                if (d[g[i*m+j]]==0) { s ++; d[g[i*m+j]] = s; }
                printf("%c", 'a' + d[g[i*m+j]] - 1);
                if (j<m-1) printf(" "); else printf("\n");
            }
    }
}

