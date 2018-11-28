#include <stdio.h>
#define u 1048576

int t,i,n,l,m[2000],k;

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    scanf("%d",&t);
    
    for (int i = 1; i <= t; i++)
    {
        scanf("%d",&n);
        for (l=0; l<n; l++) scanf("%d",&m[l]);
        int x1, x2,ans = -1, s;
        for (l=1; l<(1<<n)-1; l++)
        {
            x1 = 0; x2 = 0; s = 0;
            for (k=0; k<n; k++)
                if (l & (1<<k)) { x1 ^= m[k]; s += m[k]; } else x2 ^=m[k];
            
            if (x1==x2 && ans < s) ans = s;
        }
        
        
        printf("Case #%d: ",i);
        if (ans==-1) puts("NO");
        else printf("%d\n",ans);
    }
}
