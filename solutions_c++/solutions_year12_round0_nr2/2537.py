#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N, S, p;
        cin >> N >> S >> p;

        int ok = 0;
        int bad = 0;
        int t;
        for (int j = 0; j < N && cin >> t; ++j) {
            if (t <= 1) {
                if (t >= p)
                    ++ok;
                else
                    ++bad;
            } else {
                if ((t+2)/3 >= p)
                    ++ok;
                else if ((t+1)/3 + 1 < p)
                    ++bad;
            }
        }
        cout << "Case #" << i+1 << ": " << ok + min(N-ok-bad, S) << '\n';
    }
}
