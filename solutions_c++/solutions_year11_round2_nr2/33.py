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

PII in[300];


void solve(int tcase) {
    printf("Case #%d: ", tcase);
    int d,c;
    scanf("%d%d",&c, &d);
    d*=2;
    REP(i, c) {
        scanf("%d%d", &in[i].FI, &in[i].SE);
        in[i].FI *= 2;
    }
    sort(in, in+c);
    LL beg = 0, end = (1ll<<50);
    while(end> beg) {
        LL med = (beg+end)/2;
      //  printf("med=%lld\n", med);

        LL prev = -inf;
        bool ok=true;
        REP(i, c) {
            prev = max(prev, in[i].FI-med);
          //  printf("%lld - %lld\n", prev, prev+(in[i].SE-1)*d);
            if(prev+(LL)(in[i].SE-1)*d-in[i].FI > med) ok =false;
            prev += (LL)(in[i].SE)*d;
        }
        if (ok) end = med;
        else beg = med + 1;
    }
    printf("%.2lf\n", beg/2.0);



}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
