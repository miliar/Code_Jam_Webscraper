#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

#define min(a, b) (a < b ? a : b)
#define EPS 1e-8
#define ll long long int

using namespace std;

typedef pair<int, int> ii;
typedef pair<int , ii> i3;

int X, R, S, t, T, n, w, C=1,Tt;
vector<i3> v;

int cmpf(double a, double b) {
    if (fabs(a-b) < EPS) return 0.0;
    return a < b ? -1 : 1;
}

int main() {

    for(scanf("%d",&T);T--;) {
        scanf("%d %d %d %d %d",&X,&S,&R,&Tt,&n);
        v.clear();
        int sem = X;
        for (int i=0;i<n;i++) {
            int ini, fim;
            scanf("%d %d %d",&ini,&fim,&w);
            v.push_back(i3(w,ii(ini,fim)));
            sem -= (fim-ini);
        }
        sort(v.begin(),v.end());

        double tot = 0;
        double t = Tt;
        bool correndo;
        //corre fora da esteira
        double corre = (double)sem/(double)R;
        if (sem < (ll)R*(ll)Tt) {
            t -= corre;
            tot += corre;
            correndo=true;
        } else {
            double Y = R*t;
            double tt1 = (double)Y/(double)R;
            double tt2 = (double)(sem-Y)/(double)S;
            tot += tt1+tt2;
            correndo = false;
            t = 0.0;
        }

        for (int i=0;i<n;i++) {
            int ini = v[i].second.first;
            int fim = v[i].second.second;
            int w = v[i].first;
            //anda na estera com vel V+w
            double tt = (double)(fim-ini)/(double)(w + (correndo?R:S));
            if (correndo and cmpf(tt,t) < 0) {
                t -= tt;
                tot += tt;
            } else if (correndo) {
                double Y = (R+w)*t;
                double tt1 = (double)Y/(double)(w + R);
                double tt2 = (double)((fim-ini)-Y)/(double)(w + S);
                tot += tt1+tt2;
                t = 0.0;
                correndo=false;
            } else {
                tot += tt;
            }

        }
        printf("Case #%d: %.9lf\n",C++,tot);


    }

    return 0;
}
