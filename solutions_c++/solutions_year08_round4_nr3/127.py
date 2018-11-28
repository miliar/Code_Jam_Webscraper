#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <deque>
#include <cmath>
#define DEBUG(x) std::cerr << #x << " = " << x << '\n';
typedef long long int64;

struct Ship {
    double x, y, z, p;
} ships[1000];
int T, N;

inline double pow_needed(double x, double y, double z) {
    double pow = 0;
    for (int i=0; i<N; i++)
        pow = std::max(pow, (fabs(ships[i].x-x) + fabs(ships[i].y-y) + fabs(ships[i].z-z)) / ships[i].p);
    return pow;
}
double search(double area) {
    const int div = 10;
    double sx=0, sy=0, sz=0, pow=0;
    for (double r=area; r>1e-6; r/=div) {
        pow = 1e10;
        double step = r/div, bx=0, by=0, bz=0;
        for (double x=sx-r; x<=sx+r; x+=step)
        for (double y=sy-r; y<=sy+r; y+=step)
        for (double z=sz-r; z<=sz+r; z+=step) {
            double pn = pow_needed(x,y,z);
            if (pn >= pow) continue;
            pow = pn;
            bx = x; by = y; bz = z;
        }
        sx = bx; sy = by; sz = bz;
    }
    return pow;
}

int main() {
    std::cin >> T;
    for (int t=1; t<=T; t++) {
        std::cin >> N;
        double maxc = 0;
        for (int i=0; i<N; i++) {
            std::cin >> ships[i].x >> ships[i].y >> ships[i].z >> ships[i].p;
            maxc = std::max(maxc, ships[i].x);
            maxc = std::max(maxc, ships[i].y);
            maxc = std::max(maxc, ships[i].z);
        }

        printf("Case #%d: %.6f\n", t, search(maxc));
    }
}
