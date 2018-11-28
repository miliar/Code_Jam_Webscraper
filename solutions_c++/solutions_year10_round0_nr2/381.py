#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int main() {
    int TESTCASE;
    int N;
    cin >> TESTCASE;
    for (int CASE = 1 ; CASE <= TESTCASE ; CASE++) {
        cin >> N;
        vector<long long> t(N);
        for(int i = 0 ; i < N ; i++) {
            cin >> t[i];
            //cout << t[i] << endl;
        }

        sort(t.begin(), t.end());

        vector<long long> v;
        for (int i = 0 ; i < t.size() - 1 ; i++) {
            //cout << "push:" << t[i + 1] - t[i] << endl;
            v.push_back(t[i + 1] - t[i]);
        }

        long long g;
        if (v.size() == 1) {
            g = v[0];
        }
        else {
            g = gcd(v[0], v[1]);
            for (int i = 2 ; i < v.size() ; i++) {
                g = gcd(g, v[i]);
            }
        }

        if (g == 1) {
            cout << "Case #" << CASE << ": " << 0 << endl;
        }
        else {
            long long tmp = t[0] / g + 1;
            if (t[0] % g == 0) tmp--;
            long long ans = g * tmp - t[0];
            cout << "Case #" << CASE << ": " << ans << endl;
        }
    }
}
