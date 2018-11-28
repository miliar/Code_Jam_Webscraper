#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vi vector<int>
#define pb push_back
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

struct firefly {
    firefly(double x0, double y0, double z0, double vx, double vy, double vz) : x0(x0), y0(y0), z0(z0), vx(vx), vy(vy), vz(vz) {}
    double x0, y0, z0;
    double vx, vy, vz;
};

struct point {
    point(double x, double y, double z) : x(x), y(y), z(z) {}
    double x, y, z;
};

int n;
vector<firefly *> fires;

point * pos(firefly * f, double t)
{
    return new point(f->x0 + (t*f->vx), f->y0 + (t*f->vy), f->z0 + (t*f->vz));
}

point * masscenter(double t)
{
    double x = 0, y = 0, z = 0;
    FOR(i, 0, SZ(fires)){
        point * tmp = pos(fires[i], t);
        x += (tmp->x/(double)n);
        y += (tmp->y/(double)n);
        z += (tmp->z/(double)n);
    }
    return new point(x, y, z);
}

double dist(point * p){
    return (sqrt(p->x*p->x + p->y*p->y + p->z*p->z));
}

double distc(double t)
{
    return dist(masscenter(t));    
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(test, 0, t){
        scanf("%d", &n);
        fires.clear();
        FOR(i, 0, n){
            double a, b, c, d, e, f;
            scanf("%lf %lf %lf %lf %lf %lf", &a, &b, &c, &d, &e, &f);
            fires.push_back(new firefly(a, b, c, d, e, f));
        }

        //FOR(i, 0, 1000){
            //point * massc0 = masscenter(1799.999990);
            //printf("t = 1799.999990 %lf %lf %lf dist %lf\n", massc0->x, massc0->y, massc0->z, dist(massc0));
        //}

        double left = 0.0, right = 1e9;
        double mid = (left + right)/2.0;
        point * l = masscenter(left), * r = masscenter(right), * m = masscenter(mid);
        if( fabs(dist(l) - dist(m)) < 1e-2 && fabs(dist(l) - dist(r)) < 1e-2){
            printf("Case #%d: %lf %lf\n", test + 1, distc(0.0), 0.0);
            continue;
        }

        FOR(i, 0, 500){
            double leftt = (2*left + right)/3.0;
            double rightt = (left + 2*right)/3.0;
            //printf("l %lf r %lf lt %lf rt %lf d(lt) %lf d(rt) %lf\n",
            //        left, right, leftt, rightt, distc(leftt), distc(rightt));
            if(distc(rightt) > distc(leftt)){
                right = rightt;
            } else {
                left = leftt;
            }
        }
        printf("Case #%d: %lf %lf\n", test + 1, distc((left + right)/2.0), (left + right)/2.0);
    }

    return 0;
}

