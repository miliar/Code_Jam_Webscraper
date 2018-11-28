#include<iostream>
#include<cstdio>

using namespace std;
const int maxn=2000001;
int dp[maxn];
struct In
{
    int x,y;
} s[10000000];
int p;
int mat[1100];
int main()
{
    int i,j,n,m=1,t,sum,temp,ans,ss;
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        sum=0;
        ss=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&mat[i]);
            sum=sum^mat[i];
            ss+=mat[i];
        }
        for(i=0;i<maxn;i++)
        {
            dp[i]=-1;
        }
        dp[0]=0;
        for(i=0;i<n;i++)
        {
            p=0;
            for(j=maxn-1;j>=0;j--)
            {
                temp=j^mat[i];
                if(dp[j]!=-1&&temp>=0&&temp<maxn&&dp[temp]<dp[j]+mat[i])
                {
                    s[p].x=temp;
                    s[p++].y=dp[j]+mat[i];
                }
            }
            for(j=0;j<p;j++)
            {
                dp[s[j].x]=s[j].y;
            }
        }
        ans=0;
        for(i=maxn-1;i>0;i--)
        {
            if(dp[i]>0&&dp[i]!=ss&&i==int(sum^i))
            {
                if(ans<dp[i])
                    ans=dp[i];
            }
        }
        if(ans==0)
        {
            printf("Case #%d: NO\n",m++);
        }
        else
        {
            printf("Case #%d: %d\n",m++,ans);
        }
    }
}
