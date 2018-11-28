#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>

#define INF 2000000000
#define LIM 100001

using namespace std;

int t,iii;
long long l,n,i,j,k;
long long b[105];
long long ans;
long long mic[1000005];

int main()
{
    scanf("%d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%I64d",&l);
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&b[i]);
        }
        for(k=0;k<LIM;k++)
        {
            mic[k]=-1;
        }
        mic[0]=0;
        for(i=0;i<n;i++)
        {
            for(j=b[i];j<LIM;j++)
            {
                if(mic[j-b[i]]!=-1&&(mic[j]==-1||mic[j]>mic[j-b[i]]+1))
                mic[j]=mic[j-b[i]]+1;
            }
        }
        ans=-1;
        for(i=0;i<n;i++)
        {
            for(j=0;j<LIM;j++)
            {
                if((l-j)%b[i]==0)
                {
                    if(mic[j]!=-1&&(((l-j)/b[i]+mic[j])<ans||ans==-1))
                    ans=((l-j)/b[i]+mic[j]);
                }
            }
        }
        printf("Case #%d: ",iii);
        if(ans==-1)
        printf("IMPOSSIBLE\n");
        else
        printf("%I64d\n",ans);
    }
    return 0;
}
