#include <iostream>

using namespace std;

const int MAX = 50;
int N, K, B, T, X[MAX], V[MAX];

void ReadData() {
    cin >> N >> K >> B >> T;
    for (int i = 0; i < N; ++i)
        cin >> X[i];
    for (int i = 0; i < N; ++i)
        cin >> V[i];
}

int Work() {
    if (K == 0)
        return 0;
    int res = 0, bad = 0, good = 0;
    for (int i = N - 1; i >= 0; --i) {
        if (B - X[i] <= T * V[i]) {
            res += bad;
            if (++good == K)
                return res;
        } else {
            ++bad;
        }
    }
    return -1;
}

void Output(int t, int res) {
    cout << "Case #" << t << ": ";
    if (res != -1)
        cout << res;
    else
        cout << "IMPOSSIBLE";
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        ReadData();
        Output(i, Work());
    }
    return 0;
}

