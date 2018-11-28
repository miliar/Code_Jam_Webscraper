#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef pair<int, int> pii;

#define Rep(i,n) for(typeof(n) i = 0; i < (n); ++i)
#define Repd(i,n) for(typeof(n) i = (n)-1; i >= 0; --i)
#define For(i,a,b) for(typeof(b) i = (a); i <= (b); ++i)
#define Ford(i,a,b) for(typeof(a) i = (a); i >= (b); --i)
#define Fit(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define Fitd(i,v) for(typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))
#define nl puts("")
#define sp printf(" ")
#define ok puts("ok")

template<class F, class T> T convert(F a, int p = -1) { stringstream ss; if (p >= 0) ss << fixed << setprecision(p); ss << a; T r; ss >> r; return r; }
template<class T> void db(T a, int p = -1) { if (p >= 0) cout << fixed << setprecision(p); cout << a << " "; }
template<class T> T gcd(T a, T b) { T r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> T sqr(T x) { return x * x; }
template<class T> T cube(T x) { return x * x * x; }
template<class T> struct Triple { T x, y, z; Triple() {} Triple(T _x, T _y, T _z) : x(_x), y(_y), z(_z) {} };
template<class T> Triple<T> euclid(T a, T b) { if (b == 0) return Triple<T>(1, 0, a); Triple<T> r = euclid(b, a % b); return Triple<T>(r.y, r.x - a / b * r.y, r.z); }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return s == 0 ? 0 : cntbit(s >> 1) + (s & 1); }
const int bfsz = 1 << 16; char bf[bfsz + 5]; int rsz = 0;int ptr = 0;
char gc() { if (rsz <= 0) { ptr = 0; rsz = fread(bf, 1, bfsz, stdin); if (rsz <= 0) return EOF; } --rsz; return bf[ptr++]; }
void ga(char &c) { c = EOF; while (!isalpha(c)) c = gc(); }
int gs(char s[]) { int l = 0; char c = gc(); while (isspace(c)) c = gc(); while (c != EOF && !isspace(c)) { s[l++] = c; c = gc(); } s[l] = '\0'; return l; }
template<class T> bool gi(T &v) {
	v = 0; char c = gc(); while (c != EOF && c != '-' && !isdigit(c)) c = gc(); if (c == EOF) return false; bool neg = c == '-'; if (neg) c = gc();
    while (isdigit(c)) { v = v * 10 + c - '0'; c = gc(); } if (neg) v = -v; return true;
}

const double PI = 2 * acos(0);
const string months[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
const int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const int dr[] = {-1, 0, +1, 0};
const int dc[] = {0, +1, 0, -1};
const int inf = (int)1e9 + 5;
const ll linf = (ll)1e16 + 5;
const double eps = 1e-9;

#define maxn 15000000

int p10[20], digs[maxn + 5];
vector<pii> rec;

int move_digits(int n, int k) {
    if (k == 0 || k == digs[n]) return n;
    int x = n % p10[k];
    int y = n / p10[k];
    int m = x * p10[digs[y]] + y;
    return (digs[m] == digs[n]) ? m : -1;
}

void doit(int a, int b) {
    For(n, a, b) {
        For(k, 1, digs[n] - 1) {
            int m = move_digits(n, k);
            if (m != -1 && n < m && m <= b) {
                rec.pb(mp(n, m));
            }
        }
    }
    sort(all(rec));
    rec.erase(unique(all(rec)), rec.end());
}

int go(int a, int b) {
    int ret = 0;
    Rep(i, sz(rec)) {
        int x = rec[i].fi, y = rec[i].se;
        if (a <= x && x < y && y <= b) ++ret;
    }
    return ret;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    p10[0] = 1;
    For(i, 1, 9) p10[i] = p10[i - 1] * 10;
    
    Rep(i, 10) digs[i] = 1;
    For(i, 10, maxn) digs[i] = digs[i / 10] + 1;
    
    doit(1, 2000000);
    
    int ntest;
    gi(ntest);
    
    int a, b;
    For(test, 1, ntest) {
        gi(a); gi(b);
        printf("Case #%d: %d\n", test, go(a, b));
    }
    
    return 0;
}
