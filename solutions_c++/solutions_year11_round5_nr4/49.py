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

char inp[140];
void solve(int tcase) {
    REP(i, 140) inp[i]='\0';
    printf("Case #%d: ", tcase);
    scanf("%s", inp);
    int ns = strlen(inp);
    LL sqb = 0;
    vector<LL> pos;
    int cnt = 0;
    FOR(i, 0, ns-1) {
        sqb *= 2;
        if (inp[i]=='1') ++sqb;
        else if (inp[i]=='?') {
            pos.PB(1LL<<(ns-1-i));
            ++cnt;
        }
    }
    REP(i, 1LL<<cnt) {
        int ii=i;
        LL cur = sqb;
        REP(k, cnt) {
            if (ii&1) cur += pos[k];
            ii>>=1;
        }
        long double sqr = sqrt((long double) cur);
        LL sq = (LL) round(sqr);
        if (sq*sq == cur) {
            FORD(i, ns-1, 0) {
                inp[i]=(cur&1)+'0';
                cur >>= 1;
            }
            printf("%s\n", inp);
            return;
        }
    }



}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
