#include <stdio.h>
#include <string.h>
#include <memory.h>
char *a="welcome to code jam";
int tests;
char b[510];
int f[20][510];
int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    int n=strlen(a),m;
    scanf("%d",&tests);
    gets(b);
    for (int t0=1;t0<=tests;t0++)
    {
        gets(b);
        m=strlen(b);
        memset(f,0,sizeof(f));

        for (int i=0;i<m;i++)
            if (a[0]==b[i]) f[0][i]=1;
        for (int j=1;j<n;j++)
          for (int i=0;i<m;i++)
            if (a[j]==b[i])
                for (int k=0;k<i;k++)
                {
                    f[j][i]+=f[j-1][k];
                    if (f[j][i]>=10000) f[j][i]-=10000;
                }
        int ans=0;
        for (int i=0;i<m;i++) ans+=f[n-1][i];
        printf("Case #%d: %04d\n",t0,ans%10000);

    }
}
