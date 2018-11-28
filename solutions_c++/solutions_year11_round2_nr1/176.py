#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;

#define REP(i, n) for(int i=0; i<n; ++i)
#define ST first
#define ND second
#define PB push_back
#define VAR(v,n) __typeof__(n) v=(n)
#define FE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()

#define MAXN 102

char T[MAXN][MAXN];
double WP[MAXN];
double OWP[MAXN];
double OOWP[MAXN];

int total[MAXN];
int wins[MAXN];

void testcase(){
int n; scanf("%d", &n);
REP(i, n){
    scanf("%s", T[i]);
}

REP(i, n){
    wins[i] = 0;
    total[i] = 0;
    REP(j, n){
        if ( T[i][j] == '1' ){
            wins[i] ++;
        }
        if ( T[i][j] != '.' ){
            total[i] ++;
        }
    }
}

REP(i, n){
    long double r = 0;
    REP(j, n) if ( T[i][j] != '.' ) {
        int t = total[j];
        int w = wins[j];
        if ( T[j][i] != '.' ) t--;
        if ( T[j][i] == '1' ) w--;
        r += ( (double) w / (double) t );
    }
    OWP[i] = r / (double) total[i];
}

REP(i, n){
    long double r = 0;
    REP(j, n) if ( T[i][j] != '.' ) {
        r += OWP[j];
    }
    OOWP[i] = r / (double) total[i];
}

REP(i, n){
    printf("%.8lf\n", 0.25 * ( wins[i] / (double) total[i] ) + 0.50 * OWP[i] + 0.25 * OOWP[i] );
}
}

int main(){
int z; scanf("%d", &z);
REP(i, z) {
    printf("Case #%d:\n", i+1);
    testcase();
}
return 0;
}

