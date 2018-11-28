#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

//long long x[1000500];
long long L,t,N,C,a[10010];

int main()
{
    int T;
    scanf("%d",&T);
    for (int q=1;q<=T;++q)
    {
        scanf("%lld%lld%lld%lld",&L,&t,&N,&C);
        for (int i=0;i<C;++i)
            scanf("%lld",a+i);
        long long ans = 0;
        vector<long long> x;
        for (int i=0;i<N;++i)
        {
            t -= a[i%C]*2;
            ans += a[i%C]*2;
            if (t<=0)
            {
                x.push_back(-t/2);
                ans += t;
                t=0;
            }
        }
        sort(x.rbegin(),x.rend());
        for (int i=0;i<x.size();++i)
        {
            if (L>0)
            {
                ans += x[i];
                L--;
            }
            else
                ans += x[i]*2;
        }
        printf("Case #%d: %lld\n",q,ans);

    }

    return 0;
}
