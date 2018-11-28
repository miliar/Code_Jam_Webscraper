#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define max(a,b)    a>b?a:b;
#define min(a,b)    a<b?a:b;
#define INF 0x3fffffff
char in[105][105];
double wp[105],owp[105],oowp[105];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%s",&in[i][1]);
        }
        for(int i=1;i<=n;i++)
        {
            int a=0,b=0;
            for(int j=1;j<=n;j++)
            {
                if(in[i][j]!='.')
                {
                    b++;
                    if(in[i][j]=='1')   a++;
                }
            }
            wp[i]=a*1.0/b;
        }
        for(int i=n;i>=1;i--)
        {
            owp[i]=0;
            int down=0;
            for(int j=1;j<=n;j++)
            {
                if(i!=j&&in[i][j]!='.')
                {
                    down++;
                    int a=0,b=0;
                    for(int k=1;k<=n;k++)
                    {
                        if(k!=i&&in[j][k]!='.')
                        {
                            b++;
                            if(in[j][k]=='1')    a++;
                        }
                    }
                    owp[i]=owp[i]+a*1.0/b;
                }
            }
            owp[i]=owp[i]/down;
            //printf("opw[%d]:%g\n",i,owp[i]);
        }
        for(int i=1;i<=n;i++)
        {
            oowp[i]=0;
            int down=0;
            for(int j=1;j<=n;j++)
            {
                if(i!=j&&in[i][j]!='.')
                {
                    down++;
                    oowp[i]=oowp[i]+owp[j];
                }
            }
            oowp[i]=oowp[i]/down;
        }
        printf("Case #%d:\n",cas);
        for(int i=1;i<=n;i++)
        {
            double ans=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
            printf("%f\n",ans);
        }
    }
    return 0;
}
