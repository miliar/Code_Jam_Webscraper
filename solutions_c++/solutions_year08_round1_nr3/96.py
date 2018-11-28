// comment

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <vector>

using namespace std;


// --------------------- <tlong> ------------------- //
typedef long long i64;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)

const int maxlen = 1000;
const int base = 1000;

class tlong {
    int a[maxlen];
    int s;
    
    void add(tlong &b);
    void sub(tlong &b);
    void mul(tlong &b);
    void div(tlong &b);

    void mul(int b);
    void div(int b);
    int mod(int b);

public:
    int sign;
    int diff(tlong b);

    void operator += (tlong b);
    void operator -= (tlong b);
    void operator *= (tlong b);
    void operator /= (tlong b);
    void operator %= (tlong b);
    
    void operator += (int b);
    void operator -= (int b);
    void operator *= (int b);
    void operator /= (int b);
    void operator %= (int b);
    void half();

    string tostring();
    int toInt();

    int operator [] (int x);
    tlong operator = (tlong b);
    tlong operator = (i64 b);

    int size();
    tlong();
    tlong(i64 x);
};

tlong operator + (tlong a, tlong b) { a += b; return a; }
tlong operator * (tlong a, tlong b) { a *= b; return a; }
tlong operator - (tlong a, tlong b) { a -= b; return a; }
tlong operator / (tlong a, tlong b) { a /= b; return a; }
tlong operator * (tlong a, int b) { a *= b; return a; }
tlong operator / (tlong a, int b) { a /= b; return a; }
tlong operator % (tlong a, tlong b) { a %= b; return a; }
int operator % (tlong a, int b) { a %= b; return a.toInt(); }

bool operator == (tlong a, tlong b) { return (a.diff(b) == 0); }
bool operator != (tlong a, tlong b) { return (a.diff(b) != 0); }
bool operator <= (tlong a, tlong b) { return (a.diff(b) <= 0); }
bool operator >= (tlong a, tlong b) { return (a.diff(b) >= 0); }
bool operator < (tlong a, tlong b) { return (a.diff(b) < 0); }
bool operator > (tlong a, tlong b) { return (a.diff(b) > 0); }

int gcd(int a, int b);
tlong gcd(tlong a, tlong b);
void swap(tlong &a, tlong &b);


int tlong::diff(tlong b) {
    if (s != b.s) return s - b.s;
    for (int i = s - 1; i >= 0; --i) {
        if (a[i] != b[i]) return a[i] - b[i];
    }
    return 0;    
}

void tlong::add(tlong &b) {
    while (s < b.s) { a[s++] = 0; }
    a[s] = 0;
    forn(i, s) {
        if (i < b.s) a[i] += b[i];
        if (a[i] >= base) {
            ++a[i + 1];
            a[i] -= base;
        }
    }
    if (a[s] != 0) ++s;
}

void tlong::sub(tlong &b) {
    assert(s >= b.s);
    forn(i, s) {
        if (i < b.s) a[i] -= b[i];
        if (a[i] < 0) {
            a[i] += base;
            --a[i + 1];
        }
    }
    while (s > 0) {
        if (a[s - 1] == 0) --s; else break;
    }
}

void tlong::mul(tlong &b) {
    i64 x = 0, y;
    int c[maxlen];
    memset(c, 0, sizeof(c));
    int ss = 0, t;
    forn(i, s) {
        forn(j, b.s) {
            x = (i64)a[i]*b[j];
            for (t = i + j; x > 0; ++t) {
                x += c[t];
                y = x / base;
                c[t] = (int)(x - y*base);
                x = y;
            }
            if (t > ss) ss = t;
        }
    }
    s = ss;
    forn(i, s) {
        a[i] = c[i];
    }
}

void tlong::div(tlong &b) {
    tlong left;
    tlong right = *this;
    right.sign = 1;
    tlong t;
    while (left + 1 < right) {
        t = (left + right) / 2;
        if (s > t.s + b.s) left = t; else
            if (s < t.s + b.s - 1) right = t; else
                if (diff(t*b) >= 0) left = t; else right = t;
    }
    left.sign = sign;
    *this = left;
}

void tlong::mul(int b) {
    i64 t = 0, y;
    forn(i, s) {
        t += (i64)b*a[i];
        y = t / base;
        a[i] = (int)(t - y*base);
        t = y;
    }
    while (t > 0) {
        y = t / base;
        a[s++] = (int)(t - y*base);
        t = y;
    }
}

void tlong::div(int b) {
    int t = 0;
    for (int i = s - 1; i >= 0; --i) {
        t = t*base + a[i];
        a[i] = (int)(t / b);
        t -= a[i]*b;
    }
    while (s > 0) {
        if (a[s - 1] == 0) --s; else break;
    }
}

int tlong::mod(int b) {
    int mb = base % b;
    int t = 0;
    for (int i = s - 1; i >= 0; --i) {
        t = (t*mb + a[i]) % b;
    }
    return (int)t;
}

tlong gcd(tlong a, tlong b) {
    tlong res(1);
    a.sign = 1;
    b.sign = 1;

    while (a.size() > 1 || b.size() > 1) {
        if (a == 0) return (res*b);
        if (b == 0) return (res*a);
        
        if ((a[0] & 1) == 0 && (b[0] & 1) == 0) {
            res *= 2;
            a.half();
            b.half();
        } else {
            if ((a[0] & 1) && (b[0] & 1)) {
                if (a > b) a -= b; else b -= a;
            }

            while ((a[0] & 1) == 0) { a.half(); }
            while ((b[0] & 1) == 0) { b.half(); }
        }
    }
    return (res*gcd(a[0], b[0]));
}

