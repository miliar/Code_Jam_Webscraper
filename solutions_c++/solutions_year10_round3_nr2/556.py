#include <stdio.h>
#include <math.h>


int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int t,o,ans;
    double a,b,c,x,y;
    scanf("%d",&t);
    for(o=1;o<=t;o++)
    {
        scanf("%lf %lf %lf",&a,&b,&c);
        x=log(b/a)/log(c);
        y=log(x)/log(2.0);
        ans=y;
        if(ans<0)
        {
            ans=0;
        }
        else
        {
            if(y-ans>1e-8)
            {
                ans++;
            }
        }
        printf("Case #%d: %d\n",o,ans);
    }
    return 0;
}
        
