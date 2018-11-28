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

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
//ifstream fin("large.in");
//ofstream fout("large.out");

int n, v[3000];
long long h[3000];

bool in(int a, int b, int c) {
    if (c > a && c < b) return 1;
    return 0;
}

bool out(int a, int b, int c) {
    if (c < a || c > b) return 1;
    return 0;
}

void rec(vector<int> &g) {
    if (g.size() <= 2) return;
    long long a = g[0];
    long long b = g[g.size() - 2];
    long long c = g[g.size() - 1];
    h[b] = (int)ceil((.0 + (c-a)*h[c] - (c - b)*(h[c] - h[a]))/(c - a));
    g.pop_back();
    rec(g);
}

void solve(int I) {
    //cout << I << endl;
    fin >> n;
    //cout << n << endl;
    for (int i = 0; i < n - 1; ++i) {
        fin >> v[i];
        --v[i];
        h[i] = 0;
    }
    h[n-1] = 1000000;
    vector<int> g;
    for (int i = 1; i < n - 1; ++i) {
        for (int j = 0; j < n - 1; ++j) {
            if (j != i && j != v[i]) {
                if (in(i, v[i], j) && out(i, v[i], v[j]) || in(i, v[i], v[j]) && out(i, v[i], j)) {
                    fout << "Case #" << I << ": Impossible\n";
                    //cout << i << ' ' << j << endl;
                    //cout << v[i] << ' ' << v[j] << endl << endl;;
                    return;
                }
            }
        }
    }
    //cout << "ololo";
    fout << "Case #" << I << ": ";
    for (int i = 0; i < n; ++i) {
        g.resize(0);
        if (h[i] == 0) {
            h[i] = 1;
            g.push_back(i);
            int j = v[i];
            while (!h[j]) {
                g.push_back(j);
                j = v[j];
            }
            g.push_back(j);
            rec(g);
        }
        fout << h[i] << ' ';
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
