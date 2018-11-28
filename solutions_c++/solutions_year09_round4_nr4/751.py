#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

typedef struct {
    double x, y, r;
} circ;

int T, n;
double mini;

bool comb[20];
circ v[20];

double dist(double x1,double y1, double x2,double y2) {
    return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

double analex(bool tt) {
    circ c;
    c.r = 0.0;
    bool prim=true;
    for (int i=0;i<n;i++) {
        if (comb[i] == tt and prim) {
           c = v[i];
           prim = false;
           continue;
        }
        if (comb[i] == tt) {
            c.r = (dist(c.x,c.y,v[i].x,v[i].y)+c.r+v[i].r)/2.0;
            c.x = (c.x + v[i].x)/2.0;
            c.y = (c.y + v[i].y)/2.0;
        }
    }
   return c.r;
}

void combina(int i) {
    if (i == n) {
        double t1 = analex(true);
        double t2 = analex(false);
//        printf("analex true = %lf, false = %lf\n",t1,t2);
        mini = min(mini,max(t1,t2));
        return;
    }
    comb[i] = true;
    combina(i+1);
    comb[i] = false;
    combina(i+1);
}

int main() {

    int C = 1;

    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        for (int i=0;i<n;i++) {
            double x, y, r;
            scanf("%lf %lf %lf",&x, &y, &r);
            circ c;
            c.x = x; c.y = y; c.r = r;
            v[i] = c;
        }
        mini=9000000000.0;
        combina(0);
        printf("Case #%d: %.6lf\n",C++,mini);
    }

    return 0;
}
