#include<stdio.h>
using namespace std;
int a,b,c,d,e,f;
int zz[105];
int main()
{
    //freopen("harmony.in","r",stdin);
    //freopen("harmony.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        scanf("%d%d%d",&c,&d,&e);
        for(f=1;f<=c;f++)
             scanf("%d",&zz[f]);
        bool bole=0;
        while(d<=e)
        {
           bole=1;
           for (f=1;f<=c;f++)
           {
               if (zz[f]<d)
               {
                  if (d%zz[f]!=0)
                     bole=0;            
               }
               else
               {
                   if (zz[f]%d!=0)
                      bole=0;
               }    
           }
           if (bole==0)
              d++;
           else
               break;          
        }
        if (bole)
           printf("Case #%d: %d\n",b,d);
        else
            printf("Case #%d: NO\n",b);
    }
}
