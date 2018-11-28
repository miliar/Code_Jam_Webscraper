#include <stdlib.h>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <algorithm>
#include <cmath>
using namespace std;


int main()
{
//    freopen("a.in", "r", stdin);
//    freopen("a.out", "w", stdout);
    long long base[64];
    base[0] = 1;
    for (int i = 1; i <= 32; ++i) base[i] = base[i-1] << 1;
    int test_case;
    scanf( "%d", &test_case);
    for (int i = 1; i <= test_case; ++i)
    {
        int n, k;
        scanf( "%d %d", &n, &k);
        long long num = base[n];
        ++ k;
        if (k % num == 0)
            printf( "Case #%d: ON\n", i);
        else printf( "Case #%d: OFF\n", i);
    }
    return 0;
}