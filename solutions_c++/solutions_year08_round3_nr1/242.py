#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>

using namespace std;

typedef vector<long long> vi;

long long solve(int maxl, int k, vi& p) {
    long long res = 0;

    sort(p.begin(), p.end(), greater<int>());
    for (int i=0; i<p.size(); ++i) {
        res += ((i / k) + 1) * p[i];
    }

    return res;
}

int main() {
    int testsNum;
    cin >> testsNum;
    for (int test=1; test <= testsNum; ++test) {
        int P, K, L;
        cin >> P >> K >> L;

        vi p(L);
        for (int i=0; i<p.size(); ++i) {
            cin >> p[i];
        }

        cout << "Case #" << test << ": ";
        if (L > P * K) {
            cout << "Impossible";
        } else {
            cout << solve(P, K, p);
        }

        cout << endl;
    }

    return 0;
}
