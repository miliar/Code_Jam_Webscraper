#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long s64;
typedef unsigned long long u64;

int p[100000];
int n;

bool isPrime(int x) {
    for (int i = 0; i < n; i++) {
        int pp = p[i];
        if (pp * pp > x) return true;
        if (x % pp == 0) return false;
    }
    return true;
}

void primes() {
    n = 0; p[n++] = 2;
    for (int i = 3; i < 1000000; i += 2) {
        if (isPrime(i)) p[n++] = i;
    }
}

s64 largest(s64 x, s64 P) {
    s64 best = 0;
    for (int i = 0; x > 1 && i < n; i++) {
        int pp = p[i];
        if (pp * pp > x) return x;
        if (x % pp == 0) {
            best = pp;
            if (best >= P) return P;
            while (x % pp == 0) x /= pp;
        }
    }
    if (x > 1) best >?= x;
    return best;
}

s64 s[1024];

int main() {
    primes();
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        s64 A, B, P; cin >> A >> B >> P;
        for (s64 a = A; a <= B; a++) {
            s[a] = a;
        }
        for (s64 a = A; a <= B; a++) {
            for (s64 b = a+1; b <= B; b++) {
                s64 g = __gcd(a, b);
                if (largest(g, P) >= P) {
                    s64 ga = s[a];
                    s64 gb = s[b];
                    for (s64 c = A; c <= B; c++) {
                        if (s[c] == gb) s[c] = ga;
                    }
                }
            }
        }
        sort(&s[A], &s[B+1]);
        int sets = 1;
        for (s64 a = A+1; a <= B; a++) {
            if (s[a] != s[a-1]) sets++;
        }
        cout << "Case #" << t << ": " << sets << endl;
    }
    return 0;
}

