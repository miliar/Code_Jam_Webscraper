/* Problema:
 * Fonte:
 * Palavra-chave: */

#include <set>
#include <map>
#include <list>
#include <queue>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <functional>

#define rep(i, N) for(int i=0;i<(N);++i)
#define repd(i, N) for(int i=(N)-1;i>=0;--i)
#define rep3(i, j, N) for(int i=(j);i<(N);++i)
#define repd3(i, j, N) for(int i=(N)-1;i>=(j);--i)

#define two(x) (1ll<<(x))

using namespace std;


typedef long long ll;

int T, N;

int X[50], Y[50], R[50];

bool intersect(int i, int j, double r, double &x3, double& y3, double& x4, double& y4 ) {
    ll x0 = X[i] - X[j];
    ll y0 = Y[i] - Y[j];

    double r0 = r - R[i];
    double r1 = r - R[j];

    if(r0 <0 or r1<0) return false;

    double a = -2*x0;
    double b = -2*y0;
    double c = r1*r1-r0*r0+x0*x0+y0*y0;

    if(x0 != 0) {

        double A = b*b + a*a;
        double B = 2*b*c;
        double C = c*c -a*a*r1*r1;

        double delta = B*B - 4*A*C;
        if(delta < 0) return false;

        delta = sqrt(delta);

        y3 = (-B + delta)/(2*A);
        x3 = (-b*y3-c)/a;

        y4 = (-B + delta)/(2*A);
        x4 = (-b*y4-c)/a;

    } else {
        y3 = y4 = -c/b;
        double delta = r1*r1-y3*y3;
        if(delta < 0) return false;
        delta = sqrt(delta);
        x3 = delta;
        x4 = - delta;


    }
    x3 += X[j];
    y3 += Y[j];
    x4 += X[j];
    y4 += Y[j];
    return true;
}

double Q(double x) { return x*x; }

bool cobre(int i, int j, double r, ll& m1, ll& m2) {
    double x0, y0, x1, y1;
    if(not intersect(i, j, r, x0, y0, x1, y1)) return false;
    m1 = m2 = two(i) | two(j);

    for(int k=0;k<N;++k) {
        double d1 = sqrt(Q(x0-X[k]) + Q(y0-Y[k]));
        double d2 = sqrt(Q(x1-X[k]) + Q(y1-Y[k]));
        if(d1+R[k] <= r) {
            m1 |= two(k);
        }
        if(d2+R[k] <= r) {
            m2 |= two(k);
        }

    }
    return true;
}

ll masks[50*50*2];
int K;

int main(void) {

    scanf("%d", &T);

    for(int t=0;t<T;++t) {
        scanf("%d", &N);

        rep(i, N) scanf("%d%d%d", X+i, Y+i, R+i);

        double inicio = 0, fim = 2000;
        for(int r=0;r<100;++r) {
            double meio = (inicio + fim) / 2.0;
            K = 0;
            for(int i=0;i<N;++i) for(int j=i+1;j<N;++j) {
                ll m1, m2;
                if(cobre(i, j, meio, m1, m2)) {
                    masks[K++] = m1;
                    masks[K++] = m2;
                }
            }
            for(int i=0;i<N;++i) {
                if(meio >= R[i]) {
                    masks[K++] = two(i);
                }
            }
            bool certo = false;
            ll todos = two(N)-1;
            for(int i=0;i<K;++i) for(int j=i;j<K;++j) {
                if((masks[i] | masks[j]) == todos) {
                    certo = true;
                    break;
                }
            }
            if(certo) {
                fim = meio;
            } else {
                inicio = meio;
            }
        }

        double resp = (inicio + fim) / 2;
        printf("Case #%d: %.8f\n", t+1, resp);


    }
    return 0;
}
