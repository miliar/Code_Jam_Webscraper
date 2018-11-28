#include <cstdio>
#include <cstdlib>

int a[60][60];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {
        printf("Case #%d: ", ti);
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            for(int j = 0; j <= i; j++)
                scanf("%d", &a[i-j][j]);
        for(int i = n; i < 2*n-1; i++)
            for(int j = i-n+1;j < n; j++)
                scanf("%d", &a[i-j][j]);

        int h=n;
        for(int q = -n+1; q <= n-1; q++)
        {
            int good=1;
            for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
            {
                if(q+j>=0 && q+j<n && -q+i>=0 && -q+i<n)
                if(a[i][j] != a[j+q][i-q])good=0;
            }
            if(good)
                if(abs(q)< h)
                    h = abs(q);
        }
        int w=n;
        for(int q = 0; q <= 2*n-2; q++)
        {
            int good=1;
            for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
            {
                if(q-i>=0 && q-i<n && q-j>=0 && q-j<n)
                if(a[i][j] != a[q-j][q-i])good=0;
            }
            if(good)
                if(abs(q-n+1)< w)
                    w = abs(q-n+1);
        }
        //printf("%d %d ", h, w);
        int z = n+h+w;
        printf("%d\n",z*z-n*n);
    }
    return 0;
}
