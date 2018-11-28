#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

const int maxp = 500000;

typedef unsigned long ul_t;
typedef vector<char> vc;
typedef vector<long> vi;

vc sieve(maxp, 1);
vi primes;
void init_sieve() {
    for (int i=0; i < 2 + sqrt(2*maxp); ++i) {
        if (!sieve[i]) continue;
        for (int p = 3*(i+1); p<maxp; p += 3 + 2*i) sieve[p] = 0;
    }

    primes.push_back(2);
    for (int i=0; i<maxp; ++i) {
        if (sieve[i]) primes.push_back(3+2*i);
    }
}

struct prob {
    int A, B, P, maxp;
    vi v;
    prob(int a, int b, int p) : A(a), B(b), P(p), maxp(B-A), v(B-A+1)
    {
        for (int i=0; i<int(v.size()); ++i) v[i] = i;
    }

    int solve() {
        for (int i=0; i<maxp; ++i) {
            int p = primes[i];
            if (p < P) continue;
            if (p > maxp) break;
            int J = (p - (A%p))%p;
            int j = J;
            assert(J < int(v.size()));
            while (v[j] != j) j = v[j];
            // cout << "p=" << p << " J=" << J << " j=" << j << endl;
            for (int K=J+p; K<int(v.size()); K += p) {
                int k = K;
                while (v[k] != k) k = v[k];
                v[k] = j;
            }
        }
        int res = 0;
        for (int i=0; i<int(v.size()); ++i) {
            if (v[i] == i) ++res;
        }
        return res;
    }
};

int main() {
    init_sieve();
    int C;
    cin >> C;
    for (int i=1; i<=C; ++i) {
        int A, B, P;
        cin >> A >> B >> P;
        prob p(A, B, P);
        int res = p.solve();
        cout  << "Case #" << i << ": " << res << endl;
    }
}
