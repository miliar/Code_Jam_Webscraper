#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = (1 << 31) - 1;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;


pll getCenter(ll x, ll y) {
    return pll(x * 2LL + 1LL, y * 2LL + 1LL);
}
ll R, C, D;


pll operator * (const pll& lhs, ll scalar) {
    return pll(lhs.first * scalar, lhs.second * scalar);
}

pll operator / (const pll& lhs, ll scalar) {
    return pll(lhs.first / scalar, lhs.second / scalar);
}


pll operator + (const pll& lhs, const pll& rhs) {
    return pll(lhs.first + rhs.first, lhs.second + rhs.second);
}

pll operator - (const pll& lhs, const pll& rhs) {
    return pll(lhs.first - rhs.first, lhs.second - rhs.second);
}

vector<vector<pll> > prefix_sum;
vector<vector<ll> > mass_prefix_sum;

pll getPrefixSum(int x, int y) {
    if (x < 0 || y < 0) {
        return pll(0, 0);
    }
    return prefix_sum[x][y];
}


ll getMassPrefixSum(int x, int y) {
    if (x < 0 || y < 0) {
        return 0;
    }
    return mass_prefix_sum[x][y];
}

pll getSum(int x_min, int y_min, int x_max, int y_max) {
    pll res = 
        getPrefixSum(x_max, y_max)
        - getPrefixSum(x_min - 1, y_max)
        - getPrefixSum(x_max, y_min - 1)
        + getPrefixSum(x_min - 1, y_min - 1);
    return res;
}


ll getMassSum(int x_min, int y_min, int x_max, int y_max) {
    ll res = 
        getMassPrefixSum(x_max, y_max)
        - getMassPrefixSum(x_min - 1, y_max)
        - getMassPrefixSum(x_max, y_min - 1)
        + getMassPrefixSum(x_min - 1, y_min - 1);
    return res;
}

bool in(int x, int y) {
    return 0 <= x && x < R && 0 <= y && y < C;
}

void solveProblem() {
    cin >> R >> C >> D;
    vector<string> ff(R);
    for (int i = 0; i < ff.size(); ++i) {
        cin >> ff[i];
    }
    vector<vector<pll> > field(R, vector<pll>(C));
    vector<vector<ll> > mass_field(R, vector<ll>(C));
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            pll center = getCenter(i, j);
            ll mass = D + (ff[i][j] - '0');
            pll vector_mass = center * mass;
            field[i][j] = vector_mass;
            mass_field[i][j] = mass;
        }
    }
    prefix_sum.assign(R, vector<pll>(C));
    mass_prefix_sum.assign(R, vector<ll>(C));
    vector<vector<pll> > prefix_sum_in_line(R, vector<pll>(C));
    vector<vector<ll> > mass_prefix_sum_in_line(R, vector<ll>(C));
    for (int row = 0; row < R; ++row) {
        prefix_sum_in_line[row][0] = field[row][0];
        mass_prefix_sum_in_line[row][0] = mass_field[row][0];
        for (int column = 1; column < C; ++column) {
            prefix_sum_in_line[row][column] = prefix_sum_in_line[row][column - 1] + field[row][column];
            mass_prefix_sum_in_line[row][column] = mass_prefix_sum_in_line[row][column - 1] + mass_field[row][column];
        }
    }
    for (int column = 0; column < C; ++column) {
        prefix_sum[0][column] = prefix_sum_in_line[0][column];
        mass_prefix_sum[0][column] = mass_prefix_sum_in_line[0][column];
        for (int row = 1; row < R; ++row) {
            prefix_sum[row][column] = prefix_sum[row - 1][column] + prefix_sum_in_line[row][column];
            mass_prefix_sum[row][column] = mass_prefix_sum[row - 1][column] + mass_prefix_sum_in_line[row][column];
        }
    }
    ll res = 0;
    for (int l_x = 0; l_x < R; ++l_x) {
        for (int l_y = 0; l_y < C; ++l_y) {
            pll begin = getCenter(l_x, l_y);
            for (ll size = 3;;++size) {
                if (begin == pll(3, 3) && size == 5) {
                    cerr << "IT\n";
                }
                int u_x = l_x + size - 1;
                int u_y = l_y + size - 1;
                if (!in(u_x, u_y)) {
                    break;
                }
                pll end = getCenter(u_x, u_y);
                pll destination = (begin + end) / 2;
                ll future_mass = getMassSum(l_x, l_y, u_x, u_y);
                future_mass -= mass_field[l_x][l_y];
                future_mass -= mass_field[l_x][u_y];
                future_mass -= mass_field[u_x][l_y];
                future_mass -= mass_field[u_x][u_y];
                destination = destination *  future_mass;
                pll candidate = getSum(l_x, l_y, u_x, u_y);
                candidate = candidate - field[l_x][l_y];
                candidate = candidate - field[l_x][u_y];
                candidate = candidate - field[u_x][l_y];
                candidate = candidate - field[u_x][u_y];
                if (candidate == destination) {
                    res = max(res, size);
                }
            }
        }
    }
    if (res == 0) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        cout << res << endl;
    }
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        double t = clock();
        printf("Case #%d: ", test);
        solveProblem();
        t = (clock() - t) / CLOCKS_PER_SEC;
        cerr << test << " time " << t << " s\n";
    }
	return 0;
}
