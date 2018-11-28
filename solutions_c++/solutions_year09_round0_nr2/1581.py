#include<algorithm>
#include<cmath>
#include<iostream>
#include<list>
#include<cstring>
#include<climits>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<vector>
using namespace std;

template<class A, class B> void conv_(A& x, B& y) { stringstream s; s << x; s >> y; }

typedef unsigned int uint;
typedef unsigned long long int ullong;
#define for_(i, a, b) for(int i=(a);i<(b);++i)
#define set_(a, n) memset(a, n, sizeof a)

typedef vector<int> vi;
typedef vector<vi> vvi;

bool isOpen(int n) {
    return n <= 9;
}

void go (vvi& m, vvi& nov, int i, int j, int& next) {
    static int moves[4][2] = {
      {-1, 0}, {0, -1}, {0, 1}, {1, 0}
    };

    if (!isOpen(nov[i][j])) return;

    int min_a = INT_MAX, min_mi;

    for_(mi, 0, 4) {
        int ni = i + moves[mi][0], nj = j + moves[mi][1];
        if (ni < 0 || ni == m.size() || nj < 0 || nj == m[ni].size()) continue;

        int alt = m[ni][nj];

        if (alt < min_a) {
            min_a = alt;
            min_mi = mi;
        }
    }

    if (min_a == INT_MAX) {
        nov[i][j] = next++;
        return;
    }

    int ni = i + moves[min_mi][0], nj = j + moves[min_mi][1];
    int nalt = m[ni][nj];

    if (nalt >= m[i][j]) {
        nov[i][j] = next++;
    }
    else {
        go(m, nov, ni, nj, next);
        nov[i][j] = nov[ni][nj];
    }
}

int main(void) {
    int nt;
    cin >> nt;

    for_(t, 1, nt+1) {
        int h, w;
        cin >> h >> w;

        vvi m(h, vi(w));
        vvi nov(h, vi(w));

        for_(i, 0, h) for_(j, 0, w) {
            cin >> m[i][j];
            nov[i][j] = m[i][j];
        }

        int next = 'a';
        for_(i, 0, h) for_(j, 0, w)
            if (isOpen(nov[i][j])) {
                go(m, nov, i, j, next);
            }


        cout << "Case #" << t << ": " << endl;
        for_(i, 0, h) {
            for_(j, 0, w) {
                if (j) cout << ' ';
                cout << char(nov[i][j]);
            }
            cout << endl;
        }
    }

    return 0;
}
