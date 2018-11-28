#include <stdio.h>
const double eps=1e-8;
int n;
int abs(int a) { if (a>0) return a; else return -a; }
int d[1100][1100], p[1100], x[1100], y[1100], z[1100];

int check(double ans)
{
    int i,j;//,t;
    double t;
    for (i=0;i<n;++i)
    for (j=i+1;j<n;++j)
    {
        //t=int(ans*p[i])+int(ans*p[j]);
        t=ans*(p[i]+p[j]);
        if (t<d[i][j]) return false;
    }
    return true;  
    
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int ca, cases=0, i, j;
    scanf("%d", &ca);
    while (ca--)
    {
        scanf("%d", &n);
        for (i=0;i<n;++i)
        scanf("%d%d%d%d", &x[i], &y[i], &z[i], &p[i]);
        for (i=0;i<n;++i)
        for (j=0;j<n;++j) d[i][j]=abs(x[i]-x[j])+abs(y[i]-y[j])+abs(z[i]-z[j]);
        double l=0, r=1e7, ans;
        while (r-l>eps)
        {
            double m=(l+r)/2;
            if (check(m)) { ans=m; r=m; } else l=m;           
        }
        printf("Case #%d: %.6lf\n", ++cases, ans);
    }
    return 0;
}
