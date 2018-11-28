#include <algorithm>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <map>
#include <numeric>
#include <set>
#include <vector>
#include <utility>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


const int N = 5000001;
int primes[N], np, ex[N], maxex[N], imaxex[N];
bool flag[N];

void getPrimes()
{
    static bool sifted[N];
    for (int i = 2; i < N; i++)
        if (!sifted[i]) {
            primes[np++] = i;
            for (int j = i*2; j < N; j += i)
                sifted[j] = true;
        }
}

int decompose(ll n)
{
    for (int i = 0; i < np; i++) {
        if (n==1||n/primes[i]<primes[i]) return i;
        ll nn = n;
        ex[i] = 0;
        while (nn >= primes[i]) {
            nn /= primes[i];
            ex[i]++;
        }
    }
}

int main()
{
    int cases;
    getPrimes();
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        ll n;
        memset(maxex, 0, sizeof(maxex));
        memset(flag, 0, sizeof(flag));

scanf("%lld", &n);
if(n==1){
printf("Case #%d: 0\n", T);
continue;
}
ll res=decompose(n);
ll res2 = 0;
for (int i = 0; i < res; i++)
    res2+=ex[i]-1;

		printf("Case #%d: %lld\n", T, res2+1);
    }
}
