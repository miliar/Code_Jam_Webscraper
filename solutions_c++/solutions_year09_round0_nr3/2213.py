#include<stdio.h>
#include<cstring>

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    char s[]=" welcome to code jam",ss[502];
    int n,i,w[502][22],j,ii;
    scanf("%d\n",&n);
    for(i=1;i<=n;i++)
    {
        //scanf("%s",ss+1);
        gets(ss+1);
        memset(w,0,sizeof(w));
        w[0][0]=1;
        for(j=1;ss[j];j++)
        {
            w[j][0]=1;
            for(ii=1;ii<=19;ii++)
            {
                w[j][ii]=w[j-1][ii];
                if(s[ii]==ss[j])
                {
                    w[j][ii]+=w[j-1][ii-1];
                    w[j][ii]%=10000;
                }
                //fprintf(stderr,"w[%d][%d]=%d\n",j,ii,w[j][ii]);
            }
        }
        printf("Case #%d: %0.4d\n",i,w[j-1][19]);
    }
    fprintf(stderr,"END");
    while(1);
    
    
    return 0;
}
