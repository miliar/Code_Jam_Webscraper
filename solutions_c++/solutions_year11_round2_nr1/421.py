#include<iostream>
#include<stdio.h>
using namespace std;

int i,j,k,t,n;
char s[102];
int f[102][102];
int total[102],win[102];
double ans[102];
double wp[102],owp[102],oowp[102];

int main()
{
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        memset(f,-1,sizeof(f));
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%s",s);
            total[i]=0;
            win[i]=0;
            for(j=1;j<=n;j++)
            {
                if(s[j-1]=='1')
                {
                    win[i]++;
                    f[i][j]=1;
                }
                else
                if(s[j-1]=='0')
                    f[i][j]=0;
                if(s[j-1]!='.')
                    total[i]++;
            } 
            wp[i]=double(win[i])/double(total[i]);
            //printf("wp: %.8f\n",wp[i]);
            ans[i]=wp[i]*0.25; 
        }
        for(i=1;i<=n;i++)
        {
            wp[i]=0.0;
            for(j=1;j<=n;j++)
            {
                if(f[i][j]!=-1)
                {
                    wp[i]+=double(win[j]-f[j][i])/double(total[j]-1);
                }
            }
            owp[i]=wp[i]/double(total[i]);
            //printf("owp: %.8f\n",owp[i]);
            ans[i]+=owp[i]*0.5;
        }
        for(i=1;i<=n;i++)
        {
            oowp[i]=0.0;
            for(j=1;j<=n;j++)
            {
                if(f[i][j]!=-1)
                {
                    oowp[i]+=owp[j];
                }      
            }   
            oowp[i]=oowp[i]/double(total[i]);
            //printf("oowp: %.8f\n",oowp[i]);
            ans[i]+=oowp[i]*0.25;
        }
        printf("Case #%d:\n",k);
        for(i=1;i<=n;i++)
            printf("%.12f\n",ans[i]);
    }
    
    return 0;
}
