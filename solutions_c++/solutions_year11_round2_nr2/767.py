#include <stdio.h>
#include <algorithm>
using namespace std;

#define eps 1e-7

int a[1000005];
double now[1000005];
int up,d;

double Abs(double t)
{
    return t>0?t:-t;       
}

bool Check(double t)
{
    int i;
    now[0]=a[0]-t;
  //  printf("%lf..\n",now[0]);
    for (i=1;i<up;i++)
    { 
        now[i]=now[i-1]+d;
        if (Abs(now[i]-a[i])>t)
        {
            if (a[i]-t>now[i])
            {
                now[i]=a[i]-t;  
          //      printf("%d..\n",a[i]);                
            }                      
            else return false;
        }
   //     printf("%lf..\n",now[i]);
    }    
    return true;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int i,j,n,T,cnt,c,p;
    double l,r,mid;
    scanf("%d",&T);
    cnt=1;
    while(T--)
    {
        scanf("%d%d",&n,&d);
        up=0;
        for (i=0;i<n;i++)
        {
            scanf("%d%d",&p,&c);
            for (j=0;j<c;j++)
            {
                a[up++]=p;
            }    
        }        
        sort(a,a+up);
        l=up*d;
        r=0;
    //    printf("%lf..%lf\n",l,r);
        while((l-r)>eps)
        {
        //     printf("%lf..%lf\n",l,r);
             mid=(l+r)/2;
             if (Check(mid)==true) l=mid;
             else r=mid;
        }
        printf("Case #%d: %lf\n",cnt++,mid);  
    }
    return 0;
        
}
