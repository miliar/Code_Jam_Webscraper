#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>

#include <cmath>

using namespace std;

int main(int argc, char* argv[]) {

    int T = 0;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        int answer = 0;

        int N = 0;
        int S = 0;
        int p = 0;

        cin >> N >> S >> p;

        vector<int> a(N);
        for (int i = 0; i < N; ++i)
            cin >> a[i];
        sort(a.begin(), a.end(), greater<int>());

        for (int i = 0; i < N; ++i) {
            if (a[i] >= 3*p-2)
                ++answer;
            else if (a[i] >= max(p, 3*p-4) && S > 0) {
                ++answer;
                --S;
            }
        }

        cout << "Case #" << test << ": " << answer << endl;
    }

    return 0;
}
