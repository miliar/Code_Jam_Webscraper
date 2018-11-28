#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;

typedef long long LL;

int main()
{
    int t,cs,i,r,k,n,g[1005],f[1005],m[1005];
    LL ans;
    freopen("C:\\Users\\LL\\Desktop\\C-small-attempt1.in","r",stdin);
    freopen("C:\\Users\\LL\\Desktop\\1.out","w",stdout);
    scanf("%d",&t);
    for(cs=1;cs<=t;cs++)
    {
        printf("Case #%d: ",cs);
        scanf("%d%d%d",&r,&k,&n);
        int gsum=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&g[i]);
            gsum+=g[i];
        }
        if(gsum<=k)
        {
            printf("%I64d\n",LL(gsum)*r);
            continue;
        }
        memset(f,-1,sizeof(f));
        LL cur=0,time=0,sum=0,s;
        while(1)
        {
            if(f[cur]!=-1)
                break;
            f[cur]=time;
            m[cur]=sum;
            for(i=cur,s=0;;)
            {
                if(s+g[i]>k)
                    break;
                s+=g[i];
                i++;
                if(i==n)
                    i=0;
            }
            cur=i;
            sum+=s;
            time++;
            if(time==r)
            {
                ans=sum;
                goto ll;
            }
        }
        LL cycleSum=sum-m[cur],cycle=time-f[cur],cycleStart=cur,preSum=m[cur],preRound=f[cur];
        ans=preSum+LL(r-preRound)/cycle*cycleSum;
        r-=preRound;
        r%=cycle;
        while(1)
        {
            if(r==0)
                break;
            for(i=cur,s=0;;)
            {
                if(s+g[i]>k)
                    break;
                s+=g[i];
                i++;
                if(i==n)
                    i=0;
            }
            cur=i;
            ans+=s;
            r--;
            if(r==0)
                break;
        }
ll:     printf("%I64d\n",ans);
    }
}