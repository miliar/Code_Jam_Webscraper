#include <cassert>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,c) for(__typeof((c).begin()) i =(c).begin();i!=(c).end();++i)
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

const int NIL = (-1);

int k,n;
const int N = 128;

char c[N][N];

int ox, oy;
inline bool checkx(int x, int y) {
    //if (ox==1&&oy==0&&x==0&&y==1) printf("yoł\n");
    int sx = 2*ox - x;
    int sy = y;
    if (sx<0||sy<0||sx>=n||sy>=n) return true;
    //printf("%d %d\n",sx,sy);
    //if (ox==1&&oy==0&&x==0&&y==1) printf("yoł\n");
    //printf("-%c-%c-\n",c[x][y],c[sx][sy]);    
    if (c[x][y]==' '||c[sx][sy]==' ') return true;
    //if (ox==1&&oy==0&&x==0&&y==1) printf("yoł\n");

    return c[x][y] == c[sx][sy];
}
inline bool checky(int x, int y) {
    
    int sx = x;
    int sy = 2*oy - y;
    if (sx<0||sy<0||sx>=n||sy>=n) return true;
    if (c[x][y]==' '||c[sx][sy]==' ') return true;
    return c[x][y] == c[sx][sy];
}

inline bool check(int x, int y) { return checkx(x,y) && checky(x,y); }

int offset(int x, int y) {
    int mx = max(x-(k-1),(k-1)-x);
    int my = max(y-(k-1),(k-1)-y);
    int m = mx  +my;
    m += k;
    return m*m - k*k;
}

void scase() {
    scanf("%d",&k);
    scanf("%c",&c[0][0]);
    n = 2*k-1;
    REP(i,n) REP(j,n) c[i][j] = ' ';
    REP(i,n) {
        int j = 0;
        while(true) {
            scanf("%c",&c[i][j]);
            if (c[i][j] == '\n') {
                c[i][j] = ' ';
                break;
            }
            j++;
        }
    }
    //printf("\n--\n");
    //REP(i,n) {
      //  REP(j,n) printf("%c",c[i][j]);
        //printf("-\n");
   // }
    int best = N*N;
    for(ox = 0; ox<n; ox++)
        for(oy = 0; oy<n; oy++) {
            bool ok = true;
            REP(i,n) REP(j,n) if (!check(i,j)) {
                ok = false;
//                printf("o = %d,%d i,j = %d,%d failed\n",ox,oy,i,j);
                i = n;  j = n;
            }
            if (ok) {
                best = min(best, offset(ox,oy));
  //              printf("%d %d is ok\n",ox,oy);
            }
            
        }
    printf("%d\n",best);
//    assert(best<3*k*k);
}

int main() {
    int j;
    scanf("%d",&j);
    for(int i=1;i<=j;i++) {
        printf("Case #%d: ",i);
        scase();
    }
    return 0;
}

