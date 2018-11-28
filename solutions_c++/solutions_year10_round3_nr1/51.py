#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;
int A[1005],B[1005];
int main()
{
    freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,i,j,cas=0,N;
    scanf("%d",&T);
    while(T--)
    {
        int ans=0;
        cas++;
        scanf("%d",&N);
        for(i=1;i<=N;i++) scanf("%d%d",&A[i],&B[i]);
        for(i=1;i<=N;i++)
        {
            for(j=i+1;j<=N;j++)
            {
                if(A[i]>A[j]&&B[i]<B[j]) ans++;
                if(A[i]<A[j]&&B[i]>B[j]) ans++;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
