#include <iostream>
#include <sstream>

#include <vector>
#include <string>

#include <algorithm>

using namespace std;

typedef int ll;

int readInt() {
    string s;
    getline(cin, s);
    stringstream ss(s);

    int res;
    ss >> res;

    return res;
}

string solve(ll A, ll N, ll M) {
    for (ll x0 = 0; x0 <= 0; ++x0) {
        for (ll y0 = 0; y0 <= 0; ++y0) {
            for (ll x1 = 0; x1 <= N; ++x1) {
                for (ll y1 = 0; y1 <= M; ++y1) {
                    for (ll x2 = 0; x2 <= N; ++x2) {
                        for (ll y2 = 0; y2 <= M; ++y2) {
                            if ((x1-x0)*(y2-y0) - (x2-x0)*(y1-y0) == A) {
                                stringstream ss;
                                ss << x0 << " " << y0 << " " << x1 << " " << y1 << " " << x2 << " " << y2;
                                return ss.str();
                            }
                        }
                    }
                }
            }
        }
    }

    return "IMPOSSIBLE";
}

int main(int argc, char* argv[]) {
    int testsNum = readInt();
    for (int test = 1; test <= testsNum; ++test) {
        ll A, N, M;
        cin >> N >> M >> A;
        cout << "Case #" << test << ": " << solve(A, N, M) << endl;
    }

    return 0;
}
