#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

#define MP make_pair
#define PB push_back
#define LB lower_bound
#define UB upper_bound

const double eps = 1e-8;
const double pi = acos(-1.0);

long long n, pd, pg;
long long gcd(long long a, long long b)
{
    return b == 0 ? a : gcd(b, a % b);
}
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T, tt = 0;
    for (cin >> T; T; T--) {
        cin >> n >> pd >> pg;
        printf("Case #%d: ", ++tt);
        if (pd == 0) {
            if (pg != 100)
                puts("Possible");
            else
                puts("Broken");
        } else if (pd == 100) {
            if (pg == 0)
                puts("Broken");
            else
                puts("Possible");
        } else {
            if (pg == 0 || pg == 100) {
                puts("Broken");
            } else {
                long long gc = gcd(100, pd);
                if (n >= 100 / gc)
                    puts("Possible");
                else
                    puts("Broken");
            }
        }
    }
}
