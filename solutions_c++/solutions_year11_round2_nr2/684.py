#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int c;
double d,p[260];
int v[260];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ft = 1;ft <= t;ft++)
    {
        scanf("%d%lf",&c,&d);
        int tot = 0;
        for (int i = 1;i <= c;i++)
        {
            scanf("%lf%d",&p[i],&v[i]);
            tot += v[i];
        }
        double l,r,mid,left;
        l = 0.0;
        r = 1e13;
        while (fabs(l-r) > 1e-7)
        {
            mid = (l+r)/2.0;
            left = p[1]-mid;
            //cout << l << ' ' << r << ' ' << mid << ' ' << left << ' ' << d << endl;
            bool flag = true;
            for (int i = 1;i <= c;i++)
                for (int j = (i==1)?2:1;j <= v[i];j++)
                {
                    if (left+d >= p[i])
                    {
                        if (left+d-p[i] > mid)  flag = false;
                        left = left+d;
                    }
                    else if (p[i]-mid <= left+d)
                        left = left+d;
                    else if (p[i]-mid > left+d)
                        left = p[i]-mid;
                    //cout << i << ' ' << j << ' ' << p[i] << ' ' << left << endl;
                }
            if (left > p[c]+mid)    flag = false;
            if (flag == false)  l = mid;
            else r = mid;
        }
        printf("Case #%d: %.7f\n",ft,l);
    }
}
