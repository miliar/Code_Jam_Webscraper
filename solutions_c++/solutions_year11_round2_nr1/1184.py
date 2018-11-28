#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t,n;
char mp[110][110];
double ans[110];
double wp[110],owp[110],oowp[110];
int win[110],num[110];

int sol(char c)
{
    if(c=='1')
        return 1;
    if(c=='0')
        return 0;
    return -1;
}



int main()
{
    freopen("A-large.in","r",stdin);
    freopen("al1.txt","w",stdout);
    int i,j,k;
    scanf("%d",&t);
    int cnt=1;
    while(t--)
    {
        printf("Case #%d:\n",cnt++);
        memset(ans,0,sizeof(ans));
        memset(wp,0,sizeof(wp));
        memset(owp,0,sizeof(owp));
        memset(oowp,0,sizeof(oowp));
        memset(win,0,sizeof(win));
        memset(num,0,sizeof(num));
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%s",mp[i]);
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(sol(mp[i][j])!=-1)
                    num[i]++;
                if(sol(mp[i][j])==1)
                    win[i]++;
            }
            wp[i]=(double)0.25*win[i]/num[i];
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(sol(mp[j][i])==1)
                    owp[i]+=(double)(win[j]-1)/(num[j]-1)/num[i];
                if(sol(mp[j][i])==0)
                    owp[i]+=(double)win[j]/(num[j]-1)/num[i];
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(sol(mp[i][j])!=-1)
                    oowp[i]+=owp[j]/num[i];
            }
        }
        for(i=0;i<n;i++)
        {
            printf("%.9lf\n",wp[i]+0.5*owp[i]+0.25*oowp[i]);
            
            
        }
    }
    //system("pause");
    return 0;
}
