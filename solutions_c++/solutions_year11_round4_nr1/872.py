#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

#define LMAX 2000000

int L, S, R, n;
double t;
int su[LMAX];

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int numTests;
    cin >> numTests;
    for (int nt = 1; nt <= numTests; ++nt) {
        cin >> L >> S >> R >> t >> n;

        for (int x = 0; x <= L; ++x) {
            su[x] = S;
        }
        for (int i = 0; i < n; ++i) {
            int a, b, w;
            cin >> a >> b >> w;
            for (int x = a; x < b; ++x) {
                su[x] += w;
            }
        }

        int delta = max(R-S, 0);

        sort(&su[0], &su[L]);
        double tot = 0;
        for (int i = 0; i < L; ++i) {
            if (t > 0) {
                double ct = 1.0 / (su[i] + delta);
                if (ct <= t) {
                    t -= ct;
                    tot += ct;
                } else {
                    double h = t / ct;
                    tot += t;
                    tot += (1.0 - h) / su[i];
                    t = 0;
                }
            } else {
                tot += 1.0 / su[i];
            }
        }


        cout << "Case #" << nt << ": ";
        printf("%.9lf\n", tot);
    }
    
    return 0;
}