#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <cmath>
#include <cassert>

using namespace std;
typedef complex<double> P;

class UnionFind {
private:
  vector<int> v;

public:
  UnionFind(int n) : v(n) {
    for (int i = 0; i < n; ++i) {
      v[i] = i;
    }
  }

  int find(int i) {
    if (v[i] == i) { return i; }
    return (v[i] = find(v[i]));
  }

  void unify(int a, int b) {
    v[find(b)] = find(a);
  }
};

const int dx[] = { 0, -1, 1, 0 };
const int dy[] = { -1, 0, 0, 1 };

void solve(UnionFind& uf, const vector<vector<int> >& alt, int H, int W) {
    for (int h = 0; h < H; ++h) {
        for (int w = 0; w < W; ++w) {
            int lowest = 1000000, lowest_dir = 0;
            for (int d = 0; d < 4; ++d) {
                int hh = h + dy[d], ww = w + dx[d];
                if (hh < 0 || H <= hh || ww < 0 || W <= ww) { continue; }
                if (alt[hh][ww] < lowest) {
                    lowest = alt[hh][ww];
                    lowest_dir = d;
                }
            }

            if (lowest < alt[h][w]) {
                int hh = h + dy[lowest_dir];
                int ww = w + dx[lowest_dir];
                uf.unify(W * h + w, W * hh + ww);
            }
        }
    }
}


int main(void)
{
    int N; cin >> N;
    for (int n = 0; n < N; ++n) {
        int H, W; cin >> H >> W;
        vector<vector<int> > alt(H, vector<int>(W));
        for (int h = 0; h < H; ++h) {
            for (int w = 0; w < W; ++w) {
                cin >> alt[h][w];
            }
        }

        UnionFind uf(H * W);
        solve(uf, alt, H, W);

        char cur = 'a';
        map<int, char> m;

        cout << "Case #" << (n + 1) << ":" << endl;
        for (int h = 0; h < H; ++h) {
            for (int w = 0; w < W; ++w) {
                if (w) { cout << ' '; }
                int kind = uf.find(h * W + w);
                if (!m.count(kind)) {
                    m[kind] = cur++;
                }
                cout << m[kind];
            }
            cout << endl;
        }
    }
    return 0;
}

