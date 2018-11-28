/* All includes and defines required by the templates
 * Just add it at the beginning and all will work OOB */
#include<iostream>
#include<set>
#include<iomanip>
#include<sstream>
#include<fstream>
#include<stack>
#include<cstdio>
#include<cmath>
#include<cassert>
#include<queue>
#include<vector>
#include<list>
#include<algorithm>
#include<map>
#include<cstring>
#include<cctype>


using namespace std;
#define fe(e,C) for(__typeof((C).begin()) e = (C).begin(); e != (C).end(); e++)
#define fi(i,n) for(int i = 0, i##end = (n); i < i##end; i++)
#define ft(i,a,b) for(int i = (a), i##end = (b); i <= i##end; i++)
#define fd(i,a,b) for(int i = (a), i##end = (b); i >= i##end; i--)
#define fs(i,C) fi(i,SZ(C))
#define ALL(V) (V).begin(), (V).end()
#define SET(T, c) memset(T, c, sizeof(T))
#define VI vector<LL>
#define PB push_back
#define PII pair<int, int>
#define SEC second
#define FST first
#define MP make_pair
#define SZ(C) ((int)(C).size())
#define SQR(a) ((a)*(a))

typedef unsigned long long ULL;
typedef long long LL;

int ri() { int n; scanf(" %d", &n); return n; }
void pi(int n) { printf("%d\n", n); }
string rs() { char buf[10000]; buf[9999]=-1; scanf(" %s ", buf); assert(buf[9999]==-1); return buf; }
void ps(const string &s) { printf("%s\n", s.c_str()); }
template<class R, class T>
R conv(const T &t) { stringstream ss; ss << t; R r; ss >> r; return r; }
LL gcd(LL a, LL b) { if(b == 0) return a; else return gcd(b, a % b); }
struct pt { int x, y; pt(int x, int y):x(x), y(y) {} };

LL pow(LL x, LL n, LL p) {
    LL y = 1;
    fd(i, 24, 0) {
        y = ((LL)y * y) % p;
        if(((1<<i)&n)!=0)
            y = ((LL)y*x) % p;
    }
    return y;
}

LL inv(LL a, LL p) {
    return pow(a, p-2, p);
}

VI Prims;

bool validate(LL a, LL b, LL seed, LL p, VI &s) {
    if(s[0] != seed) return false;
    
    ft(i, 1, SZ(s)-1) {
        seed = (seed * a + b) % p;
        if(seed != s[i])
            return false;
    }

    return true;
}

void solve(LL t) {
    printf("Case #%lld: ", t);
    LL D = ri(), K = ri();
    VI s;
    LL equal = -1;

    fi(i,K) {
        s.PB(ri());
        if(SZ(s) >= 2) {
            LL j = SZ(s)-1;
            if(s[j-1] == s[j]) {
                equal = s[j];
            }
        }
    }

    if(equal != -1) {
        printf("%lld\n", equal);
        return;
    }

    if(K < 3) {
        printf("I don't know.\n");
        return;
    }

    VI next;
    LL minP = *max_element(ALL(s)) + 1;
    LL maxP = 1;
    fi(i, D) maxP *= 10;
    fe(pi, Prims) {
        LL p = *pi;
        if(p > maxP) break;
        if(minP <= p) {
            LL a = ((LL)(s[1] - s[2]) * inv(s[0] - s[1], p)) % p;
            a = (a % p + p)%p;
            LL b = (((LL)((s[2] - (((LL)a * s[1]) % p))) % p + 2 * p) % p);
            b = (b % p + p)%p;
            if(validate(a, b, s[0], p, s)) {
                next.PB(((LL)a * s.back() + b) % p);
                //cout<<"dla p="<<p<<" a="<<a<<" b="<<b<<" next="<<next.back()<<endl;
            }
        }
    }
    if(*max_element(ALL(next)) == *min_element(ALL(next))) {
        printf("%lld\n", next.back());
    }
    else {
        printf("I don't know.\n");
    }
}


int main(){
    vector<bool> isPr(1000001, true);
    ft(i, 2, 1000)
        if(isPr[i])
            for(LL j = i * i; j <= 1000000; j+=i)
                isPr[j] = false;
    ft(i,2,1000000)
        if(isPr[i])
            Prims.PB(i);

    fi(t,ri()) solve(t+1);
    return 0;
}

