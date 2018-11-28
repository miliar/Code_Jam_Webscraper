#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;
int A[1005],B[1005];
int main()
{
    freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    __int64 P,L,c;
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int ans=0;
        cas++;
        scanf("%I64d%I64d%I64d",&L,&P,&c);
        int t=0;
        while(L<P)
        {
            t++;
            L*=c;
        }
        if(t>0)
            ans=ceil(log((double)t)/log(2.0));
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
