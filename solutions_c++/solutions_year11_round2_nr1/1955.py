#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large(1).in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j,k,l,t,kase=1,cnt,x,n,tmp,cn;
    double wp[1000],owp[1000],oowp[1000],sum;
    char s[1000][1000];
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d",&n);
        gets(s[0]);
        for (i=0;i<n;i++)
            gets(s[i]);
        //WP
        for (i=0;i<n;i++)
        {
            cnt=0;
            x=0;
            for (j=0;j<n;j++)
            {
                if (s[i][j]=='0' || s[i][j]=='1')
                {
                    cnt++;
                }
                if (s[i][j]=='1')
                    x++;
            }
            wp[i]=(double)x/(double)cnt;
            //printf("wp<<%d<<%lf\n",i,wp[i]);
        }
        //OWP
        for (i=0;i<n;i++)
        {
            sum=0;
            cn=0;
            for (j=0;j<n;j++)
            {
                if (s[i][j]=='0' || s[i][j]=='1')
                {
                    cn++;

                    cnt=0;
                    x=0;
                    tmp=j;
                    for (k=0;k<n;k++)
                    {
                        if (k==i)
                            continue;
                        if (s[tmp][k]=='0' || s[tmp][k]=='1')
                        {
                            cnt++;
                        }
                        if (s[tmp][k]=='1')
                            x++;
                    }
                    sum+=((double)x/(double)cnt);
                }
            }
            owp[i]=(double)sum/(double)cn;
            //printf("owp<<%d<<%lf\n",i,owp[i]);
        }
        //oowp
        for (i=0;i<n;i++)
        {
            sum=0;
            cnt=0;
            for (j=0;j<n;j++)
            {
                 if(s[i][j]=='0' || s[i][j]=='1')
                 {
                 sum+=owp[j];
                 cnt++;
                 }
            }
            oowp[i]=((double)sum/(double)cnt);
            //printf("oowp<<%d<<%lf\n",i,oowp[i]);
        }
        printf("Case #%d:\n",kase++);
        for(i=0;i<n;i++)
        {
            sum=0;
            sum=0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
            printf("%lf\n",sum);
        }

    }
    return 0;
}
