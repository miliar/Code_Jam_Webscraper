#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

#define D(x) x

using namespace std;

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
        int N, K, B, T;
        cin >> N >> K >> B >> T;

        vector<int> X(N), V(N);
        for (int i = 0; i < N; i++) cin >> X[i];
        for (int i = 0; i < N; i++) cin >> V[i];

        vector<int> ok;
        for (int i = 0; i < N; i++) {
            int F = X[i] + V[i]*T;
            if (F >= B) ok.push_back(i);
        }

        if (ok.size() < K) {
            cout << "Case #" << testCase << ": IMPOSSIBLE" << endl;
        } else {
            reverse(ok.begin(), ok.end());
            int swaps = 0;
            for (int i = 0; i < K; i++) {
                swaps += (N-1-i) - ok[i];
            }
            cout << "Case #" << testCase << ": " << swaps << endl;
        }
    }

}
