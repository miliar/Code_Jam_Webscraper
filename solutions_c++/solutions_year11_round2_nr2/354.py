#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>

using namespace std;

// BEGIN CUT HERE

template<typename T> std::ostream& operator<<(std::ostream& os, const vector<T> &v) {
        os << "[";
        int N = v.size();
        for (int i = 0; i < N; i++) {
                os << v[i];
                if (i != (N - 1)) os << ", ";
        }
        os << "]" << endl;
}

// END CUT HERE

int main() {
        cout.precision(15);

        int T;
        cin >> T;
        for (int t = 1; t <= T; t++) {
                long long C, D;
                cin >> C >> D;

                vector<long long> pos(C);
                vector<long long> cnt(C);
                vector<long long> sum(C);
                for (int i = 0; i < C; i++) {
                        cin >> pos[i] >> cnt[i];
                }

                long double ret = 0;
                sum[0] = cnt[0];
                for (int i = 1; i < C; i++) {
                        sum[i] = sum[i - 1] + cnt[i];
                }
                for (int i = 0; i < C; i++) {
                        for (int j = i; j < C; j++) {
                                long long nPoints = sum[j];
                                if (i > 0) nPoints -= sum[i - 1];
                                ret = max(ret, ((nPoints - 1) * D - (pos[j] - pos[i]))/ (long double)2);
                        }
                }

                cout << "Case #" << t << ": " << ret << endl;
        }

        return 0;

}

