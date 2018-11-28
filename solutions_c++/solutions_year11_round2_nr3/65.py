#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))

int n, m;
int st[16], end[16];
int gr[16][16], ng[16], g;

int max_c;
int color[16];
int bit_cnt[1024];
int sav[16];
void dfs(int x, int c) {
    color[x] = c;
    if(x == n-1) {
        int used = 0;
        FOR(i,0,n) used |= (1<<color[i]);
        if(bit_cnt[used+1] != 1) return;
        if(max_c >= bit_cnt[used]) return;
        //used = bit_cnt[used];
        FOR(i,0,g) {
            int now = 0;
            FOR(j,0,ng[i]) 
                now |= (1<<color[gr[i][j]]);
            if(now != used) return;
        }
        max_c = bit_cnt[used];
        FOR(i,0,n) sav[i] = color[i]+1;
        return;
    }
    FOR(i,0,5)
        dfs(x+1,i);
}
void doit() {
    max_c = 1;
    // colors: 0~4 (five colors at max)
    FOR(c,0,5) {
        dfs(0, c);
    }
}
int main() {
    SET(bit_cnt,0);
    FOR(i,0,1024) {
        FOR(j,0,10) if(i&(1<<j)) bit_cnt[i]++;
    }
    int e = 0, T;
    scanf("%d",&T);
    while(T--) {
        scanf("%d %d",&n,&m);
        FOR(i,0,m){ scanf("%d",&st[i]);st[i]--;}
        FOR(i,0,m){ scanf("%d",&end[i]);end[i]--;}
        g = 0; SET(ng, 0);
        FOR(i,0,n)
            gr[g][ng[g]++] = i;
        g++;
        FOR(i,0,m) {
            int x = st[i], y = end[i];
            FOR(j,0,g) {
                int cnt = 0, ix, iy;
                FOR(k,0,ng[j]) {
                    if(gr[j][k] == x) cnt++, ix = k;
                    if(gr[j][k] == y) cnt++, iy = k;
                }
                if(cnt == 2) {
                    // break group gr[g][] into two pieces
                    ng[g] = 0;
                    FOR(k,min(ix,iy),max(ix,iy)+1) 
                        gr[g][ng[g]++] = gr[j][k];
                    g++;
                    int tmp[16], nt = 0;
                    FOR(k,0,ng[j]) {
                        tmp[nt++] = gr[j][k];
                        if(k == min(ix, iy))
                            k = max(ix, iy) - 1;
                    }
                    ng[j] = nt;
                    FOR(k,0,nt) gr[j][k] = tmp[k];
                    break;
                }
            }
        }
        /*
        printf("groups = %d\n", g);
        FOR(i,0,g) {
            FOR(j,0,ng[i])
                printf("%d ",gr[i][j]);
            printf("\n");
        }
        */
        doit();
        printf("Case #%d: %d\n", ++e, max_c);
        FOR(i,0,n) printf("%d ",sav[i]);
        printf("\n");
    }
    return 0;
}
