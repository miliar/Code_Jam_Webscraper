#include <stdio.h>
#include <string.h>
long long points[3][3];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long ca, cases=0, i, j , n, k, a, b, c, d, x0, y0, m, x, y, tot;
    scanf("%I64d", &ca);
    while (ca--)
    {
        scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d", &n, &a, &b, &c, &d, &x0, &y0, &m);
        x=x0;
        y=y0;
        memset(points, 0, sizeof(points));
        points[x%3][y%3]++;
        for (i=1;i<n;++i)
        {
            x=(a*x+b)%m;
            y=(c*y+d)%m;
            points[x%3][y%3]++;
        }
        tot=0;
        for (i=0;i<9;++i)
        for (j=i;j<9;++j)
        for (k=j;k<9;++k)
        if (((i%3)+(j%3)+(k%3))%3==0 && ((i/3)+(j/3)+(k/3))%3==0) 
        {
            if (i==j && j==k)
                tot+=points[i%3][i/3]*(points[i%3][i/3]-1)*(points[i%3][i/3]-2)/6;
            else if (i==j) 
                tot+=points[i%3][i/3]*(points[i%3][i/3]-1)/2*points[k%3][k/3];
            else if (j==k)
                tot+=points[j%3][j/3]*(points[j%3][j/3]-1)/2*points[i%3][i/3];
            else
                tot+=points[i%3][i/3]*points[j%3][j/3]*points[k%3][k/3];
        }
        printf("Case #%I64d: %I64d\n", ++cases, tot);
    }
    return 0;
}
