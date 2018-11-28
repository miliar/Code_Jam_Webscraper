#include<algorithm>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<vector>
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) for(int i=0;i<(n);++i)
#define fup FOR
#define fdo FORD
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
#define siz SIZE
#define CLR memset((x),0,sizeof (x))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SQR(a) ((a)*(a))

#define DEBUG 1
#define debug(x) {if(DEBUG) cerr << #x << " = " << x << endl;}
#define debugv(x) {if(DEBUG) {cerr << #x << " = "; FORE(it,(x)) cerr << *it << " . "; cerr  <<endl;}}

using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef VI vi;
typedef LL lli;

const int inf = 1000000000;
const int MAXN = 1000500;

bool prime[MAXN];
int p[MAXN];
int P;

void sieve() {
    REP(i, MAXN) prime[i]=true;
    prime[0]=prime[1]=false;
    P = 0;
    for(int i = 2; i < MAXN; ++i) {
        if (prime[i]) {
            p[P] = i;
            ++P;
        }
        for (LL j = i;  i*j < MAXN; ++j) {
            prime[i*j] = false;
        }
    }
}

void solve(int tcase) {
    printf("Case #%d: ", tcase);
   long long n;
   scanf("%lld", &n);
   int res = (n != 1);
   REP(i, MAXN) {
       LL pr = p[i];
       if (n < pr*pr) break;
     // printf("%lld %lld %d\n", pr*pr, n, res);
       LL N = n;
       while (N >= pr * pr){
           ++res;
           N /= pr;
       }


   }
   printf("%d\n", res);
}

int main() {
    int t;
    sieve();
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
