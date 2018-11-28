#include <iostream>
#include <cstdio>
#include <bitset>
#include <cstring>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

long long a[32];

int inverse(int a, int n) {
    int x = 1, y = 0, b = n, k;
    for (;b; swap(x, y), swap(a, b)) {
        k = a / b;
        a -= b * k;
        x -= y * k;
    }
    return x < 0 ? x + n : x;
}

template <int T> //  T > n!!!
void primes (int n, bitset <T> & a) {
    a.set (0); a.set (1);     
    for (int i = 2; i*i <= n; ++i) if (!a.test (i)) 
        for(int j = i*i; j <= n; j += i)
            a.set (j);
}

bitset <1200001> p;

int main() {
    #ifdef LOCAL
//	freopen("A-small-attempt1.in" , "r", stdin);
//    freopen("A-small-attempt1.out" , "w", stdout);
	freopen("A-large (1).in", "r", stdin);
    freopen("A-large (1).out"  , "w", stdout);
    #endif
    int test;
    scanf ("%d", &test);
    primes <1200001> (1000000, p);
    FOR (test_num, 1, test + 1) {
        printf ("Case #%d: ", test_num);
        int d, k;
        cin >> d >> k;
        REP (i, k) cin >> a[i];
        if (k == 1) {
            cout << "I don't know.";
            cout << endl;
            continue;
        }
        if (a[0] == a[1]) {
            cout << a[0] << endl;
            continue;
        }
        if (k == 2) {
            cout << "I don't know.";
            cout << endl;
            continue;
        }
        int dd = 1;
        REP (i, d)
            dd *= 10;
        int next = -1;
        bool amb = false;
        FOR (P, 2, dd)
            if (!p[P]) {
                long long A = (((ll) inverse (((a[0]-a[1]) % P + P) % P, P) * (a[1] - a[2])) % P + P) % P;               
                long long B = ((a[1] - a[0] * A) % P + P) % P;
                long long S = a[0] % P;
                bool ok = true;
                REP (i, k) {
                    if (S != a[i]) {
                        ok = false;
                        break;
                    }
                    S = (A * S + B) % P;
                }
                if (ok) {
                    if (next != -1 && S != next) {
                        amb = true;
                        goto out;
                    }
                    next = S;
                }
            }
out:;
        if (next == -1 || amb) {
            cout << "I don't know.";
            cout << endl;
            continue;                            
        }
        cout << next << endl;
    }
	return 0;
}
