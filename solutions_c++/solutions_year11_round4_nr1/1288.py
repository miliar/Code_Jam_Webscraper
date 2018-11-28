#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;


pair<double, double> tab[10000];


int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        double X0, X, S, R, tR, tT;
        int N;
        scanf("%lf%lf%lf%lf%d", &X, &S, &R, &tR, &N);
        tT=0;
        X0=0;
        R-=S;
        for (int i=0; i<N; i++) {
            double b, e, w;
            scanf("%lf%lf%lf", &b, &e, &w);
            tab[i].first=w+S;
            tab[i].second=e-b;
            X-=tab[i].second;
        }
        tab[N].first=S;
        tab[N].second=X;
        sort(tab, tab+N+1);
        for (int i=0; i<=N; i++) {
            double t0=min(tab[i].second/(tab[i].first+R), tR);
            tR-=t0;
            tT+=t0+(tab[i].second-(tab[i].first+R)*t0)/tab[i].first;
        }
        
               
        
        printf("Case #%d: %.9lf\n", t, tT);
    }
    return 0;
}

