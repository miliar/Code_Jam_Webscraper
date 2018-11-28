#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <utility>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<long> VL;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)

#define pb push_back
#define mp make_pair
#define st first
#define nd second

LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }
int bc(LL x) { return x?bc(x>>1)+(x&1):0; }

inline int rnd(int n) { return rand()%n; }

inline int GI() { int x; scanf("%d",&x); return x; }
inline LL GL() { LL x; scanf("%lld",&x); return x; }
inline char GC() { char x[2]; scanf("%s",x); return x[0]; }
inline void GS(char *x) { scanf("%s",x); }

const int N = 512;

int r,c,dumb_d;
int val[N][N], sum[N][N], sumx[N][N], sumy[N][N], tmp[N][N];
char buf[N];

bool check(int i, int j, int k) {
    
    int tmp = 0;

    tmp += sum[i][j]+sum[i+k][j+k]-sum[i][j+k]-sum[i+k][j];
    tmp -= val[i][j]+val[i+k-1][j]+val[i][j+k-1]+val[i+k-1][j+k-1];
    tmp *= (i+i+k-1);
    tmp -= 2 * (sumx[i][j]+sumx[i+k][j+k]-sumx[i][j+k]-sumx[i+k][j]);
    tmp += 2 * (i*val[i][j]+(i+k-1)*val[i+k-1][j]+i*val[i][j+k-1]+(i+k-1)*val[i+k-1][j+k-1]);

    if (tmp != 0) return false;

    tmp += sum[i][j]+sum[i+k][j+k]-sum[i][j+k]-sum[i+k][j];
    tmp -= val[i][j]+val[i+k-1][j]+val[i][j+k-1]+val[i+k-1][j+k-1];
    tmp *= (j+j+k-1);
    tmp -= 2 * (sumy[i][j]+sumy[i+k][j+k]-sumy[i][j+k]-sumy[i+k][j]);
    tmp += 2 * (j*val[i][j]+j*val[i+k-1][j]+(j+k-1)*val[i][j+k-1]+(j+k-1)*val[i+k-1][j+k-1]);

    if (tmp != 0) return false;

    return true;


}

void single_case(int case_number) {
    scanf("%d%d%d",&r,&c,&dumb_d);
    REP(i,r) {
        scanf("%s",buf);
        REP(j,c) val[i][j] = buf[j]-'0';
    }

    REP(i,r) {
        tmp[i][0] = 0;
        REP(j,c) tmp[i][j+1] = tmp[i][j] + val[i][j];
    }
    REP(j,c+1) {
        sum[0][j] = 0;
        REP(i,r) sum[i+1][j] = sum[i][j] + tmp[i][j];
    }
    REP(i,r) {
        tmp[i][0] = 0;
        REP(j,c) tmp[i][j+1] = tmp[i][j] + val[i][j]*i;
    }
    REP(j,c+1) {
        sumx[0][j] = 0;
        REP(i,r) sumx[i+1][j] = sumx[i][j] + tmp[i][j];
    }
    REP(i,r) {
        tmp[i][0] = 0;
        REP(j,c) tmp[i][j+1] = tmp[i][j] + val[i][j]*j;
    }
    REP(j,c+1) {
        sumy[0][j] = 0;
        REP(i,r) sumy[i+1][j] = sumy[i][j] + tmp[i][j];
    }

    /*
    printf("VAL:\n");
    REP(i,r+1) { REP(j,c+1) printf("%4d",val[i][j]); printf("\n"); }
    printf("SUM:\n");
    REP(i,r+1) { REP(j,c+1) printf("%4d",sum[i][j]); printf("\n"); }
    printf("SUMX:\n");
    REP(i,r+1) { REP(j,c+1) printf("%4d",sumx[i][j]); printf("\n"); }
    printf("SUMY:\n");
    REP(i,r+1) { REP(j,c+1) printf("%4d",sumy[i][j]); printf("\n"); }
    */

    int best = 0;
    FOR(k,3,min(r,c)+1)
        REP(i,r+1-k)
            REP(j,c+1-k)
                if (check(i,j,k)) best = k;

    printf("Case #%d: ",case_number);
    //printf("Case #%d:\n",case_number);

    if (best==0) printf("IMPOSSIBLE\n"); else printf("%d\n",best);
}

int main() {
    int j;
    scanf("%d",&j);
    REP(i,j) single_case(i+1);
    return 0;
}


