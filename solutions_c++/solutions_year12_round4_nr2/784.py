#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>

#define EPS 1e-9

#define LIM 1000

using namespace std;


typedef pair<int,int> ii;
int n, X, Y, T,C=1, r[1024];
double x[1024], y[1024];
ii v[1024];

inline int cmpf(double a, double b) {
    if (fabs(a-b) < EPS) return 0;
    return a < b ? -1 : 1;
}

inline double dist(double x1, double y1, double x2, double y2) {
    return sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) );
}

bool vai(int u) {
    if (u==n) return true;
    double dx = (double)X/(double)LIM;
    double dy = (double)Y/(double)LIM;
    for (int i=0;i<LIM;i++)
        for (int j=0;j<LIM;j++) {
            bool blz = true;
            double xx = i*dx;
            double yy = j*dy;
            for (int k=0;k<u;k++)
                if (cmpf(dist(xx,yy,x[v[k].second],y[v[k].second]),v[u].first+v[k].first)<0) {
                    blz=false;
                    break;
                }
            if (blz) {
                x[v[u].second] = xx;
                y[v[u].second] = yy;
                if (vai(u+1)) return true;
            }
        }
    return false;
}

int main() {

    for(scanf("%d",&T);T--;) {
        scanf("%d %d %d",&n,&X,&Y);
        for (int i=0;i<n;i++) {
            int R;
            scanf("%d",&R);
            v[i] = ii(R,i);
            r[i] = R;
        }
        sort(v,v+n);
        vai(0);
        printf("Case #%d:",C++);
        for (int i=0;i<n;i++)
            printf(" %.6lf %.6lf",x[i],y[i]);
        printf("\n");

        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++) if (i!=j) {
                if (cmpf(dist(x[i],y[i],x[j],y[j]), r[i]+r[j])<0) {
                    printf("PAU\n");
                    while(1);
                }
            }

    }

    return 0;
}
