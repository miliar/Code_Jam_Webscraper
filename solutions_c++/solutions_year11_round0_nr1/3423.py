#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))
int n, dat[128][2];
int cach[128][128][128];
int doit(int x, int y, int i) {
    if(y<=0 || x<=0) return 1048576;
    if(y>100 || x>100) return 1048576;
    if(i == n) return 0;
    int& ret = cach[x][y][i];
    if(ret != -1) return ret;
    ret = 1048576;
    int v;
    if(dat[i][0] == 0 && x == dat[i][1]) {
        FOR(py,-1,2) {
            v = doit(x, y+py, i+1)+1; 
            ret=min(ret, v);
        }
    }
    else if(dat[i][0] == 1 && y == dat[i][1]) {
        FOR(px,-1,2) {
            v = doit(x+px, y, i+1)+1; 
            ret=min(ret, v);
        }
    }
    else {
        FOR(px,-1,2)
            FOR(py,-1,2) {
                v = doit(x + px, y + py, i)+1;
                ret=min(ret, v);
            }
    }
    return ret;
}
int main() {
    int e = 0, T;
    scanf("%d",&T);
    while(T--) {
        int ans = 0;
        scanf("%d",&n);
        FOR(i,0,n) {
            char per; int pos;
            scanf(" %c %d",&per,&pos);
            if(per == 'B') dat[i][0] = 0, dat[i][1] = pos;
            else           dat[i][0] = 1, dat[i][1] = pos;
        }
        SET(cach, -1);
        ans = doit(1, 1, 0);
        printf("Case #%d: %d\n", ++e, ans);
    }
    return 0;
}
