#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
vector<bool> isp;
vector<int> primes;
void tst()
{
    long long n;
    scanf("%lld",&n);
    if(n==1)
    {
        puts("0");
        return;
    }
    int ans=1;
    for(int i=0;i<primes.size() && primes[i]<=n;i++)
    {
        int p = primes[i];
        long long nn = n;
        while(nn>=p)
        {
            nn/=p;
            ans++;
        }
        ans--;
    }
    printf("%d\n",ans);
        
}
int main()
{
    int t;
    scanf("%d",&t);
    isp.resize(2000000,true);
    for(int i=2;i<2000000;i++)
        if(isp[i])
        {
            primes.push_back(i);
            for(int j=2*i;j<2000000;j+=i)
                isp[j]=false;
        }
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        tst();
    }

}
