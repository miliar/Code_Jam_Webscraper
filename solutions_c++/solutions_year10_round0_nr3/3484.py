#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int cases,t;
    scanf("%d",&cases);
    int snapper[50];
    for(t=1;t<=cases;t++)
    {
        int n,k,i,j;
        scanf("%d %d",&n,&k);
        if(k%2 == 0)
            printf("Case #%d: OFF\n",t);
        else
        {
            for(i=0;i<=n;i++)
               snapper[i] = 0;
            for(i=1;i<=k;i++)
            {
               if(i%2)
                   snapper[1]=1;
               else
               {
                   for(j=1;j<=n;j++)
                   {
                      if(snapper[j]==1)
                         snapper[j] = 0;
                      else 
                      {
                          snapper[j] = 1;
                          break;
                      }
                   }
               }
            }
            for(i=1;i<=n;i++)
            {
               if(snapper[i] == 0)
                      break;
            }
            if(i == n+1)
               printf("Case #%d: ON\n",t);   
            else
               printf("Case #%d: OFF\n",t);
        }
    }
    return 0;
}
