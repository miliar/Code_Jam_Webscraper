#include <stdio.h>
#include <stdio.h> 
#include <process.h> 
FILE *stream; 
int main ()
{
    int i,j,k,l,m,n,ii,r,num,dang,p;
    int dui[1001];
    int na,na1;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf ("%d",&ii);
    for (i=0;i<ii;i++)
    {
        scanf ("%d%d%d",&r,&k,&n);
        na=0;
        num=0;
        for (j=0;j<n;j++)
        {
            scanf("%d",&dui[j]);
        }
        for (j=0;j<r;j++)
        {
            dang=0;
            na1=na;
            p=1;
            while (dang+dui[na]<=k)
            {
                if (na1==na&&p==0) break; 
                p=0;
                dang=dang+dui[na];
                
                na++;
                if (na==n) na=0;
            }
           
            
            num=num+dang;
        }        
        printf("Case #%d: %d\n",i+1,num);
    }


}