int gcd(int a, int b) {
    while (a > 0 && b > 0) {
        if (a > b) a %= b; else b %= a;
    }
    return (a + b);
}

void swap(tlong &a, tlong &b) {
    tlong c = a;
    a = b;
    b = a;
}

void tlong::operator += (tlong b) {
    if (b.s == 0) return;
    if (sign == b.sign) add(b); else {
        int dres = diff(b);
        if (dres == 0) s = 0; else 
        if (dres > 0) sub(b); else {
            b.sub(*this);
            s = b.s;
            forn(i, s) { a[i] = b[i]; }
            sign = b.sign;
        }
    }
    if (s == 0) sign = 1;
}

void tlong::operator -= (tlong b) {
    if (b.s == 0) return;
    b.sign *= -1;
    if (sign == b.sign) add(b); else {
        int dres = diff(b);
        if (dres == 0) s = 0; else
        if (dres > 0) sub(b); else {
            b.sub(*this);
            s = b.s;
            forn(i, s) { a[i] = b[i]; }
            sign = b.sign;
        }
    }
    if (s == 0) sign = 1;
}

void tlong::operator *= (tlong b) {
    if (b.s == 0) {
        s = 0;
        sign = 1;
    } else {
        sign *= b.sign;
        b.sign = 1;
        mul(b);
    }
}

void tlong::operator /= (tlong b) {
    assert(b.s != 0);
    sign *= b.sign;
    b.sign = 1;
    if (b.s == 1) div(b[0]); else div(b);
}

void tlong::operator %= (tlong b) {
    assert(b.s != 0);
    tlong c = *this / b;
    *this -= c*b;
}
    
void tlong::operator += (int b) {
    if (b == 0) return;
    tlong c(b);
    *this += c;
}

void tlong::operator -= (int b) {
    if (b == 0) return;
    tlong c(b);
    *this -= c;
}

void tlong::operator *= (int b) {
    if (b == 0) {
        s = 0;
        sign = 1;
    } else {
        if (b < 0) {
            sign *= -1;
            b *= -1;
        }
        mul(b);
    }
}

void tlong::operator /= (int b) {
    assert(b != 0);
    if (b < 0) {
        sign *= -1;
        b *= -1;
    }
    div(b);
}

void tlong::operator %= (int b) {
    assert(b != 0);
    *this = tlong(mod(b));
}
            
void tlong::half() {
    int t = 0;
    for (int i = s - 1; i >= 0; --i) {
        t = (a[i] + t*base);
        a[i] = (t >> 1);
        t &= 1;                                        
    }
    while (s > 0) {
        if (a[s - 1] == 0) --s; else break;
    }
}

int tlong::operator [] (int x) {
    if (x >= s || x < 0) return -1;
    return a[x];
}

tlong tlong::operator = (tlong b) {
    s = b.s;
    forn(i, s) {
        a[i] = b[i];
    }
    sign = b.sign;
                
    return b;
}

tlong tlong::operator = (i64 b) {
    tlong c(b);
    s = c.s;
    forn(i, s) {
        a[i] = c[i];
    }
    sign = c.sign;
                
    return c;
}

string tlong::tostring() {
    if (s == 0) return string("0");

    ostringstream out;
    if (sign == -1) out << "-";
    out << a[s - 1];
    for (int i = s - 2; i >= 0; --i) {
        int j = 10;
        while (j <= a[i]) j *= 10;
        while (j < base) {
            j *= 10;
            out << "0";
        }
        out << a[i];
    }

    return out.str();
}

int tlong::toInt() {
    int res = 0;
    for (int i = s - 1; i >= 0; --i) {
        res = 10*res + a[i];
    }
    return res;
}

int tlong::size() {
    return s;
}

tlong::tlong() {
    sign = 1;
    s = 0;
}

tlong::tlong(i64 x) {
    sign = 1;
    s = 0;
    if (x == 0) return;
    if (x < 0) {
        sign = -1;
        x = -x;
    }
    int i = 1;
    int cur = 0;
    while (x >= 0) {
        if (i == base || x == 0) {
            a[s++] = cur;
            cur = 0;
            i = 1;
        }
        if (x == 0) break;
        cur = (int)(cur + (x%10)*i);
        x /= 10;
        i *= 10;
    }
}

// ---------------- </tlong> ----------- //

const int nmax = 100001;

int n;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        cerr << "-----" << endl;
        scanf("%d", &n);
        n--;
        pair < tlong, tlong > res(3, 1);
        tlong a, b;
        while (n > 0) {
            a = 3*res.first + 5*res.second;
            b = res.first + 3*res.second;
            res.first = a, res.second = b;
            n--;
            cerr << "res: " << res.first.tostring() << " " << res.second.tostring() << endl;
        }

        int result = a[0];
        b = res.second * res.second * 5;
        tlong left = 1, right = b;
        while (left + 1 < right) {
            a = (left + right);
            a /= 2;
            if (a*a < b) left = a; else right = a;
        }
        result += left[0];
        
        printf("Case #%d: %03d\n", testid + 1, result % 1000);
    }

    return 0;
}
