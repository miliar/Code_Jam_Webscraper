#include <cstdio>
#include <cmath>
using namespace std;

int N;
bool prime[1000001];
int main ()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    for (int i=0;i<=1000000;++i) prime[i]=1;
    int T;
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
    scanf("%d",&N);
    if (N==1) { printf("Case #%d: 0\n",z); continue; }
    for (int i=2;i*i<=N;++i) if (prime[i])
    {
        for (int j=2*i;j<=N;j+=i) prime[j]=0;
    }
    long long res=1;
    for (int i=2;i<=N;++i) if (prime[i])
    {
        int j=2;
        for (j=2;pow(1.0*i,j)<=N;++j);
        res+=j-2;
    }
    printf("Case #%d: %lld\n",z,res);
    }
    return 0;
}
