#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> pii;

int sg (int x) {
    if (x < 0)
        return -1;
    else return 1;
}

int main() {
    int n, T;
    cin >> T;
    string in;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        cin >> n;
        vector<char> vc(n);
        vi but(n);
        for (int i = 0; i < n; ++i) {
            cin >> in >> but[i];
            vc[i] = in[0];
//            cerr << in << " " << vc[i] << endl;
        }
        vi nextO(n + 1), nextB(n + 1);
        nextO.back() = nextB.back() = -1;
        for (int i = n - 1; i >= 0; --i) {
            nextO[i] = nextO[i + 1];
            nextB[i] = nextB[i + 1];
            if (vc[i] == 'O')
                nextO[i] = but[i];
            if (vc[i] == 'B')
                nextB[i] = but[i];
        }
        int res = 0, curO = 1, curB = 1;
        for (int i = 0; i < n; ++i) {
            int add = 0;
            if (vc[i] == 'O') {
                add = abs(curO - but[i]) + 1;
                res += add;
                curB += sg(nextB[i] - curB) * min(add, abs(nextB[i] - curB));
                curO = but[i];
            } else {
                add = abs(curB - but[i]) + 1;
                res += add;
                curO += sg(nextO[i] - curO) * min(add, abs(nextO[i] - curO));
                curB = but[i];
            }
//            cerr << add << " " << curO << " " << curB << endl;
        }
        cout << res << endl;
    }
    return 0;
}
