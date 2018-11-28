#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

struct T {
    double begin, end, speed;
    T() {}
    T(double a, double b, double c): begin(a), end(b), speed(c) {};
    bool operator<(const T& other) const {
        return speed < other.speed;
    }
};

double solve() {
    double len, walk, run, runtime;
    int n;
    scanf("%lf %lf %lf %lf %d", &len, &walk, &run, &runtime, &n);
    double result = 0;
    double walklen = len;
    vector<T> v;

    for (int i = 0; i < n; i++) {
        double begin, end, speed;
        scanf("%lf %lf %lf", &begin, &end, &speed);
        v.push_back(T(begin, end, speed));
        walklen -= end-begin;
    }

    double time = walklen/run;
    if (time > runtime) {
        result += runtime;
        walklen -= runtime*run;
        runtime = 0;
        result += walklen/walk;
        walklen = 0;
    } else {
        runtime -= time;
        result += time;
        walklen = 0;
    }

    sort(v.begin(), v.end());
    for (int i = 0; i < n; i++) {
        double len = v[i].end-v[i].begin;
        double s = v[i].speed;

        if (len/(s+run) < runtime) {
            runtime -= len/(s+run);
            result += len/(s+run);
        } else {
            len -= runtime*(s+run);
            result += runtime;
            runtime = 0;
            result += len/(s+walk);
        }
    }

    return result;
}

int main() {
    int T;
    scanf ("%d\n", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: %lf\n", i, solve());
    }

    return 0;
}
