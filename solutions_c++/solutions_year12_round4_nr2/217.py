#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <stack>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
typedef long long int64;
#define REP(i,n) for(int i=0; i<(n); i++)

struct point {
    double x,y;
    point(double x=0, double y=0): x(x), y(y) {}
} res[10100];

void inc(int &x, int p) {
    if (x==0) x+=p;
    else x+=2*p;
}

struct par {
    int r,p;
} v[10100];

bool cmp(par a, par b) {
    return a.r<b.r;
}

int main() {
    int nt;

    scanf(" %d",&nt);
    for (int ct=1;ct<=nt;ct++) {
        int n,w,h;

        scanf("%d%d%d",&n,&w,&h);
        
        REP(i,n) {
            scanf("%d",&v[i].r);
            v[i].p=i;
        }

        sort(v,v+n,cmp);

        int x=-v[n-1].r,y=-v[n-1].r,mxh=0;
        for (int i=n-1;i>=0; i--) {
            if (x+v[i].r>w) {
                x=-v[i].r;
                y+=mxh;
                mxh=0;
            }

            if (mxh==0) {
                mxh=2*v[i].r;
                res[v[i].p]=point(x+v[i].r,y+v[i].r);
                x+=2*v[i].r;
                continue;
            }

            int acc=0;
            if (y+v[i].r<0) acc=-(y+v[i].r);
            int r0=v[i].r;
            
            while (i>=0 && y+acc+v[i].r<=h && acc+2*v[i].r<=mxh) {
                res[v[i].p]=point(x+v[i].r,y+v[i].r+acc);
                acc+=2*v[i].r;
                i--;
            }
            x+=2*r0;
            i++;
        }
        
        printf("Case #%d:",ct);
        REP(i,n)
            printf(" %.1lf %.1lf",res[i].x,res[i].y);
        printf("\n");
    }
    return 0;
}
