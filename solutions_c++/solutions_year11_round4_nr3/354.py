#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
using namespace std;

typedef long long LL ;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000 + 1000;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
vector<int> primes;

bool isPrime(int n) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

void prepare() {
    for (int i = 2; i < 1000000; i++) {
        if (isPrime(i)) {
            primes.PB(i);
        }
    }
}

int solve() {
    LL n;
    cin >> n;
    if (n == 1) return 0;
    int ret = 1;
    for (int i = 0; i < (int) primes.size(); i++) {
        LL m = primes[i];
        LL k = m;
        while (k * m <= n) {
            ret++;
            k *= m;
        }
    }
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    prepare();
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        int ret = solve();
        cout << "Case #" << u << ": " << ret << "\n";
    }
}

