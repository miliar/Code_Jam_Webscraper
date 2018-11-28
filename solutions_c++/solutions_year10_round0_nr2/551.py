#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

struct BigNum {
#define REDUCE() while(len>1 && !cyf[len-1]) len--;
    static const int BASE = 1000000000, BD = 9;
    int len, al;
    LL* cyf;

    BigNum(int v = 0, int l = 2) : len(1), al(l), cyf(new LL[l]) {
        REP(x, al) cyf[x] = 0;
        if ((cyf[0] = v) >= BASE) przen(1);
    }

    BigNum(const BigNum & a) : len(a.len), al(len), cyf(new LL[al]) {
        REP(x, al) cyf[x] = a.cyf[x];
    }

    ~BigNum() {
        delete cyf;
    }

    void Res(int l) {
        if (l > al) {
            LL* n = new LL[l = max(l, 2 * al)];
            REP(x, l) n[x] = x >= al ? 0 : cyf[x];
            delete cyf;
            cyf = n;
            al = l;
        }
    }

    void przen(int p) {
        int x = 0;
        for (; x < p || cyf[x] < 0 || cyf[x] >= BASE; x++) {
            Res(x + 2);
            if (cyf[x] < 0) {
                LL i = (-cyf[x] - 1) / BASE + 1;
                cyf[x] += i*BASE;
                cyf[x + 1] -= i;
            } else
                if (cyf[x] >= BASE) {
                LL i = cyf[x] / BASE;
                cyf[x] -= i*BASE;
                cyf[x + 1] += i;
            }
        }
        len = max(len, x + 1);
        REDUCE();
    }
#define OPER1(op) bool operator op (const BigNum &a) const

    OPER1( ==) {
        if (a.len != len) return 0;
        REP(x, len) if (cyf[x] != a.cyf[x]) return 0;
        return 1;
    }

    OPER1(<) {
        if (len != a.len) return len < a.len;
        int x = len - 1;
        while (x && a.cyf[x] == cyf[x]) x--;
        return cyf[x] < a.cyf[x];
    }

    OPER1(>) {
        return a<*this;
    }

    OPER1( <=) {
        return !(a<*this);
    }

    OPER1( >=) {
        return !(*this<a);
    }

    OPER1( !=) {
        return !(*this == a);
    }

    BigNum & operator=(int a) {
        REP(x, len) cyf[x] = 0;
        len = 1;
        if (cyf[0] = a >= BASE) przen(1);
        return *this;
    }

    void operator+=(int a) {
        cyf[0] += a;
        przen(1);
    }

    void operator-=(int a) {
        cyf[0] -= a;
        przen(1);
    }

    void operator*=(int a) {
        REP(x, len) cyf[x] *= a;
        przen(len);
    }

    int operator/=(int a) {
        LL w = 0;

        FORD(p, len - 1, 0) {
            w = w * BASE + cyf[p];
            cyf[p] = w / a;
            w %= a;
        }
        REDUCE();
        return w;
    }

    int operator%(int a) {
        LL w = 0;
        FORD(p, len - 1, 0) w = (w * BASE + cyf[p]) % a;
        return w;
    }
#define OPER2(op) BigNum& operator op (const BigNum &a)

    OPER2( +=) {
        Res(a.len);
        REP(x, a.len) cyf[x] += a.cyf[x];
        przen(a.len);
        return *this;
    }

    OPER2( -=) {
        REP(x, a.len) cyf[x] -= a.cyf[x];
        przen(a.len);
        return *this;
    }

    OPER2( *=) {
        BigNum c(0, len + a.len);

        REP(x, a.len) {
            REP(y, len) c.cyf[y + x] += cyf[y] * a.cyf[x];
            c.przen(len + x);
        }
        *this = c;
        return *this;
    }

    OPER2( /=) {
        int n = max(len - a.len + 1, 1);
        BigNum d(0, n), prod;

        FORD(i, n - 1, 0) {
            int l = 0, r = BASE - 1;
            while (l < r) {
                int m = (l + r + 1) / 2;
                if (*this < prod + (a * m << i))
                    r = m - 1;
                else
                    l = m;
            }
            prod += a * l << i;
            d.cyf[i] = l;
            if (l) d.len = max(d.len, i + 1);
        }
        *this = d;
        return *this;
    }

    OPER2( %=) {
        BigNum v = *this;
        v /= a;
        v *= a;
        *this -= v;
        return *this;
    }

    OPER2( =) {
        Res(a.len);
        FORD(x, len - 1, a.len) cyf[x] = 0;
        REP(x, a.len) cyf[x] = a.cyf[x];
        len = a.len;
        return *this;
    }

    void readFromCharArray(const char* a) {
        int s = strlen(a);
        *this = 0;
        Res(len = s / BD + 1);
        REP(x, s) cyf[(s - x - 1) / BD] = 10 * cyf[(s - x - 1) / BD] + a[x] - '0';
        REDUCE();
    }

    void write() const {
        printf("%d", int(cyf[len - 1]));
        FORD(x, len - 2, 0) printf("%0*d", BD, int(cyf[x]));
    }

    BigNum & operator>>=(int n) {
        if (n >= len) n = len;
        REP(x, len - n) cyf[x] = cyf[x + n];
        FOR(x, len - n, n) cyf[x] = 0;
        len -= n;
        if (len == 0) len = 1;
        return *this;
    }

    BigNum & operator<<=(int n) {
        if (cyf[0] == 0 && len == 1) return *this;
        Res(len + n);
        FORD(x, len - 1, 0) cyf[x + n] = cyf[x];
        REP(x, n) cyf[x] = 0;
        len += n;
        return *this;
    }

#define OPER3(op) BigNum operator op(const BigNum &a) \
	const {BigNum w=*this;  w op ## = a;  return w; }
#define OPER4(op) BigNum operator op(int a) \
	{BigNum w = *this; w op ## = a; return w; }
    OPER3(+);
    OPER3(-);
    OPER3(*);
    OPER3( /);
    OPER3( %);
    OPER4( <<);
    OPER4( >>);
};

BigNum NatGCD(const BigNum& a, const BigNum& b) {
    return b == BigNum(0) ? a : NatGCD(b, a % b);
}

BigNum roznica(const BigNum& a, const BigNum& b) {
    if (a > b) {
        return a - b;
    }
    return b - a;
}

int main() {
    int c, n;
    char* num = new char[51];
    BigNum* nums = new BigNum[1000];

    scanf("%d\n", &c);
    REP(i, c) {
        scanf("%d", &n);
        REP(j, n) {
            scanf("%s", num);
            BigNum bignum;
            bignum.readFromCharArray(num);
            nums[j] = bignum;
        }
        BigNum gcd = roznica(nums[0], nums[1]);
        FOR(j, 1, n - 2) {
            gcd = NatGCD(gcd, roznica(nums[j], nums[j + 1]));
        }
        BigNum result = (nums[0] % gcd);
        printf("Case #%d: ", i + 1);
        if (result == BigNum(0)) {
            printf("0\n");
        } else {
            result = gcd - result;
            result.write();
            printf("\n");
        }
    }
}
