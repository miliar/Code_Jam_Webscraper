#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <inttypes.h>
#include <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <sstream>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")
#define _inline(f...) f() __attribute__((always_inline)); f
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); it++)
#define foreach(x...) _foreach(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

_inline(int cmp)(double x, double y = 0, double tol = EPS) {
return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

const int DIG = 4;
const int BASE = 10000; // BASE**3 < 2**51
const int TAM = 2048;

struct bigint {
    int v[TAM], n;
    bigint(int x = 0): n(1) {
        memset(v, 0, sizeof(v));
        v[n++] = x; fix();
    }

    bigint(char *s): n(1) {
        memset(v, 0, sizeof(v));
        int sign = 1;
        while (*s && !isdigit(*s)) if (*s++ == '-') sign *= -1;
        char *t = strdup(s), *p = t + strlen(t);
        while (p > t) {
            *p = 0; p = max(t, p - DIG);
            sscanf(p, "%d", &v[n]);
            v[n++] *= sign;
        }

        free(t); fix();
    }

bigint& fix(int m = 0) {
n = max(m, n);
int sign = 0;
for (int i = 1, e = 0; i <= n || e && (n = i); i++) {
v[i] += e; e = v[i] / BASE; v[i] %= BASE;
if (v[i]) sign = (v[i] > 0) ? 1 : -1;
}
for (int i = n - 1; i > 0; i--)
if (v[i] * sign < 0) { v[i] += sign * BASE; v[i+1] -= sign; }
while (n && !v[n]) n--;
return *this;
}
int cmp(const bigint& x = 0) const {
int i = max(n, x.n), t = 0;
while (1) if ((t = ::cmp(v[i], x.v[i])) || i-- == 0) return t;
}
bool operator <(const bigint& x) const { return cmp(x) < 0; }
bool operator ==(const bigint& x) const { return cmp(x) == 0; }
bool operator !=(const bigint& x) const { return cmp(x) != 0; }
operator string() const {
ostringstream s; s << v[n];
for (int i = n - 1; i > 0; i--) {
s.width(DIG); s.fill('0'); s << abs(v[i]);
}
return s.str();
}
friend ostream& operator <<(ostream& o, const bigint& x) {
return o << (string) x;
}
bigint& operator +=(const bigint& x) {
for (int i = 1; i <= x.n; i++) v[i] += x.v[i];
return fix(x.n);
}
bigint operator +(const bigint& x) { return bigint(*this) += x; }
bigint& operator -=(const bigint& x) {
for (int i = 1; i <= x.n; i++) v[i] -= x.v[i];
return fix(x.n);
}
bigint operator -(const bigint& x) { return bigint(*this) -= x; }
bigint operator -() { bigint r = 0; return r -= *this; }
void ams(const bigint& x, int m, int b) { // *this += (x * m) << b;
for (int i = 1, e = 0; (i <= x.n || e) && (n = i + b); i++) {
v[i+b] += x.v[i] * m + e; e = v[i+b] / BASE; v[i+b] %= BASE;
}
}
bigint operator *(const bigint& x) const {
bigint r;
for (int i = 1; i <= n; i++) r.ams(x, v[i], i-1);
return r;
}
bigint& operator *=(const bigint& x) { return *this = *this * x; }
// cmp(x / y) == cmp(x) * cmp(y); cmp(x % y) == cmp(x);
bigint div(const bigint& x) {
if (x == 0) return 0;
bigint q; q.n = max(n - x.n + 1, 0);
int d = x.v[x.n] * BASE + x.v[x.n-1];
for (int i = q.n; i > 0; i--) {
int j = x.n + i - 1;
q.v[i] = int((v[j] * double(BASE) + v[j-1]) / d);
ams(x, -q.v[i], i-1);
if (i == 1 || j == 1) break;
v[j-1] += BASE * v[j]; v[j] = 0;
}
fix(x.n); return q.fix();
}
bigint& operator /=(const bigint& x) { return *this = div(x); }
bigint& operator %=(const bigint& x) { div(x); return *this; }
bigint operator /(const bigint& x) { return bigint(*this).div(x); }
bigint operator %(const bigint& x) { return bigint(*this) %= x; }
bigint pow(int x) {
if (x < 0) return (*this == 1 || *this == -1) ? pow(-x) : 0;
bigint r = 1;
for (int i = 0; i < x; i++) r *= *this;
return r;
}
bigint root(int x) {
if (cmp() == 0 || cmp() < 0 && x % 2 == 0) return 0;
if (*this == 1 || x == 1) return *this;
if (cmp() < 0) return -(-*this).root(x);
bigint a = 1, d = *this;
while (d != 1) {
bigint b = a + (d /= 2);
if (cmp(b.pow(x)) >= 0) { d += 1; a = b; }
}
return a;
}
};

int ss( const void *a , const void *b ){
    int *i = (int *) a ;
    int *j = (int *) b ;

    return *j - *i ;
}

int main(){
    int N , in = 1 ;
    scanf("%d", &N ) ;
    while( N -- ){
        int p , k , l ;
        scanf("%d %d %d", &p ,&k ,&l ) ;

        int v[ l ] ;
        for( int i = 0 ; i < l ; i++ ) scanf("%d", &v[ i ] ) ;

        qsort( v , l , sizeof( int ) , ss ) ;

        int fator = 1 ;
        bigint sum = 0 ;

        for( int i = 0 ; i < l ; i++ ){
            bigint b( v[ i ] ) ;
            sum += ( b * fator ) ;
            if( (i + 1) % k == 0 ) fator ++;
        }

        printf("Case #%d: ", in++ ) ; cout << sum << endl ;

    }

    return 0 ;
}
