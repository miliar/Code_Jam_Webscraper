#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cassert>
#include <math.h>
#include <string.h>
using namespace std;
#define LL long long
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define REP(i,n) for( int i=0;i<int(n);++i)
LL gcd(LL a, LL b)
{
    return b == 0 ? a : gcd(b, a % b);
}
namespace my_namespace {
};
using namespace my_namespace;
int a[102][102];
int prime_factors(LL v, int *pp)
{
    int cnt = 0;
    for (LL a = 2; a * a <= v; a++) {
        if (v % a == 0) {
            *pp = 0;
            while (v % a == 0) {
                (*pp)++;
                v /= a;
            }
            cnt++;
        }
    }
    if (v != 1) {
        *pp = 1;
        cnt++;
    }
    return cnt;
}
int combine(int a, int b)
{
    if (a == 0)
        return b;
    if (b == 0)
        return a;
    return a * b / gcd(a, b);
}
void problem()
{
    int n = SCAN_INT();
    if (n == 1) {
        printf("%d\n", 0);
        return;
    }
    int minc = 0;
    int maxc = 1;
    for (int p = 2; p <= n; p++) {
        bool bad = false;
        for (int j = 2; j < p; j++)
            if (p % j == 0)
                bad = true;
        if (bad)
            continue;
        int cnt = -1;
        int acc = 1;
        while (acc <= n) {
            acc *= p;
            cnt++;
        }
        minc++;
        maxc += cnt;
    }
    printf("%d\n", maxc - minc);
}
int main()
{
    int n = SCAN_INT();
    assert(0 == scanf(" "));
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
