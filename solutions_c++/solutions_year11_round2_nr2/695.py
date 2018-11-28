#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

typedef long long ll;

#define MAXN 1000001

#define eps 1e-8

int D;

ll pos[MAXN];
int n;

void set_positions(int number, ll position) {
    while (number--) {
        pos[n] = position;
        ++n;
    }
}

bool try_time(double t) {
    double last_pos = (double)pos[0] - t;
    for (int i = 1; i < n; ++i) {
        double early = last_pos + (double)D;
        if ((double)pos[i] < early) {
            double dist = early - (double)pos[i];
            if (dist > t + eps) return false;
            last_pos = early;
            continue;
        }
        else {
            if ((double)pos[i] - t < early) last_pos = early;
            else last_pos = (double)pos[i] - t;
        }
    }
    return true;
}

void solve(int test) {
    int C;
    cin >> C >> D;
    n = 0;
    for (int i = 0; i < C; ++i) {
        int V;
        ll P;
        cin >> P >> V;
        set_positions(V, P);
    }
    double R = 1000000000000.0;
    double L = 0.0;
    while (R - L > 1e-9) {
        double Q = L + 0.5 * (R - L);
        if (try_time(Q)) R = Q;
        else L = Q;
    }
    cout.setf(ios::fixed);
    cout.precision(9);
    double ret = L + (R - L)*0.5;
    cout << "Case #" << test << ": " << ret << endl;
}

int main() {
    int n_tests;
    cin >> n_tests;
    for (int test = 1; test <= n_tests; ++test) {
        solve(test);
    }
    return 0;
}
