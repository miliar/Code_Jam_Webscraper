#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#define MAX 300
#define boro 1<<16
#define mem(a,b) memset(a,b,sizeof a)

using namespace std;

int n;
int candy[MAX];
//int dp[(1<<16)][MAX];

int rec(int mask,int item)
{
    //int &ret=dp[mask][item];

    if(item==n )
    {

        if(__builtin_popcount(mask)==0 || __builtin_popcount(mask)==n) return 0;
//        printf("mask %d n=%d \n",mask,n);
        int kid_1=0,kid_2=0,sum_1=0,sum_2=0,i;

        for( i=0;i<n;i++)
        {
            if((mask&(1<<i)))
            {
                kid_1=(kid_1^candy[i]);
                sum_1+=candy[i];
            }
            else
            {
                kid_2= (kid_2^candy[i]);
                sum_2+=candy[i];
             }
        }
//        printf("kd_1 %d kd_2 %d s_1 %d s_2 %d  \n",kid_1,kid_2,sum_1,sum_2);

        if(kid_1==kid_2)
        {
                return max(sum_1,sum_2);
        }
        else return 0;
    }

    int ret=max(rec(mask|(1<<item) , item+1),rec(mask,item+1) );

    return ret;
}
int main(void)
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);

    int loop,i,ans,cas=0;
    scanf("%d",&loop);
    while(loop--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&candy[i]);
        }
//        for(i=0;i<n;i++) printf("intial  %d \n",candy[i]);
        //mem(dp,-1);
        ans=rec(0,0);
        if(ans==0) printf("Case #%d: NO\n",++cas);
        else printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
