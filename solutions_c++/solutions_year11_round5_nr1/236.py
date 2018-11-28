#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

typedef double TYPE;

struct pt {
    TYPE x, y;
    pt(TYPE x = 0, TYPE y = 0) : x(x), y(y) { }
    TYPE operator%(pt p) { return x*p.y - y*p.x; }
};

inline int g_mod(int i, int n) { if(i == n) return 0; return i; }
double p_signedarea(vector<pt>& pol) {
    double ret = 0;
    for(unsigned int i = 0; i < pol.size(); ++i)
        ret += pol[i] % pol[g_mod(i+1, pol.size())];
    return ret/2;
}

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        printf("Case #%d:\n", z);

        int W, L, U, G;
        scanf("%d %d %d %d", &W, &L, &U, &G);

        vector<pt> poly[2];
        vector<int> xs;
        for(int w = 0; w < 2; w++) {
            for(int i = 0; i < (w == 0 ? L : U); i++) {
                int x, y;
                scanf("%d %d", &x, &y);
                poly[w].push_back(pt(x, y));
                xs.push_back(x);
            }
        }

        vector<pt> merged;
        merged.push_back(pt(0, 0));
        int pa = 0, pb = 0;
        while(pa < (int)poly[0].size() && pb < (int)poly[1].size()) {
            if(poly[0][pa].x == poly[1][pb].x) {
                merged.push_back(pt(poly[0][pa].x, poly[1][pb].y - poly[0][pa].y));
                pa++; pb++;
            } else if(poly[0][pa].x < poly[1][pb].x) {
                double new_y =
                    (poly[1][pb].y - poly[1][pb-1].y)/(poly[1][pb].x - poly[1][pb-1].x)
                    * (poly[0][pa].x - poly[1][pb-1].x) + poly[1][pb-1].y;
                merged.push_back(pt(poly[0][pa].x, new_y - poly[0][pa].y));
                pa++;
            } else {
                double new_y =
                    (poly[0][pa].y - poly[0][pa-1].y)/(poly[0][pa].x - poly[0][pa-1].x)
                    * (poly[1][pb].x - poly[0][pa-1].x) + poly[0][pa-1].y;
                merged.push_back(pt(poly[1][pb].x, poly[1][pb].y - new_y));
                pb++;
            }
        }
        merged.push_back(pt(W, 0));
        double per_cut = abs(p_signedarea(merged))/G;

        int pc = 1;
        double prev = 0;

        for(int i = 1; i < G; i++) {
            double left = per_cut;
            while(true) {
                double area = (merged[pc].y + merged[pc-1].y)
                    * (merged[pc].x - merged[pc-1].x)/2;
                if(area - prev + 1e-9 < left) {
                    left -= area - prev;
                    prev = 0;
                    pc++;
                } else {
                    double lo = 0, hi = 1, narea;
                    double diff = merged[pc].y - merged[pc-1].y;

                    for(int z = 0; z < 50; z++) {
                        double mid = (lo+hi)/2;
                        narea = (2*merged[pc-1].y + mid*diff)
                            * mid * (merged[pc].x - merged[pc-1].x)/2 - prev;
                        if(narea > left)
                            hi = mid;
                        else
                            lo = mid;
                    }

                    prev += narea;
                    printf("%.9lf\n", lo * (merged[pc].x - merged[pc-1].x)
                           + merged[pc-1].x);

                    break;
                }
            }
        }
    }
}
