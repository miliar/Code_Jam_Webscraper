#include <cstdio>
#include <vector>
#include <set>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a) < 0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

typedef long long ll;

int main() {
    int z;
    scanf("%d", &z);
    FOR(zz, 1, z) {
        ll n, A, B, C, D, x, y, M;
        scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x, &y, &M);
        ll tmp[3][3];
        REP(i, 3) REP(j, 3) tmp[i][j] = 0;
        REP(i, n) {
            tmp[x%3][y%3]++;
            x = (A*x+B)%M;
            y = (C*y+D)%M;
            
        }
        ll ret = 0;
        REP(a1, 3) REP(a2, 3)
        REP(b1, 3) REP(b2, 3) if(a1!=b1 || a2!=b2)
        REP(c1, 3) REP(c2, 3) if(!((a1==c1 && a2==c2) || (b1==c1 && b2==c2))){
        if ((a1+b1+c1)%3==0 && (a2+b2+c2)%3==0)
            ret += tmp[a1][a2]*tmp[b1][b2]*tmp[c1][c2];
        }
        ret /= 6;
        
        REP(a1, 3) REP(a2, 3)
        REP(b1, 3) REP(b2, 3) if(a1!=b1 || a2!=b2)
        if ((2*a1+b1)%3==0 && (2*a2+b2)%3==0 && tmp[a1][a2]>=2)
            ret += tmp[a1][a2]*(tmp[a1][a2]-1)*tmp[b1][b2]/2;
            
        REP(i, 3) REP(j, 3)
        ret += tmp[i][j]*((ll)tmp[i][j]-1)*((ll)tmp[i][j]-2)/6;
        
        
        printf("Case #%d: %lld\n", zz, ret);
    }
    return 0;
}
