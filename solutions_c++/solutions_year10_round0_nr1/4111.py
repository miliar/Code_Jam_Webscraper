#include <iostream>
using namespace std;

#define MaxN 30
#define ll long long

ll pow[MaxN+5];
ll n,k,t;

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen( "test.out", "w", stdout );
    pow[0] = 1;
    for (int i = 1; i <= MaxN; i++)
        pow[i] = 2*pow[i-1];
        
    scanf("%lld",&t);
    for (int T = 0; T < t; T++) {
        scanf("%lld %lld",&n,&k);
        
        if ( k % pow[n] == pow[n]-1 ) printf("Case #%d: ON\n",T+1);
        else                               printf("Case #%d: OFF\n",T+1);
    }
    
    return 0;
    
}
