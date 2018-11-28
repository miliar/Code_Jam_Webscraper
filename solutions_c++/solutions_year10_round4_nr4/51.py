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


double alpha(double r, double R, double l) {
    double c = R*R-r*r-l*l;
    c = c/(r*l*2.0);
    return 2*acos(-c);
}

double area(double r, double a) {
    return r*r*(a-sin(a))*0.5;
}

double area2(double r1, double r2, double l) {
//  printf("a2 %lf %lf %lf\n",r1,r2,l);
    double a1,a2;
    a1 = alpha(r1,r2,l);
    a2 = alpha(r2,r1,l);
//  printf("a = %lf %lf\n",a1,a2);
    return area(r1,a1) + area(r2,a2);
}


double pit(double x, double y) { return sqrt(x*x+y*y); }

double dist(double x1, double y1, double x2, double y2) {
    return pit(x1-x2,y1-y2);
}

void scase() {
    int n,m;
    scanf("%d%d",&n,&m);
    double x1,x2,y1,y2,x[100],y[100];
    scanf("%lf%lf",&x1,&y1);
    scanf("%lf%lf",&x2,&y2);
    REP(i,m)
       scanf("%lf%lf",&x[i],&y[i]);
    REP(i,m) {
        double r1 = dist(x1,y1,x[i],y[i]);
        double r2 = dist(x2,y2,x[i],y[i]);
        double l = dist(x1,y1,x2,y2);
        printf(" %.7lf",area2(r1,r2,l));
    }
    printf("\n");

}

int main() {
    int j;
    scanf("%d",&j);
    for(int i=1;i<=j;i++) {
        printf("Case #%d:",i);
        scase();
    }
    return 0;
}

