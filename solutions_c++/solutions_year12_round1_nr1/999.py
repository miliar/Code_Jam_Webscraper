#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
double p[1000000];
using namespace std;
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    int t,cases = 1;
    scanf("%d",&t);

    int a,b;
    double zhongjianbianliang;
    double ans;
    while(t--)
    {
        scanf("%d%d",&a,&b);
        p[0]=1;
        for(int i=1;i<=a;++i)
            scanf("%lf",&p[i]);
        zhongjianbianliang=1;
        ans=b+2;
        for(int i=0;i<=a;++i)
        {
            zhongjianbianliang *= p[i];
            double tem1 = (1-zhongjianbianliang)*((b+1)+(a-i)*2+b-a+1);
            double tem2 = ((a-i)*2+b-a+1)*zhongjianbianliang;
            if(ans>tem1+tem2) ans = tem1+tem2;
        }
        printf("Case #%d: %.6f\n",cases++,ans);
    }
    return 0;
}

