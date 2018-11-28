#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

char buf[2000];
char newbuf[2000];
int tab[5];

int main() {
    int z;
    scanf("%d", &z);
    FOR(zz, 1, z) {
        int k;
        scanf("%d\n%s\n", &k, buf);
        REP(i, k) tab[i] = i;
        int len = strlen(buf);
        int ret = len;
        do {
            REP(block, len/k) {
                int from = block*k;
                REP(i, k) newbuf[from+i] = buf[from+tab[i]];
            }
            int tmp = 1;
            FOR(i, 1, len-1) if(newbuf[i]!=newbuf[i-1]) tmp++;
            ret <?= tmp;
        } while (next_permutation(tab, tab+k));
        printf("Case #%d: %d\n", zz, ret);
    }
    return 0;
}
