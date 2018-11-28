#include <stdio.h>
#define u 100000000

short ans[u+2];
long per[31],l,k,a,b,n;

int main()
{
    freopen("a-small.in","r",stdin);
    freopen("a-large.out","w",stdout);
    per[0] = 1;
    ans[0] = 0;
    for (l=1; l<=u; l++)
    {
        for (k=1; k<=30; k++)
        {
          per[k]^=1;
          if (per[k]) break;
        }
          
        for (k=1; k<=30; k++)
            if (!per[k]) { ans[l] = k-1; break; }
                    
    }
    scanf("%d",&n);
    for (l=0; l<n; l++)
    {
        scanf("%d%d",&a,&b);
        printf("Case #%d: ",l+1);
        if (ans[b]>=a) printf("ON\n"); else printf("OFF\n");
    }
    
    return 0;    
}
