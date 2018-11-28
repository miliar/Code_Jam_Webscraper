#include <algorithm>
#include <vector>
#include <sstream>
#include <set>
#include <iostream>
#include <map>
#include <iomanip>
#include <fstream>
#include <locale>
#include <cmath>
#include <queue>
using namespace std;

struct poly {
    poly(int x, int y, int w, int l): x(x), y(y), w(w), l(l) {}
    int x;
    int y;
    int w;
    int l;
};

int main() {
#ifndef ONLINE_JUDGE
    ifstream cin("B-small-attempt3.in");
#endif
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t+1 << ": ";
        int N,W,L;
        cin >> N >> W >> L;
        vector<long long> r(N);
        for (int i = 0; i < N; i++) {
            cin >> r[i];
        }
        vector<long long> x(N), y(N);
        for (int i = 1; i < N; i++) {
            bool found = false;
            long long cx = 0, cy = 0;
            while (!found) {
                cx = rand() % (W+1);
                cy = rand() % (L+1);
                found = true;
                for (int j = 0; j < i; j++) {
                    if ((cx-x[j])*(cx-x[j]) + (cy-y[j])*(cy-y[j]) < (r[i]+r[j])*(r[i]+r[j])) {
                        found = false;
                        break;
                    }
                }
            }
            x[i] = cx;
            y[i] = cy;
        }
        for (int i = 0; i < N; i++)
            cout << x[i] << " " << y[i] << " ";
        cout << endl;
    }
}
