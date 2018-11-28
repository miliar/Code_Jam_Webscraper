#include <iostream>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

const int NN = 1100;
double eps = 1e-8;
struct node{
    double x, y;
}ret[NN];
int n, d;
int p[NN], r[NN];

bool cmp(const node &p, const node &q) {
    if (p.x < q.x) return true;
    if (fabs(p.x - q.x) < eps && p.y < q.y) return true;
    return false;
}

bool ok(double m){
    //printf("m = %lf\n",m); 
	  int tot = 0;
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < r[i]; ++j) {
            ret[tot].x = p[i] - 1.0 * m;
            ret[tot].y = p[i] + 1.0 * m;
            tot++;
        }
    }
    sort(ret + 0, ret + n, cmp);
    
    double start = ret[0].x;
    //printf("%lf\n",start);
    for (int j = 1; j < tot; ++j) {
        double next = start + d;
        //printf("ret x = %lf y = %lf\n",ret[j].x, ret[j].y);
        if (next + eps < ret[j].x) {
           start = ret[j].x;
           //printf("adopt 1\n");
        } else if (next + eps > ret[j].x && next - eps < ret[j].y) {
           start = next;
           //printf("adopt 2\n");
        } else return false;
        //printf("%lf\n",start);
    }
    return true;
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int pp = 1; pp <= t; ++pp) {
        printf("Case #%d: ",pp);
        scanf("%d%d",&n, &d);
        for (int j = 0; j < n; ++j) {
            scanf("%d%d",&p[j], &r[j]);
        }
       	double l = 0;
	      double r = 1e10;
        for (int i = 0; i < 500; ++i){
        	     double m = (l + r) / 2.0;
               if (ok(m)) r = m;
               else l = m;
       	}    
       	printf("%0.13lf\n",(l + r) / 2.0);
    }
    return 0;
}
