#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solve(int p, vector<int>& m, int mfrom, const vector<int>& prices, int lvl, int curr, bool& success)
{
    //cout << "solve(p = " << p << ", mfrom = " << mfrom << ", lvl = " << lvl << ", curr = " << curr << ")" << endl;

    if (lvl == 0) {
        success = true;
        return 0;
    }

    bool canbe0 = true;
    for (int i = mfrom, iend = mfrom + (1 << lvl); i < iend; ++i) {
        if (m[i] == 0) {
            canbe0 = false;
            break;
        }
    }

    bool ok0l = false, ok0r = false, ok1l = false, ok1r = false;
    int res0l = 0, res0r = 0, res1l = 0, res1r = 0;

    if (canbe0) {
        for (int i = mfrom, iend = mfrom + (1 << lvl); i < iend; ++i) --m[i];
        res0l = solve(p, m, mfrom,                  prices, lvl-1, curr * 2,     ok0l);
        res0r = solve(p, m, mfrom + (1 << (lvl-1)), prices, lvl-1, curr * 2 + 1, ok0r);
        for (int i = mfrom, iend = mfrom + (1 << lvl); i < iend; ++i) ++m[i];
    }

    res1l = solve(p, m, mfrom,                  prices, lvl-1, curr * 2,     ok1l);
    res1r = solve(p, m, mfrom + (1 << (lvl-1)), prices, lvl-1, curr * 2 + 1, ok1r);

    bool ok0 = ok0l && ok0r, ok1 = ok1l && ok1r;
    int res0 = res0l + res0r, res1 = res1l + res1r + prices[curr];

    success = ok0 || ok1;
    if (ok0 && ok1) {
        return min(res0, res1);
    } else if (ok0) {
        return res0;
    } else if (ok1) {
        return res1;
    }
    return -1;
}

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int p;
        cin >> p;
        vector<int> m(1 << p);
        for (int i = 0; i < (1 << p); ++i) {
            cin >> m[i];
        }
        vector<int> prices(1 << p);
        for (int i = p-1; i >= 0; --i) {
            for (int j = 0; j < (1 << i); ++j) {
                cin >> prices[(1 << i) + j];
            }
        }
        bool ok;
        int result = solve(p, m, 0, prices, p, 1, ok);
        cout << "Case #" << (test + 1) << ": " << result << endl;
    }
}
