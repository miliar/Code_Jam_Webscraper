
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

const int Q = 1000000007;
const int B = 73;

map<ll, int> mem[B];
ll t[B][B*B], wybor[B][B];

int b;

int go(int ile, ll suma)
{
    if(!ile)
    {
        if(!suma) return 1;
        return 0;
    }
    if(!suma) return 0;
    if(mem[ile].count(suma))
        return mem[ile][suma];
    int s = suma % b;
    ll ret = 0;
    REP(o,b)
    {
        if(suma == s)
        {
            ret += t[ile][s];
        }
        else
            REP(i,ile+1) 
            {
                ret += t[ile][s] * go(i, (suma - s) / b) % Q * wybor[ile][i] % Q;
                if(i) 
                    ret += t[ile-1][s] * go(i, (suma - s) / b) % Q * (wybor[ile][i] - wybor[ile-1][i]) % Q;
                ret += Q;
                ret %= Q;
            }
        s += b;
        if(s > suma) break;
    }
    return mem[ile][suma] = ret;
}

ll T[B][B*B][B];

void test()
{
    ll n;
    scanf("%lld %d",&n,&b);
    REP(i,B) REP(j,B*B) REP(k,B) T[i][j][k] = 0;
    REP(x,b+1) T[0][0][x] = 1;
    FOR(i,1,b) REP(s,B*B) REP(u,b+1) 
    {
        FOR(x,1,u-1) if(x<=s)
            T[i][s][u] += T[i-1][s-x][x];
        T[i][s][u] %= Q;
    }
    REP(i,B) REP(j,B*B) t[i][j] = T[i][j][b];
//    printf("t == %lld\n",t[2][6]);
//    REP(i,3) REP(j,7) REP(k,11) printf("%d %d %d :: %lld\n",i,j,k,T[i][j][k]);
    REP(i,b+1) mem[i].clear();
    int ret = 0;
    FOR(i,1,b) 
    {
//        printf("%d\n",go(i,n));
        ret = (ret + go(i, n)) % Q;
    }
    printf("%d\n",ret);
}

ll odw(ll x, int p)
{
    int n = p-2;
    ll ret = 1;
    while(n)
    {
        if(n%2)
        {
            ret = ret*x%Q;
        }
        n/=2;
        x=x*x%Q;
    }
    return ret;
}

int main()
{
    wybor[0][0] = 1;
    FOR(x,1,B-1) wybor[x][x] = ( wybor[x-1][x-1] * x ) % Q;
    REP(x,B) FOR(y,x+1,B-1) 
        wybor[y][x] = wybor[y-1][x] * y * odw(y-x, Q) % Q;
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d: ",cas);
        test();
    }
    return 0;
}
