#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct node {
    int b,e,w;
    node(int _b,int _e,int _w)
    : b(_b),e(_e),w(_w) {}
    node() {}
};

const int MAXN = 1000+5;

node L[MAXN*2];
int b[MAXN],e[MAXN],w[MAXN];
int S,R,N,X;
double t;

bool cmp(const node &a,const node &b) {
    return a.w<b.w;
}

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int ntest;
    scanf("%d",&ntest);
    for (int run = 1; run<=ntest; run++) {
        printf("Case #%d: ",run);
        scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
        int prev = 0;
        for (int i = 0; i<N; i++) {
            scanf("%d%d%d",&b[i],&e[i],&w[i]);
            L[2*i] = node(prev,b[i],0);
            L[2*i+1] = node(b[i],e[i],w[i]);
            prev = e[i];
        }
        L[2*N] = node(prev,X,0);
        sort(L,L+2*N+1,cmp);
        double ans = 0;
        for (int i = 0; i<2*N+1; i++) {
            double len = L[i].e-L[i].b,vec =L[i].w;
            if (t>0) {
                double _t = len/(vec+R);
                if (t>=_t) {
                    t -= _t;
                    ans += _t;
                }
                else {
                    ans += t;
                    len -= t*(vec+R);
                    t = 0;
                    ans += len/(vec+S);
                }
            }
            else ans += len/(vec+S);
        }
        printf("%.8f\n",ans);
    }
    return 0;
}
