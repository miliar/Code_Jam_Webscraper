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
#include <stdio.h>
using namespace std;
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define SZ size()
#define REP(i,n) for( int i=0;i<int(n);++i)
#define ALWAYS(f,p) (*({bool _fa=true;f if(!(p)) {_fa=false;break;}&_fa;}))
#define EXISTS(f,p) !(ALWAYS(f,!(p)))
#define VI vector<int>
#define FOR(i,p,k) for( int i=p; i<int(k); ++i)
namespace my_namespace {
};
using namespace my_namespace;
int count_digits(int v)
{
    int res = 0;
    while (v) {
        res++;
        v /= 10;
    }
    return res;
}
void problem()
{
    int a = SCAN_INT();
    int b = SCAN_INT();
    int total = 0;
    int last_pct = 0;
    FOR(u, a, b + 1) {
        int digits = count_digits(u);
        int dig_pow = 1;
        REP(i, digits - 1)
         dig_pow *= 10;
        VI shifts;
        int v = u;
        REP(i, digits - 1) {
            int last = v % 10;
            v = v / 10 + last * dig_pow;
            if (v >= u || v < a || last == 0)
                continue;
            if (EXISTS(REP(j, shifts.SZ), shifts[j] == v))
                continue;
            shifts.push_back(v);
        }
        total += shifts.SZ;
    }
    printf("%d\n", total);
}
int main()
{
    int n = SCAN_INT();
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
