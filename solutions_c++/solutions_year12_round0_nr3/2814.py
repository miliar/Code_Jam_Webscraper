#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cassert>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long long ll;

const int LIM = 2000001;

vector<int> getpairs(int n) {
    ostringstream oss;
    oss << n;
    string s = oss.str();
    vector<int> res;
    for (int i = 0; i + 1 < s.size(); ++i) {
        char c = s[0];
        s.erase(s.begin());
        s += c;
        if (s[0] != '0') {
            istringstream iss(s);
            int m;
            iss >> m;
            if (m > n && m <= LIM && find(res.begin(), res.end(), m) == res.end()) {
                res.push_back(m);
            }
        }
    }

    return res;
}

int main()
{
    int T;
    cin >> T;

    vector< vector<int> > recycle(LIM);

    for (int i = 1; i < LIM; ++i) {
        recycle[i] = getpairs(i);
    }

    for (int test = 1; test <= T; ++test) {
        int a, b;
        cin >> a >> b;
        ll r = 0;
        for (int i = a; i < b; ++i) {
            for (int j = 0; j < recycle[i].size(); ++j) {
                r += (recycle[i][j] <= b);
            }
        }

        cout << "Case #" << test << ": " << r << endl;
    }

    return 0;
}
