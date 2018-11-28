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

const char *file_name = "D-small-attempt0.in";

int x[16], y[16], r[16];

double dst(int a, int b) {
    return sqrt((x[a] - x[b]) * (x[a] - x[b]) + (y[a] - y[b]) * (y[a] - y[b]));
}

int main() {
    FILE *f = fopen(file_name, "rt");
    int num_tests;
    fscanf(f, "%d", &num_tests);
    int N;
    REP(t, num_tests) {
        fscanf(f, "%d", &N);
        REP(i, N) {
            fscanf(f, "%d %d %d", x + i, y + i, r + i);
        }
        double sol = 1e100;
        if (N == 1) {
            sol = r[0];
        } else if (N == 2) {
            sol = max(r[0], r[1]);
        } else {
            sol = min(sol, max(double(r[0]), (dst(1, 2) + r[1] + r[2]) * 0.5));
            sol = min(sol, max(double(r[1]), (dst(0, 2) + r[0] + r[2]) * 0.5));
            sol = min(sol, max(double(r[2]), (dst(1, 0) + r[1] + r[0]) * 0.5));
        }
        printf("Case #%d: %.6lf\n", t + 1, sol);
    }
    fclose(f);
    return 0;
}

