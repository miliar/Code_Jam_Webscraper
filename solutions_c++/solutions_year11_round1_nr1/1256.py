#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

long long n,pd,pg,mind,wind,losd,ming,wing,losg,g;

long long gcd(long long a,long long b)
{
    if (b == 0) return a;
    return gcd(b,a%b);
}

int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ft = 1;ft <= t;ft++)
    {
        scanf("%lld%lld%lld",&n,&pd,&pg);
        printf("Case #%d: ",ft);
        mind = 100/gcd(pd,100);
        wind = pd*mind/100;
        losd = mind-wind;
        ming = 100/gcd(100,pg);
        wing = pg*ming/100;
        losg = ming-wing;
        if (mind > n || mind > ming || (pg == 0 && pd != 0) || (pg == 100 && pd != 100))
        {
            printf("Broken\n");
            continue;
        }
        //cout << wind << ' ' << losd << ' ' << wing << ' ' << losg << endl;
        //if (wing >= wind && losg >= losd)
            printf("Possible\n");
        //else
            //printf("Broken\n");
    }
}
