#include<cstdio>

using namespace std;

int main()
{
    int t;
    long long r;
    long long n,k;
    int z=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld%lld",&n,&k);
        r=(1<<n)-1;
        if(k%(1<<n)==r)
        {
            printf("Case #%d: ON\n",++z); 
        }
        else
        {
            printf("Case #%d: OFF\n",++z);
        }
    }
    return 0;
}
