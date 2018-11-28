#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <functional>

using namespace std;

typedef long long ll;


ll gcd(ll a, ll b) {
    if (a < b) return gcd(b, a);
    if (b == 0) return a;
    return gcd(b, a%b);
}

struct Rational {
    ll n, d;
    Rational(ll N = 0, ll D = 1) : n(N), d(D) { normalize(); }
    void normalize() {
        ll g = gcd(abs(n), abs(d));
        if (d < 0) g = -g;
        if (g == 0) g = 1;
        n /= g;
        d /= g;
    }
    bool valid() const {
        return d != 0;
    }
    bool i() const {
        return d == 1;
    }
    double tod() const { return double(n)/d; }
};
ll ceil(const Rational& a) {
    return (a.n < 0) ? (a.n / a.d) : ((a.n + a.d - 1) / a.d);
}
ll floor(const Rational& a) {
    return (a.n < 0) ? ((a.n - a.d + 1) / a.d) : (a.n / a.d);
}
Rational& operator+=(Rational& a, const Rational& b) { 
    a.n = a.n * b.d + b.n * a.d;
    a.d *= b.d;
    a.normalize();
    return a;
}
Rational& operator-=(Rational& a, const Rational& b) { 
    a.n = a.n * b.d - b.n * a.d;
    a.d *= b.d;
    a.normalize();
    return a;
}
Rational& operator*=(Rational& a, const Rational& b) { 
    a.n *= b.n;
    a.d *= b.d;
    a.normalize();
    return a;
}
Rational& operator/=(Rational& a, const Rational& b) { 
    a.n *= b.d;
    a.d *= b.n;
    a.normalize();
    return a;
}
Rational operator+(const Rational& a, const Rational& b) { 
    Rational r(a);
    r += b;
    return r;
}
Rational operator-(const Rational& a, const Rational& b) { 
    Rational r(a);
    r -= b;
    return r;
}
Rational operator*(const Rational& a, const Rational& b) { 
    Rational r(a);
    r *= b;
    return r;
}
Rational operator/(const Rational& a, const Rational& b) { 
    Rational r(a);
    r /= b;
    return r;
}
Rational operator-(const Rational& a) { 
    Rational r(a);
    r.n = -r.n;
    return r;
}
bool operator==(const Rational& a, const Rational& b) {
    return a.n == b.n && a.d == b.d;
}
bool operator<(const Rational& a, const Rational& b) {
    return a.n * b.d < b.n * a.d;
}
bool operator>(const Rational& a, const Rational& b) {
    return a.n * b.d > b.n * a.d;
}
bool operator<=(const Rational& a, const Rational& b) {
    return a.n * b.d <= b.n * a.d;
}
bool operator>=(const Rational& a, const Rational& b) {
    return a.n * b.d >= b.n * a.d;
}
ostream& operator<<(ostream& s, const Rational& a) {
    return s << a.n << '/' << a.d;
}

int N;
vector<int> which;
vector<int> h;
//vector<Rational> ma;

void doStuff(int i, int slope) {
    int j = which[i];
    vector<int> path;
    // Fill in h(i, j), given h[i] and h[j]
    for (int k = i+1; k < j; ) {
        path.push_back(k);
        k = which[k];
        if (k > j) throw "NOPE";
    }
    for (int z = path.size(); z--; ) {
        ++slope;
        int pz = path[z];
        int wz = which[pz];
        h[pz] = h[wz] - slope * (wz - pz);
        doStuff(pz, slope);
    }
}

int main() {
    int T;
    cin >> T;
    for (int z = 1; z <= T; ++z) {
        cout << "Case #" << z << ":";
        cin >> N;
        which.resize(N-1);
        for (int i = 0; i < N-1; ++i) { cin >> which[i]; --which[i]; }
        h = vector<int>(N, 0);
        try {
            int slope = 0;
            vector<int> path;
            // Fill in h(0, N-1)
            for (int k = 0; k < N; ) {
                path.push_back(k);
                if (which[k] <= k) throw "NOPE";
                k = which[k];
                if (k == N-1) break;
            }
            for (int z = path.size(); z--; ) {
                ++slope;
                int pz = path[z];
                int wz = which[pz];
                h[pz] = h[wz] - slope * (wz - pz);
                doStuff(pz, slope);
            }
            int M = 0;
            for (int i = 0; i < N; ++i) {
                if (h[i] < M) M = h[i];
            }
            for (int i = 0; i < N; ++i) {
                cout << ' ' << h[i] - M;
            }
            cout << endl;
        } catch (const char*) {
            cout << " Impossible" << endl;
        }
    }
}