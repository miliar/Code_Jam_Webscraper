#include <cstdio>
using namespace std;
long long tst()
{
    int R,k,N;
    scanf("%d%d%d",&R,&k,&N);
    int inp[N];
    long long sum=0;
    for(int i=0;i<N;i++)
    {
        scanf("%d",&inp[i]);
        sum += inp[i];
    }
    if(sum<=k)
    {
        return R*sum;
    }
    int jumpto[N];
    int jumpile[N];
    int ilemam=0;
    for(int i=0,j=0;i<N;)
    {
        if(ilemam>k)
        {
            jumpto[i] = (j-1)%N;
            jumpile[i] = ilemam-inp[(j-1)%N];
            ilemam -= inp[i];
            i++;
        }
        else
        {
            ilemam += inp[j%N];
            j++;
        }
    }

    long long ans = 0;

    int t=0;
    for(int i=0;i<R;i++)
    {
        ans += jumpile[t];
        t = jumpto[t];
    }
    return ans;
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
        printf("Case #%d: %lld\n",i,tst());

}
