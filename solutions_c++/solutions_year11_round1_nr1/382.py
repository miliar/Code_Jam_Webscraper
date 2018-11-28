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

#define TRACE(x...) x
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

typedef map<long long, int> prime_map;

void squeeze(prime_map& M, long long &n, int p)
{
    for(;n % p == 0; n /= p) M[p]++;
}

prime_map factor(long long n)
{
    prime_map M;
    if (n < 0) return factor(-n);
    if (n < 2) return M;
    squeeze(M, n, 2); squeeze(M, n, 3);
    int maxP = sqrt(n) + 2;
    for(int p = 5; p < maxP; p += 6)
    {
        squeeze(M, n, p);
        squeeze(M, n, p+2);
    }
    if (n > 1) M[n]++;
    return M;
}

bool can(long long n, int pd, int pg)
{
    if (pg == 100 and pd != 100) return false;
    if (pg == 0) return (pd == 0);
    prime_map p = factor(pd);
    int twos = max(0, 2-p[2]);
    int fives = max(0, 2-p[5]);
    int res = 1;
    while (twos--) res *= 2;
    while(fives--) res *= 5;
    return res <= n;
}

int main()
{
    int t;
    read(t);

    int pd, pg;
    long long n;

    forz(t)
    {

        scanf("%ld %d %d", &n, &pd, &pg);
        printf("Case #%d: %s\n", i+1, can(n, pd, pg)?"Possible":"Broken");
    }
    return 0;
}
