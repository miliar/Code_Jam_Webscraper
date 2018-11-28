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

// welcome to code jam
const string STR = "welcome to code jam";

int solve(const string& s)
{
    vector<vector<int> > t(s.length() + 1, vector<int>(STR.length() + 1));

    for (int i = 0; i <= s.length(); ++i) {
        t[i][0] = 1;
    }
    for (int i = 1; i <= s.length(); ++i) {
        for (int j = 1; j <= STR.length(); ++j) {
            if (s[i - 1] == STR[j - 1]) {
                t[i][j] += t[i - 1][j - 1];
            }
            t[i][j] += t[i - 1][j];
            t[i][j] %= 10000;
        }
    }

    return t[s.length()][STR.length()];
}



int main(void)
{
    int N; cin >> N;
    string str;
    getline(cin, str);

    for (int i = 0; i < N; ++i) {
        getline(cin, str);

        int v = solve(str);
        char buf[256];
        sprintf(buf, "Case #%d: %04d", i + 1, v);
        cout << buf << endl;
    }

    return 0;
}

