#include <iostream>
#include <cstring>

using namespace std;

#define N 1001

int main()
{
    freopen ("2.in","r",stdin);
    freopen ("2.out","w",stdout);
    long long group[N];
    long long t,n,k,r;
    long long earn[N],round[N];
    scanf("%I64d",&t);
    for(int cntc=0;cntc<t;cntc++)
    {
        scanf("%I64d%I64d%I64d",&r,&k,&n);
        memset(earn,0,sizeof(earn));
        memset(round,0,sizeof(round));
        long long sum=0;
        for(int i=0;i<n;i++)
        {
            scanf("%I64d",&group[i]);
            sum+=group[i];
        }
        if(sum<=(long long)k)
        {
            printf("Case #%d: %I64d\n",cntc+1,sum*r);
            continue;
        }
        int flag=1;
        long long ans=0;
        long long cntr=1,nowp=0;
        round[0]=1;
        earn[0]=0;
        for(int i=0;;i++)
        {
            if(nowp+group[i%n]<=k)
                nowp+=group[i%n];
            else
            {
              //  printf("%d\n",i%n);
                cntr++;
                ans+=nowp;
                nowp=group[i%n];
                if(round[(i)%n]&&flag)
                {
                    ans+=(ans-earn[(i)%n])*((r-cntr+1)/(cntr-round[(i)%n]));
                    cntr=r-(r-cntr+1)%(cntr-round[(i)%n])+1;
                    flag=0;
                }
                if(!round[(i)%n])
                {
                    round[(i)%n]=cntr;
                    earn[(i)%n]=ans;
                }
                if(cntr>r)
                    break;
            }
        }
        printf("Case #%d: %I64d\n",cntc+1,ans);
    }
    return (0);
}

