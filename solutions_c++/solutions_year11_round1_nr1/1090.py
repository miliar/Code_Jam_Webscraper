// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)

int t;
LL n;
LL pd, pg;
LL wd, d, x, y, wg, g;
string s;
bool success;

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    if (a < b)
        return gcd(b, a);
    return gcd(b, a % b);
}


int main()
{
//     freopen("A-small-attempt2.in", "r", stdin);
//     freopen("A-small-attempt2.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    for (int cc = 1; cc <= t; cc++)
    {
        scanf("%lld %lld %lld", &n, &pd, &pg);
        
        success = false;

        if (pg == 0 && pd > 0)
            goto OUT_PUT;

        if (pg == 100 && pd < 100)
            goto OUT_PUT;

        int gcd_ = gcd(100, pd);
        int gcd2 = gcd(100, pg);
        d = 100 / gcd_;
        wd = pd / gcd_;
        g = 100 / gcd2;
        wg = pg / gcd2;

        
        int d2, wd2;
        int g2, wg2;
        for (int i = 1; ; i++)
        {
            d2 = d * i;
            wd2 = wd * i;
            if (d2 > n)
            {
                success = false;
                break;
            }

            success = true;
            goto OUT_PUT;
//             for (int j = 1; ; j++)
//             {
//                 g2 = g * j;
//                 wg2 = wg * j;
//                 y = g2 - d2;
//                 x = wg2 - wd2;
// 
//                 if (x >= 0 && y >= 0 && y >= x)
//                 {
//                     success = true;
//                     goto OUT_PUT;
//                 }
// 
//                 if (g2 > d2 && wg2 > wd2)
//                 {
//                     break;
//                 }
//             }

        }

OUT_PUT:
        if (success)
            printf("Case #%d: Possible\n", cc);
        else
            printf("Case #%d: Broken\n", cc);
    }
    
	return 0;
}

