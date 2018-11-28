#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool in(int x, int y, int n)
{
    return x >= 0 && x < n && y >= 0 && y < n;
}

bool check(const vector<string>& res, int n, char c, int x, int y, int len, int sx, int sy)
{
    if ((!in(x - sx, y - sy, n) || in(x - sx, y - sy, n) && res[x - sx][y - sy] != c) &&
        in(x + sx * (len-1), y + sy * (len-1), n)) {
        for (int i = 0; i < len; ++i) {
            if (res[x + sx * i][y + sy * i] != c) return false;
        }
        return true;
    }
    return false;
}

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int n, k;
        cin >> n >> k;
        vector<string> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        vector<string> res(n, string(n, '.'));
        for (int i = 0; i < n; ++i) {
            for (int j = 0, jj = n-1; jj >= 0; --jj) {
                if (a[n-i-1][jj] != '.') {
                    res[n-j-1][i] = a[n-i-1][jj];
                    ++j;
                }
            }
        }
        //for (int i = 0; i < n; ++i) {
        //    copy(res[i].begin(), res[i].end(), ostream_iterator<char>(cout)); cout << endl;
        //}
        char cc[] = {'R', 'B'};
        bool ok[2] = {false, false};
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int cn = 0; cn < 2; ++cn) {
                    if (check(res, n, cc[cn], i, j, k, 1, 0) || 
                        check(res, n, cc[cn], i, j, k, 0, 1) ||
                        check(res, n, cc[cn], i, j, k, 1, 1) ||
                        check(res, n, cc[cn], i, j, k, 1, -1)) ok[cn] = true;
                }
            }
        }
        cout << "Case #" << (test + 1) << ": ";
        if (ok[0] && ok[1]) cout << "Both" << endl;
        else if (ok[0]) cout << "Red" << endl;
        else if (ok[1]) cout << "Blue" << endl;
        else cout << "Neither" << endl;
    }
}
