#include <stdio.h>
#include <string.h>
char a[210][110];
int best,ans,t1,k,m,n,tmp,s;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t1);
    for (int t0=1;t0<=t1;t0++)
    {
        scanf("%d%d",&n,&m);
        ans=0;
        a[0][0]='/';a[0][1]=0;
        for (int i=1;i<=n+m;i++)
        {
            scanf("%s",a[i]);
            tmp=strlen(a[i]);
            a[i][tmp]='/';a[i][tmp+1]=0;
             
            best=10000; 
            for (int j=0;j<i;j++)
            {
                k=0;
                while (a[i][k]&&a[j][k]&&a[i][k]==a[j][k]) k++;
                if (a[i][k]==0)
                {
                    best=0;
                    break;
                }
                s=0;
                for (;a[i][k];k++) 
                  if (a[i][k]=='/') s++;
                if (s<best) best=s;
            }                     
            if (i>n) ans+=best;
                          
        }
            printf("Case #%d: %d\n",t0,ans);
        
    }
    
}
