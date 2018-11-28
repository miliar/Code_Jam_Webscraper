
#include <algorithm>
#include <iostream>
#include <string>
#define MAXN 1000000

using namespace std;

int C, D;

int N;
double a[MAXN];

bool check(double L) {
    double cur = a[0] - L;
    for(int i = 1; i < N; i++) {
        double next = a[i] + L;
        if(next < cur + D)
            return false;

        if(next > cur + D)
            next = cur + D;
        if(next < a[i] - L)
            next = a[i] - L;

        cur = next;
    }
    return true;
}

double solve() {
    double low = 0.0, high = 1e12;
    for(int i = 0; i < 200; i++) {
        double mid = 0.5 * (low + high);
        if(check(mid))
            high = mid;
        else
            low = mid;
    }
    return low;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        N = 0;
        cin >> C >> D;
        int P, V;
        for(int i = 0; i < C; i++) {
            cin >> P >> V;
            for(int j = 0; j < V; j++)
                a[N++] = P;
        }
        sort(a, a + N);

        printf("Case #%d: %.2lf\n", t, solve());
    }
}
