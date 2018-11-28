#include <cstdio>
#include <vector>

using namespace std;

const long long inf = 2000000000000000000ll;
void tst()
{
    int n;
    long long l;
    scanf("%lld%d",&l,&n);

    vector<int> inp(n);
    for(int i=0;i<n;i++)
        scanf("%d",&inp[i]);
    vector<long long> cost(100000,inf);
    cost[0]=0;
    for(int i=0;i<cost.size();i++)
        for(int j=0;j<n;j++)
            if(i+inp[j]<cost.size())
                cost[i+inp[j]] = min(cost[i+inp[j]],cost[i]+1);
    long long best = inf;

    for(int j=0;j<n;j++)
    {
        int s = l%inp[j];
        for(int k=s;k<cost.size();k+=inp[j])
            if(cost[k]<inf)
                best = min(best, cost[k]+(l-k)/inp[j]);
    }

    if(best==inf)
        puts("IMPOSSIBLE");
    else
        printf("%lld\n",best);


}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        tst();
    }
}
