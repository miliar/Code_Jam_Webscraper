#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = (1 << 31) - 1;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;


const ll BORDER = 1000 * 1000;

vector<ll> primes;
void gen(){
    primes.clear();
    vector<bool> is_prime(BORDER, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i < is_prime.size(); ++i) {
        if (!is_prime[i]) {
            continue;
        }
        primes.push_back(i);
        for (int j = 2; j * i < is_prime.size(); ++j) {
            is_prime[i * j] = false;
        }
    }
}

vector<pll> almostFactorInteger(ll n) {
    vector<pll> res;
    for (ll i = 0; i < primes.size(); ++i) {
        int power = 0;
        ll p = primes[i];
        ll prime_power = 1;
        while (prime_power * p <= n) {
            ++power;
            prime_power *= p;
        }
        if (power > 0) {
            res.push_back(pll(p, power));
        }
    }
    return res;
}

void solveProblem() {
    ll n;
    cin >> n;
    if (n == 1) {
        cout << 0 << endl;
        return;
    }
    ll res = 0;
    vector<pll> fact = almostFactorInteger(n);
    for (int i = 0; i < fact.size(); ++i) {
        res += fact[i].second - 1;
    }
    cout << res + 1 << endl;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    gen();
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        double t = clock();
        printf("Case #%d: ", test);
        solveProblem();
        t = (clock() - t) / CLOCKS_PER_SEC;
        cerr << test << " time " << t << " s\n";
    }
	return 0;
}
