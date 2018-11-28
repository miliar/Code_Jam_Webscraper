
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

#define maxC 1005
int t[maxC];
int n, C, L;
lli T;

lli get_ith(int i) {
    return t[i % C];
}

int tt[10005];

lli get_cost(int start, int ile) {
    CLR(tt);
    fup(i, start, n - 1) tt[get_ith(i)]++;
    lli sum = 0;
    fdo(i, 10000, 0) {
        int f = min(ile, tt[i]); 
        tt[i] -= f;
        ile -= f;
        sum += (lli)i * (lli)f;

        sum += (lli)i * 2 * (lli)tt[i];
        
    }
    return sum;
}

int main() {
    int cas;
    scanf("%d", &cas);
    fup(ca, 1, cas) {
        cin >> L >> T >> n >> C;
        fup(i, 0, C - 1) scanf("%d", &t[i]);
        lli sum = 0;

        fup(i, 0, n - 1) {
            lli sum2 = sum + get_ith(i) * 2;
            if (sum <= T && T <= sum2) {
                lli c1 = get_cost(i + 1, L - 1);
                lli c2 = get_cost(i + 1, L);
                
                lli x1 = (T - sum) / 2; 
                lli d = get_ith(i) - x1;
                c1 = T + d + c1;

                c2 = sum2 + c2;

                sum = min(c1, c2);
                break;
            } else sum = sum2;
        }
        printf("Case #%d: %lld\n", ca, sum);

    }
    return 0;
}


