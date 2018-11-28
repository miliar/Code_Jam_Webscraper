#include<cstdio>
#include<cstring>
#include<cstdlib>
int a[1000];
int f[21][4000000],p[21][4000000],ans1[100],ans2[100];
int lp,tst,n,i,j,a1,a2,now;

int main(void)
{
    scanf("%d",&tst);
    for (lp=0;lp<tst;lp++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
            scanf("%d",&a[i]);
        memset(f,0,sizeof(f));
        for (i=0;i<n;i++)
        {
            for (j=-2000000;j<=2000000;j++)
            {
                if (j!=0&&f[i][j+2000000]==0) continue;
                f[i+1][j+a[i]+2000000]=1;
                p[i+1][j+a[i]+2000000]=1;
                f[i+1][j-a[i]+2000000]=1;
                p[i+1][j-a[i]+2000000]=2;
                if (j!=0||f[i][j+2000000]==1)
                {
                    f[i+1][j+2000000]=1;
                    p[i+1][j+2000000]=0;
                }
            }
        }
        a1=-1;a2=-1;
        if (f[n][0+2000000]==1)
        {
            now=0;
            for (i=n;i>0;i--)
            {
                if (p[i][now+2000000]==1)
                {
                    a1++;
                    ans1[a1]=a[i-1];
                    now-=a[i-1];
                    continue;
                }
                if (p[i][now+2000000]==2)
                {
                    a2++;
                    ans2[a2]=a[i-1];
                    now+=a[i-1];
                    continue;
                }
            }
            printf("Case #%d:\n",lp+1);
            for (i=0;i<=a1;i++)
            {
                if (i!=0) printf(" ");
                printf("%d",ans1[i]);
            }
            printf("\n");
            for (i=0;i<=a2;i++)
            {
                if (i!=0) printf(" ");
                printf("%d",ans2[i]);
            } 
            printf("\n");
        } else printf("Impossible\n");
    }
    return 0;
}
