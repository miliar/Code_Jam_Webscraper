#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

int ret[1<<10][10];
int n, m;
int maski[10];

int newmask(int a) {
    int newr = 0;
    FOR(i, 1, n-1)
        if ((a&(1<<i))!=0)
            newr |= (1<<(i-1));
    FOR(i, 0, n-2)
        if ((a&(1<<i))!=0) newr |= (1<<(i+1));
    return newr;
}

int cnt(int m) {
    int ret = 0;
    while(m!=0) {
        ret += (m&1);
        m>>=1;
    }
    return ret;
}

bool correct(int x) {
    REP(i, n) if ((x&(1<<i))!=0 && (x&(1<<(i+1)))!=0) return false;
    return true;
}

int get(int maska, int p) {
    if (p==-1) return 0;
    if (ret[maska][p]!=-1) return ret[maska][p];
    ret[maska][p] = 0;
    REP(i, 1<<n) if ((maska&i)==0 && correct(i))
        ret[maska][p] >?= cnt(i)+get(newmask(i)|(p>0 ? maski[p-1] : 0), p-1);
    //printf("%d %d = %d\n", maska, p, ret[maska][p]);
    return ret[maska][p];
}

char buf[20];

int main() {
    int zzz;
    scanf("%d", &zzz);
    FOR(zz, 1, zzz) {
        scanf("%d%d\n", &m, &n);
        REP(i, m) {
            scanf("%s\n", buf);
            maski[i] = 0;
            REP(j, n) maski[i] = 2*maski[i] + (buf[j]=='x');
            //printf("%d %d\n", maski[i], newmask(maski[i]));
        }
        memset(ret, -1, sizeof(ret));
        printf("Case #%d: %d\n", zz, get(maski[m-1], m-1));
    }
    return 0;
}
