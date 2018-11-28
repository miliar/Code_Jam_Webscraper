#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << '\n')

#define forz(p)     for(int i = 0; i < p; ++i)
#define foriz(i, p) for(int i = 0; i < p; ++i)
#define tr(x)       for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define read(n)     (scanf("%d", &(n)) == 1)

const int INF = 0x3f3f3f3f;
const double EPS = 1e-9;

inline int cmpD(double x, double y, double tol = EPS)
{
    return (x <= y + tol) ? (x + tol < y) ?  -1 : 0 : 1;
}

#define LIM 1000000

char ppp[(LIM+1)];
int pp[LIM];
int pc;

inline void MARK(int p)
{
    for(int P = p*p; P < (LIM+1); P += p+p) ppp[P] = 0;
}

void build_sieve()
{
    forz((LIM+1)) ppp[i] = (i % 2) and (i % 3);
    ppp[0] = ppp[1] = 0;
    ppp[2] = ppp[3] = 1;
    pp[0] = 2;
    pp[1] = 3;
    pc = 2;
    int threshold = (int)sqrt(LIM)+2;
    if (!(threshold % 2)) threshold++;
    for(int i = 6; i < threshold; i += 6)
    {
        if (ppp[i-1])
        {
            pp[pc++] = i-1;
            MARK(i-1);
        }
        if (ppp[i+1])
        {
            pp[pc++] = i+1;
            MARK(i+1);
        }
    }
    for(int i = threshold; i < (LIM+1); i += 2)
    {
        if (ppp[i]) pp[pc++] = i;
    }
}

int gcd(int a, int b) { return (b==0? a : gcd(b, a %b)); }
long long lcm(long long a, long long b) { return a*(b/gcd(a,b)); }

long long go()
{
    long long N;
    scanf("%lld", &N);

    if (N == 1) return 0;

    int psum = 0;
    int pcount = 0;

    for(int i = 0; pp[i] <= N; ++i)
    {
        PRINT("New prime: %d!\n", pp[i]);
        pcount++;
        long long pl = pp[i];
        while(pl <= N)
        {
            psum++;
            pl *= pp[i];
        }
    }

    WATCH(psum);
    WATCH(pcount);

    return psum - pcount + 1;

    /*int sum = 1;
    int wstr = 1;
    int nlcm = 1;
    for(int i = 2; i <= N; ++i)
    {
       int alcm = lcm(i, nlcm); 
       if (alcm != nlcm)
       {
           wstr++;
           nlcm = alcm;
       }
    }

    int wrev = 1;
    sum = N;
    nlcm = N;
    for(int i = N-1; i > 0; --i)
    {
        int alcm = lcm(i, nlcm);
        if (alcm != nlcm)
        {
            wrev++;
            nlcm = alcm;
        }
    }
    WATCH(N);
    WATCH(wstr);
    WATCH(wrev);
    PRINT("\n");
    return max(wrev, wstr) - min(wrev, wstr);*/
}

int main()
{
    build_sieve();
    int T;
    read(T);
    forz(T)
    {
        printf("Case #%d: %lld\n", i+1, go());
    }
    return 0;
}
