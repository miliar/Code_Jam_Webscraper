#include <stdio.h>

int main()
{
    int tt[2][1500]={0};
    int i,j,k,l,trt,na,nb,cas,deph,depm,arrh,arrm;
    
    scanf("%d",&i);
    for(cas=1;cas<=i;cas++)
    {
            scanf("%d %d %d",&trt,&na,&nb);
            while (na--)
            {
                  scanf("%d:%d %d:%d",&deph,&depm,&arrh,&arrm);
                  k=arrh*60+arrm+trt-1;
                  for (j=deph*60+depm;j<1440;j++)
                  {
                      tt[0][j]--;
                      if (j>k) tt[1][j]++;
                  }
            }
            while (nb--)
            {
                  scanf("%d:%d %d:%d",&deph,&depm,&arrh,&arrm);
                  k=arrh*60+arrm+trt-1;
                  for (j=deph*60+depm;j<1440;j++)
                  {
                      tt[1][j]--;
                      if (j>k) tt[0][j]++;
                  }
            }
            k=0;
            l=0;
            for (j=0;j<1440;j++)
            {
                 if (tt[0][j]<k) {k=tt[0][j];}
                 if (tt[1][j]<l) l=tt[1][j];
                 tt[1][j]=tt[0][j]=0;
            }
            printf("Case #%d: %d %d",cas,-k,-l);
            (cas<i) && printf("\n");
    }
    return 0;
}
