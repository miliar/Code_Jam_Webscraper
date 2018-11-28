#include <stdio.h>
#include <string.h>

#define FOR(i,n) for((i)=0;(i)<(n);(i)++)
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define _FORIT(it, b, e) for (__typeof(b) it = (b); it != (e); it++)
#define FORIT(x...) _FORIT(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define CLR(a,v) memset((a),(v),sizeof(a)) 
#define TLE while(1);
#define RTE printf("%d", 1/0);

#define INF 0x3F3F3F3F

int n, m;
int h[110][110];
char label[110][110], cur;

int get_int() {
    int ch, i;
    while (((ch = getchar()) == ' ') || (ch == '\n'));
    for (i = 0; ch >= '0' && ch <= '9'; ch = getchar() ) i = (i<<3)+(i<<1)+(ch-'0');
    return i;
}

char dfs(int y, int x) {
    if (label[y][x]) return label[y][x];
    int vx, vy, k = h[y][x];
    if (y-1>=0 && h[y-1][x]<k) vx = x, vy = y-1, k = h[y-1][x];
    if (x-1>=0 && h[y][x-1]<k) vx = x-1, vy = y, k = h[y][x-1];
    if (x+1<m && h[y][x+1]<k) vx = x+1, vy = y, k = h[y][x+1];
    if (y+1<n && h[y+1][x]<k) vx = x, vy = y+1, k = h[y+1][x];
    if (k==h[y][x]) { label[y][x] = cur++; return label[y][x]; }
    return (label[y][x] = dfs(vy, vx)); 
}


int main() {
    
    int i, j, t, c;
    
    for (t = get_int(), c = 1; c <= t; c++) {
        printf("Case #%d:\n", c);
        n = get_int(); m = get_int();
        FOR(i, n) FOR(j, m) h[i][j] = get_int(), label[i][j] = 0;
        cur = 'a';
        FOR(i, n) FOR(j, m) if (!label[i][j]) dfs(i, j);
        FOR(i, n) FOR(j, m) (j==m-1) ? printf("%c\n", label[i][j]) : printf("%c ", label[i][j]);
    }
    
    return 0;
}
