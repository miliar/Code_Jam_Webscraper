#include<stdio.h>
int main()
{
    int snapper[10],i,k,n,t,j,j0,j1,flag,count;
    scanf("%d",&t);
    for (i=1;i<=t;i++)
    {
       scanf("%d%d",&n,&k);
       for (j=0;j<n;j++) snapper[j]=0;
       for (j=0;j<k;j++)
       {
            count=0;
            flag=1;
            for (j0=0;flag&&j0<n;j0++) 
            {
                if (snapper[j0]==0) flag=0 ;
                count++;
            }
            for (j1=0;j1<count;j1++)
            if (snapper[j1]==0) snapper[j1]=1;
            else snapper[j1]=0;
            
       }
       flag=1;
       for (j0=0;flag&&(j0<n);j0++)  if (snapper[j0]==0) flag=0;
       if (flag) printf("Case #%d: ON\n",i);
       else printf("Case #%d: OFF\n",i);
    }
    return 0;
}


    
