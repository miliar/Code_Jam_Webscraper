#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
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
        int T;
        cin >> T;
        for (int t = 1; t <= T; t++) {
                bool ret = false;
                long long n, pd, pg;
                cin >> n >> pd >> pg;
                
                if ((pd != 0 && pg == 0) ||
                    (pd != 100 && pg == 100)) {
                        ret = false;
                } else if (pd == 0) {
                        ret = true;
                } else {
                        for (long long i = 1; i <= min((long long)10005, n); i++) {
                                long long d = i * 100 / pd;
                                if (i * 100 % pd != 0) continue;
                                if (d <= n) {
//                                        cout << i << " " << d << endl;
                                        ret = true;
                                        break;
                                }
                        }
                }

                cout << "Case #" << t << ": " << (ret ? "Possible" : "Broken") << endl;
        }
        return 0;
}

