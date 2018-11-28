#include <cstdio>

int a1,a2,b1,b2;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int run=1;run<=T;run++)
    {
        scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
        int ans=0;
        for (int i=a1;i<=a2;i++)
            for (int j=b1;j<=b2;j++)
            {
                int a=i,b=j;
                if (a<b)
                {
                    a=j;
                    b=i;
                }
                int r=0; bool ok=1;
                while (b)
                {
                     r++;
                     if (a/b>1)
                     {
                         if (r&1) ans++;
                         ok=0;
                         break;
                     }
                     int t=b;
                     b=a%b;
                     a=t;
                }
                if (ok&&r%2==0) ans++;
            }
        printf("Case #%d: %d\n",run,ans);
    }
    return 0;
} 
        
