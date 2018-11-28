#include<stdio.h>
#include<string.h>
#define _cls(x) memset(x,0,sizeof(x))
char base[]=" welcome to code jam";
char str[510];
int f[510][20];
int main()
{
    int t;
    freopen("c-large.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d",&t);gets(str);
    for (int tt=1;tt<=t;tt++)
    {
        gets(str+1);
        _cls(f);
        int len=strlen(str+1);
        for (int i=1;i<=len;i++)
            if (str[i]==base[1])
                f[i][1]=1;
        for (int j=2;j<=19;j++)
            for (int i=j;i<=len;i++)
                if (str[i]==base[j])
                for (int k=j-1;k<i;k++)
                    if (base[j-1]==str[k] && f[k][j-1])
                    {
                        f[i][j]+=f[k][j-1];
                        f[i][j]%=10000;
                    }
        int sum=0;
        for (int i=19;i<=len;i++)
            sum=(sum+f[i][19])%10000;
        printf("Case #%d: %04d\n",tt,sum);
                
    }
}