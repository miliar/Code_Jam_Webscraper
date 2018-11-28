#include <iostream>
#include <vector>
using namespace std;

long long sum(vector< vector<long long> >& p, int i, int j)
{
    return p[i][j-1] + p[i-1][j] - p[i-1][j-1];
}

long long square(vector< vector<long long> >& p, int i, int j, int k)
{
    return p[i+k][j+k] - p[i+k][j] - p[i][j+k] + p[i][j];
}

long long corners(vector< vector<long long> >& w, int i, int j, int k)
{
    return w[i][j] + w[i+k-1][j] + w[i][j+k-1] + w[i+k-1][j+k-1];
}

long long wcornersi(vector< vector<long long> >& w, int i, int j, int k)
{
    return w[i][j] * (i*2+1) + w[i+k-1][j] * ((i+k-1)*2+1) + w[i][j+k-1] * (i*2+1) + w[i+k-1][j+k-1] * ((i+k-1)*2+1);
}

long long wcornersj(vector< vector<long long> >& w, int i, int j, int k)
{
    return w[i][j] * (j*2+1) + w[i+k-1][j] * (j*2+1) + w[i][j+k-1] * ((j+k-1)*2+1) + w[i+k-1][j+k-1] * ((j+k-1)*2+1);
}

bool check(int i, long long pmp, long long mp)
{
    return mp * i == pmp;
}

int solve(int r, int c, vector< vector<long long> >& w)
{
    vector< vector<long long> >
        pmpi2(r + 1, vector<long long>(c + 1)),
        pmpj2(r + 1, vector<long long>(c + 1)),
        mp(r + 1, vector<long long>(c + 1));
    for (int i = 1; i <= r; ++i) {
        for (int j = 1; j <= c; ++j) {
            pmpi2[i][j] = sum(pmpi2, i, j) + (i * 2 - 1) * w[i-1][j-1];
            pmpj2[i][j] = sum(pmpj2, i, j) + (j * 2 - 1) * w[i-1][j-1];
            mp[i][j] = sum(mp, i, j) + w[i-1][j-1];
        }
    }
    for (int k = min(r, c); k >= 3; --k) {
        for (int i = 0; i <= r - k; ++i) {
            for (int j = 0; j <= c - k; ++j) {
                long long m = square(mp, i, j, k) - corners(w, i, j, k);
                if (check(i * 2 + k, square(pmpi2, i, j, k) - wcornersi(w, i, j, k), m) && 
                    check(j * 2 + k, square(pmpj2, i, j, k) - wcornersj(w, i, j, k), m)) {
                    return k;
                }
            }
        }
    }
    return -1;
}

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int r, c, d;
        cin >> r >> c >> d;
        vector< vector<long long> > w(r, vector<long long>(c));
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                char tmp;
                cin >> tmp;
                w[i][j] = d + (tmp - '0');
            }
        }
        int result = solve(r, c, w);
        cout << "Case #" << (test + 1) << ": ";
        if (result == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << result;
        }
        cout << endl;
    }
}
