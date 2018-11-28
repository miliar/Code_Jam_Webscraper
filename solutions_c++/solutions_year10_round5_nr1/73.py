
//Tomasz Kulczyński
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }

ll odw(ll x, int p)
{
    int n = p - 2;
    ll ret = 1;
    while(n)
    {
        if(n%2)
        {   
            ret = ret * x % p;
        }
        x = x*x % p;
        n/=2;
    }
    return ret;
}

bool p[1001013];

void test()
{
    int d,k;
    int s[13];
    scanf("%d %d",&d,&k);
    REP(i,k) scanf("%d",&s[i]);
    if(k==1)
    {
        puts("I don't know.");
        return ;
    }
    if(s[0]==s[1])
    {
        printf("%d\n",s[0]);
        return ;
    }
    if(k==2)
    {
            puts("I don't know.");
            return;
    }
    int ret = -1, m = 1;
    REP(i,d) m *= 10;
    REP(n,m) p[n] = 0;
    FOR(n,2,m-1) if(!p[n])
    {
        for(int j = n+n; j<=m; j+=n) p[j] = 1;
    }
    FOR(i, (int)max(2, s[0]+1), m) if(!p[i])
    {
        ll a = odw(s[1]-s[0], i) * (s[2] - s[1]) % i;
        a = (a+i) % i;
        int b = (s[1] - a * s[0] % i + i) % i;
        b = (b+i) % i;
        int ok = 1;
        FOR(j,1,k-1) 
            if(s[j] != (a * s[j-1] + b) % i)
            {
                ok = 0;
                break;
            }
        if(ok)
        {
            if(ret == -1)
            {
                ret = (a * s[k-1] + b) % i;
            }
            else if(ret != (a * s[k-1] + b) % i)
            {
                ret = -2;
                break;
            }
        }
    }
    if(ret < 0)
    {
            puts("I don't know.");
            return ;
    }
    printf("%d\n",ret);
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d: ",cas);
        test();
    }
    return 0;
}
