#include<stdio.h>
#include<cstring>
char b[1000][1000];
int main()
{
    int t,n,i,j,k;
    freopen("GAL.in","r",stdin);
    freopen("GAL.out","w",stdout);
    scanf("%d",&t);getchar();
    for(int cn=1;cn<=t;cn++)
    {
        scanf("%d",&n);getchar();
        for(i=0;i<n;i++)scanf("%s",b[i]);
        double wp[1000],owp[1000],oowp[1000];
        for(i=0;i<n;i++)
        {
            double p=0,w=0;
            for(j=0;j<n;j++)
            {
                if(b[i][j]!='.')p++;
                if(b[i][j]=='1')w++;
            }
            wp[i]=w/p;
            //printf("%f\n",wp[i]);
            double sum=0,num=0;

            for(j=0;j<n;j++)
            {
                p=w=0;
                if(b[j][i]!='.')
                {
                    num++;
                    for(k=0;k<n;k++)
                    {
                        if(k==i)continue;
                        if(b[j][k]!='.')p++;
                        if(b[j][k]=='1')w++;
                    }
                    sum+=w/p;
                }
            }
            sum/=num;
            owp[i]=sum;
            //printf("%f\n",owp[i]);
        }
        for(i=0;i<n;i++)
        {
            double sum=0,p=0;
            for(j=0;j<n;j++)
            {
                if(b[i][j]!='.')
                {
                    sum+=owp[j];
                    p++;
                }
            }
            oowp[i]=sum/p;
        }
        printf("Case #%d: \n",cn);
        for(i=0;i<n;i++)
        {
            printf("%f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
        }
    }
    return 0;
}
