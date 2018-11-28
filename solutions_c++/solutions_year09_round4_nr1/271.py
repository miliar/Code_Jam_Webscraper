#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

int ReadRow() {
    string s;
    cin >> s;
    for (int i = (int)s.size() - 1; i >= 0; --i)
        if (s[i] == '1')
            return i;
    return 0;
}

int N, p[50];

int solve() {
    cin >> N;
    for (int i = 0; i < N; ++i)
        p[i] = ReadRow();
    int ans = 0;
    for (int i = 0; i < N; ++i)
        if (p[i] > i) {
            int j = i;
            for (; j < N && p[j] > i; ++j);
            for (int k = j; k > i; --k) {
                swap(p[k], p[k - 1]);
                ++ans;
            }
        }
    return ans;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        freopen((string(argv[1]) + ".in").c_str(), "r", stdin);
        freopen((string(argv[1]) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
