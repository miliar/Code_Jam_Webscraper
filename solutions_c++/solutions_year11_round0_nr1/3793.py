#include<cstdio>
#include<cmath>
int main()
{
    int cas,n,t,i,j;
    char c;

   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
    
    scanf("%d",&cas);
    for(j = 1;j <= cas;j++)
    {
       scanf("%d",&n);
       int od = 1;
       int ot = 0;
       int bd = 1;
       int bt = 0;
       for(i = 1;i <= n;i++)
       {
           do{
               scanf("%c",&c);
           }while(c == ' ');
           scanf("%d",&t);
      //     scanf("%c%d",c,&t);
           if(c == 'O')
           {
               int tmp = bt - ot;
               int ab = t - od > 0 ? t - od : od - t;
               if(tmp > 0)
               {
                   if(tmp >= ab)
                       ot = bt + 1;
                   else
                       ot = bt + (ab - tmp + 1);
               }
               else
                   ot += (ab + 1);
               od = t;
           //    printf("The step %d is O %d\n",i,ot);
           }
           else if(c == 'B')
           {
               int tmp = ot - bt;
               int ab = t - bd > 0 ? t - bd : bd - t;
               if(tmp > 0)
               {
                   if(tmp >= ab)
                       bt = ot + 1;
                   else
                       bt = ot + (ab - tmp + 1);
               }
               else
                   bt +=  (ab + 1);
               bd = t;
           //    printf("The step %d is B %d\n",i,bt);
           }
       }
       int ans = bt;
       if(ot > ans)
           ans = ot;
       printf("Case #%d: %d\n",j,ans);
        
    }

    return 0;
}
