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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>


using namespace std;

#define FOR(i,a,b) for (int (i) = (a); (i) < (b); (i)++)
#define ALL(M) (M).begin(), (M).end()
#define CLR(M, v) memset(M, v, sizeof(M))
#define SI(V) (int)(V.size())
#define PB push_back
#define MP make_pair

typedef long long i64;
typedef vector<int> VI;
typedef vector<string> VS;

const int INF = 0x3F3F3F3F;
const i64 LINF = 0x3F3F3F3F3F3F3F3FLL;
const double EPS = 1E-14;

template<class T> T SQR(T x) { return x*x; }

template <class T> T gcd(T a, T b) { return (b!=0) ? gcd(b, a % b) : a; }

// Needed digits MAX_DIGITS / log(BASE)
const int NDIG = 25;
const int BASE = 10000;
const int NBASE = 4;        // log10(BASE)
const int BASEDIG = 14;
const int FRAC = 0;

struct Num {
	int v[NDIG], n;
	Num(int x = 0) : n(FRAC+1) { memset(v, 0, sizeof(v)); v[n++] = x; fix(); }
	Num(char *s) : n(FRAC+1) {
        memset(v, 0, sizeof(v)); int sign = 1;
        while (*s && !isdigit(*s)) if (*s++ == '-') sign = -1;
        char t[NDIG*NBASE], *t1 = t, *p; memcpy(t, s, sizeof(t)); p = t + strlen(t);
        while (p > t1) {
            *p = 0; p = max(t1, p - NBASE);
            sscanf(p, "%d", &v[n]); v[n++] *= sign;
        }
        fix();
    }
	inline Num& fix(int m = 0) {
        n = max(m, n); int sign = 0;
        for (int i = 1, e = 0; i <= n || e && (n = i); i++) {
            v[i] += e; e = v[i] / BASE; v[i] %= BASE;
            if (v[i]) sign = (v[i] > 0) ? 1 : -1;
        }
        for (int i = 1; i <= n; i++) if (v[i] * sign < 0)
            v[i] += sign * BASE, v[i+1] -= sign;
        while (n && !v[n]) n--;
        return *this;
	} 
	int cmp(const Num &x = 0) const {
        int i = max(n, x.n), t;
        while (1) if ((t = v[i]-x.v[i]) || i-- == 0) return (FRAC && i<=1) ? 0 : t;
    }
    bool operator <(const Num& x) const { return cmp(x) < 0; }
    bool operator ==(const Num& x) const { return cmp(x) == 0; }
    bool operator !=(const Num& x) const { return cmp(x) != 0; }
	Num& operator+=(const Num &x) {
        for (int i = 1; i <= x.n; i++) v[i] += x.v[i];
        return fix(x.n);
	}
	Num operator+(const Num &x) { return Num(*this)+=x; }
	Num& operator -=(const Num& x) {
        for (int i = 1; i <= x.n; i++) v[i] -= x.v[i];
        return fix(x.n);
    }
    Num operator-(const Num& x) { return Num(*this) -= x; }
    Num operator -() { Num r; return r -= *this; }
	void ams(const Num& x, int m, int b) { // *this += (x * m) << b;
        for (int i = 1, e = 0; (i <= x.n || e) && (n = i + b); i++)
            v[i+b] += x.v[i] * m + e, e = v[i+b] / BASE, v[i+b] %= BASE;
    }
    Num operator *(const Num& x) {
        Num r; int i;
        for (i = 1; i <= n; i++) r.ams(x, v[i], i-1);
        if (FRAC) for (i = 1; i <= r.n; i++) r.v[i] = (i <= r.n-FRAC) ? r.v[i+FRAC] : 0;
        r.n-=FRAC;
        return r;
    }
    Num& operator *=(const Num& x) { return *this = *this * x; }
    Num div(const Num& x) {
        if (x == 0) return 0;
        Num q; q.n = max(n - x.n + 1, 0);
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
    void div2() {
		for (int i = n, p = 0; i > 0; i--) 
			v[i] += p, p = ((v[i]&1) ? BASE : 0), v[i]>>=1;
		while (n && !v[n]) n--;
	}
    Num& operator /=(const Num& x) { return *this = div(x); }
    Num& operator %=(const Num& x) { div(x); return *this; }
    Num operator /(const Num& x) { return Num(*this).div(x); }
    Num operator %(const Num& x) { return Num(*this) %= x; }
    Num pow(int k) {
        if (!k) return 1;
        if (k==1) return *this;
        Num x = (*this**this).pow(k>>1);
        return (k&1) ? *this*x : x;
    }
    Num root(int x) {
        if (cmp() == 0 || cmp() < 0 && x % 2 == 0) return 0;
        if (*this == 1 || x == 1) return *this;
        if (cmp() < 0) return -(-*this).root(x);
        Num lo = 1, hi = *this, mi;
        for (int i = 0; lo < hi && i < 1000; i++) {
            mi = lo + hi; mi.div2();
            int c = cmp(mi.pow(x));
            if (c == 0) break;
            (c < 0) ? (hi = mi) : (lo = mi, mi.v[0]+1);
        }
        return mi;
    }
    friend Num abs(const Num &x) {
        Num ret = x;
        for(int i = 1; i <= x.n; i++) ret.v[i] = abs(x.v[i]);
        return ret;
    }
    operator string() const {
        ostringstream s; s << v[n];
        for (int i = n - 1; i > 0; i--) {
            if (i==FRAC) s << '.';
            s.width(NBASE); s.fill('0'); s << abs(v[i]);
        }
        string ss = s.str();
        return ss;
        // Check for required float precision total = NBASE*FRAC
        //return ss.substr(0, ss.size()-6);
    }
    friend void print(const Num& x) {
        string s = (string) x;
        int check = 0;
        for (int i = 0; i < (int)s.size(); i++) if (s[i]!='.') check += s[i]-'0';
        printf("%d %s\n", check%10, s.c_str());
    }
};


////////////////////////////////////////////////////////////////////////////////

const int MAXV = 1010;

int N;
Num NUM[MAXV];
Num T, Y;

int main() {
    
//	freopen("B.in","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-large.in","r",stdin);freopen("B-large.ans","w",stdout);

    char S[100];

    int TC;
    scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        // Read input.
        scanf("%d", &N);
        FOR(i,0,N) {
            scanf("%s", S);
            NUM[i] = Num(S);
        }
                
        // Compute T value.
        T = abs(NUM[0]-NUM[1]);
        FOR(i,2,N) T = gcd(T,abs(NUM[0]-NUM[i]));
        
        // Compute Y.
        Y = ((NUM[0]+T-1)/T * T) - NUM[0];
        
        // Prints result.
        printf("Case #%d: %s\n", tc, string(Y).c_str());
    }

	return 0;
}
