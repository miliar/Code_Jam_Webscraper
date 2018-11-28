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
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

const int maxn = 1 << 20;

bool isprime[maxn];

int main()
{
    memset(isprime, true, sizeof(isprime));
    for (int i = 2; i * i <= maxn; i++)
        if (isprime[i]) {
            for (int j = i * i; j <= maxn; j += i)
                isprime[j] = false;
        }
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        long long n;
        scanf("%lld", &n);
        long long ans = 0;
        for (int i = 2; (long long)i * i <= n && i < maxn; i++)
            if (isprime[i]) {
                long long a = i;
                while ((a *= i) <= n) {
                    ans ++;
                }
            }
        if (n > 1)
            ans ++;
        printf("Case #%d: %lld\n", ++cas, ans);
    }
}
