#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <vector>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
using namespace std;

#define REP(i, N) for (int i = 0; i < (int)(N); ++i)
#define FOR(i, N, M) for (int i = (int)(N); i <= (int)(M); ++i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); --i)
#define FORI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define TIP(x) (cerr << #x << " = " << (x) << endl)
#define sz size()
#define pb push_back
#define mp make_pair
#define pf first
#define ps second
#define INF 1000000000
#define ALL(x) (x).begin(), (x).end()
#define CLEAR(X) (memset(X, 0, sizeof(X)))
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

const char *file_name = "B-large.in";
//const char *file_name = "b.in";

inline double SQR(double x) {
    return x * x;
}

int main() {
    FILE *f = fopen(file_name, "rt");
    int num_tests;
    fscanf(f, "%d", &num_tests);
    REP(t, num_tests) {
        int N;
        fscanf(f, "%d", &N);
        double ax, ay, az, bx, by, bz;
        ax = ay = az = bx = by = bz = 0;
        REP(i, N) {
            int x, y, z, vx, vy, vz;
            fscanf(f, "%d %d %d %d %d %d", &x, &y, &z, &vx, &vy, &vz);
            ax += x; ay += y; az += z;
            bx += vx; by += vy; bz += vz;
        }
        fprintf(stderr, "%lf %lf %lf\n", ax, ay, az);
        fprintf(stderr, "%lf %lf %lf\n", bx, by, bz);

        double a = (SQR(bx) + SQR(by) + SQR(bz));
        double b = (2 * (ax * bx + ay * by + az * bz));
        double c = (SQR(ax) + SQR(ay) + SQR(az));
        double tmin = -1;
        if (a) {
            tmin = -b / (2. * a);
        } else if (b) {
            tmin = -c / b;
        } else {
            tmin = 0;
        }
        if (tmin < 0) tmin = 0;
        double dst = sqrt(fabs(a * SQR(tmin) + b * tmin + c)) / (double) N;
        fprintf(stderr, "%lf %lf %lf %lf\n", a, b, c, tmin);
        printf("Case #%d: %.8lf %.8lf\n", t + 1, dst, tmin);
    }
    fclose(f);
    return 0;
}

