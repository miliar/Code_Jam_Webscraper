#include <map>
#include <list>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int compo[ 1001 ];
bool prime[ 1001 ];
vector<int> primes;

int gcd(int m, int n)
{
    if(n==0) return m;
    if(m==0) return n;
    return gcd(n,m%n);
}

bool ok(int x)
{
    for(int i= 2; i*i <= x; i++)
     if( x%i == 0 ) return false;

    return true;
}

int large(int p)
{

    int ret  =0 ;

    for(int i = 0;i < primes.size(); i++)
    {
        if(p % primes[i] == 0 )ret >?= primes[i];
    }

    return ret;
}

void gen()
{
    for(int i = 2; i <= 1000; i++)
     if(ok(i))
     {
      prime[i]=  1;
      primes.push_back(i);
     }
     return ;
}

int main()
{
    freopen("bin.txt","r", stdin);
    freopen("bout.txt","w", stdout);

    memset(prime,0,sizeof prime);
    gen();

    /*while(true)
    {
        int x,y;
        scanf("%d %d", &x, &y);
        printf("%d\n", gcd(x,y));
    }*/

    int c;

    scanf("%d", &c);

    for(int i = 1;i <= c; i++)
    {
        memset(compo, 0,sizeof compo);
        int a,b,p,cnt=0;
        scanf("%d %d %d", &a, &b, &p);

        for(int j = a; j <= b ; j++)
        {

         int wh=-1;
         if(compo[j]) wh = compo[j];
         for(int k = j + 1 ; k <= b && (wh==-1) ; k ++)
         {
            int x = gcd(j,k);x = large(x);
            if( x >= p && compo[k])
            {
                wh = compo[ k ];
                break;
            }
         }
         if(wh==-1){ ++cnt; wh = cnt;}
         compo[ j ] = wh;
         for(int k = j + 1 ; k <= b ; k ++)
         {
            int x = gcd(j,k);
            x = large(x);
            if( x >= p )
             compo[ k ] = wh;
         }
        }
/*
        for(int j = a; j <= b; j++)
         printf("%d %d\n",j, compo[j]);*/

        printf("Case #%d: %d\n", i,cnt);
    }

    return 0;
}
