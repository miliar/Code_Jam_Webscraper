#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int a[110][260];
int x[110];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out2.txt", "w", stdout);

    int tc, ti;
    scanf("%d", &tc);
    for(ti = 1; ti <= tc; ti++)
    {
        int del,ins,m,n;
        scanf("%d%d%d%d", &del, &ins, &m, &n);
        for(int i = 0; i < n; i++)
            scanf("%d", &x[i]);
        for(int i = 0; i <= n; i++)
            for(int j = 0; j <= 255; j++)a[i][j] = 0;

        for(int k = 0; k < n; k++)
        {
            if(m > 0)
            {
                for(int i = 0; i < 256; i++)
                {
                    for(int j = 0; j < i; j++)
                    {
                        if(a[k][i] > a[k][j] + (((i-j-1)/m)+1)*ins)
                            a[k][i] = a[k][j] + (((i-j-1)/m)+1)*ins;
                    }
                    for(int j = i+1; j < 256; j++)
                    {
                        if(a[k][i] > a[k][j] + (((j-i-1)/m)+1)*ins)
                            a[k][i] = a[k][j] + (((j-i-1)/m)+1)*ins;
                    }
                }
            }
            for(int i = 0; i < 256; i++)
                a[k+1][i] = a[k][i] + del;
            for(int i = 0; i < 256; i++)
            {
                int l = min(i+m, 255)+1;
                int M = 20000000;
                for(int j = max(0, i-m); j < l; j++)
                    if(a[k][j] < M)
                        M = a[k][j];
                M += abs(i-x[k]);
                if(a[k+1][i] > M)
                    a[k+1][i] = M;
            }

        }
        for(int i = 0; i < 256; i++)
        {
            for(int j = 0; j < i; j++)
            {
                if(a[n][i] > a[n][j] + (((i-j-1)>>1)+1)*ins)
                    a[n][i] = a[n][j] + (((i-j-1)>>1)+1)*ins;
            }
            for(int j = i+1; j < 256; j++)
            {
                if(a[n][i] > a[n][j] + (((j-i-1)>>1)+1)*ins)
                    a[n][i] = a[n][j] + (((j-i-1)>>1)+1)*ins;
            }
        }
        int ans = 0;
        for(int i = 0; i < 256; i++)
        {
            if(a[n][ans] > a[n][i])
                ans = i;
        }
        printf("Case #%d: %d\n", ti, a[n][ans]);
    }
    return 0;
}
