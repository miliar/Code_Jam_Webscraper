#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <deque>
#include <queue>
#include <set>
#include <tr1/unordered_set>
#include <tr1/unordered_map>

#define D(x) x

using namespace std;
using namespace std::tr1;

typedef pair<int, int> state;

bool solve(int N, vector<int>& d, vector<int>& l, int D) {
    if (D <= 2*d[0]) return true;

    vector<state> current, next;
    set<state> visited;

    for (int i = 1; i < N; i++) {
        if (d[i] <= 2*d[0]) {
            current.push_back(make_pair(0, i));
        }
    }

    while (!current.empty()) {
        for (vector<state>::iterator it = current.begin(); it != current.end(); it++) {
            state s = *it;
            if (visited.find(s) != visited.end()) continue;
            visited.insert(s);

            int i = s.first, j = s.second;
            int len = min(l[j], d[j] - d[i]);
            if (D <= d[j] + len) return true;
            for (int k = j+1; k < N; k++) {
                if (d[k] <= d[j] + len) {
                    next.push_back(make_pair(j, k));
                }
            }
        }
        swap(current, next);
        next.clear();
    }
    return false;
}


int main() {
    int T;
    cin >> T;

    for (int testCase = 1; testCase <= T; testCase++) {
        int N;
        cin >> N;

        vector<int> d(N), l(N);

        for (int i = 0; i < N; i++) {
            cin >> d[i] >> l[i];
        }
        int D;
        cin >> D;

        bool result = solve(N, d, l, D);
        cout << "Case #" << testCase << ": " << (result ? "YES" : "NO");

        cout << endl;
    }
}
