#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <functional>
#include <algorithm>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
//ifstream fin("large.in");
//ofstream fout("large.out");

int n, w, h;
vector< pair<int, int> > r;
greater< pair<int, int> > gt;
vector<int> x, y;

void solve(int I) {
    x.resize(0);
    y.resize(0);
    r.resize(0);
    fin >> n >> w >> h;
    r.resize(n);
    for (int i = 0; i < n; ++i) {
        fin >> r[i].first;
        r[i].second = i;
    }
    sort(r.begin(), r.end(), gt);
    x.resize(n);
    y.resize(n);
    int base = -r[0].first, nbase = r[0].first;
    x[0] = y[0] = 0;
    for (int i = 1; i < n; ++i) {
        int ri = x[i-1] + r[i-1].first;
        if (ri + r[i].first <= w) {
            x[i] = ri + r[i].first;
            y[i] = max(0, base + r[i].first);
        } else {
            base = nbase;
            nbase += 2*r[i].first;
            x[i] = 0;
            y[i] = max(0, base + r[i].first);
        }
    }
    fout << "Case #" << I << ": ";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (r[j].second == i) {
                fout << x[j] << ' ' << y[j] << ' ';
                break;
            }
        }
    }
    fout << endl;
}

int t;

int main() {
    fin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }

    return 0;
}
