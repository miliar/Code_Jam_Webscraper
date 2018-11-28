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
const int MAXN  = 2010;

int col[MAXN];
VI out[MAXN];
int u[MAXN];
int v[MAXN];
int next[MAXN];
int prev[MAXN];
VI::iterator cur[MAXN];
int clm=inf;

void go(int beg, VI::iterator it, int end) {
    if (it != out[beg].end()) {;
        VI::iterator jt = it;
        ++jt;
        go(beg, jt, *it);
    }
    if (end == beg+1) return;

    int b = *it;
    int no=2;
    while (b != end) {
        ++no;
        if (cur[b] != out[b].end()) {
            VI::iterator jt = cur[b];
            ++jt;
            go(b,jt,*cur[b]);
        }
        b = *cur[b];
    }
    clm = min(clm, no);
}

void go2(int beg, VI::iterator it, int end) {
    if (end == beg+1) return;
    int c1 = col[beg];
    int c2 = col[end];
    int b = *it;
    int c = -1;
    int prev = c1;
    while(b != end) {
        c = (c+1)%clm;
        while(c == c1 || c == c2) c = (c+1)%clm;
        while( c== prev || c==c2) c =(c+1)%clm;  
        col[b] = c;
     //   printf("(%d, %d), %d -> %c\n",beg, end ,b,c+'A');
        prev = c;
        b = *cur[b];
    }
    if (it != out[beg].end()) {
        VI::iterator jt = it;
        ++jt;
        go2(beg, jt, *it);
    }
 //   printf("%d - %d\n", beg,end);
    b = *it;
    while (b != end) {
   //     printf("%d -- %d : %d --%d\n", beg, end, b, *cur[b]);
        if (cur[b] != out[b].end()) {
    //        printf("sub\n");
            VI::iterator jt = cur[b];
            ++jt;
            go2(b,jt,*cur[b]);
        }
        b = *cur[b];
    }

}

void solve(int tcase) {
    printf("Case #%d: ", tcase);
    int n,m;
    clm =inf;
    scanf("%d%d", &n, &m);
    REP(i, m) {
        scanf("%d", &u[i]);
        --u[i];
    }
 //  printf("%d\n", n);
    REP(i, m) {
        scanf("%d", &v[i]);
        --v[i];
    //    printf("%d %d\n", u[i],v[i]);
        if (u[i]<v[i]) out[u[i]].PB(v[i]);
        else out[v[i]].PB(u[i]);
    }
    REP(i,n) {
        if (i<n) out[i].PB(i+1);
        sort(ALL(out[i]));
        reverse(ALL(out[i]));
    }
    REP(i,n) next[i]= (i+1)%n;
    REP(i,n) {
        prev[i]=(i+n-1)%n;
        col[i]=-1;
        cur[i]=out[i].begin();
    }
    go(0,cur[0],n-1);
    printf("%d\n", clm);
    col[0]=0;
    col[n-1]=1;
    go2(0,cur[0],n-1);
    REP(i, n) printf("%d ", col[i]+1);
    printf("\n");
    REP(i,n) out[i].clear();
}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
