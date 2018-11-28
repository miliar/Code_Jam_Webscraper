#include <iostream>

using namespace std;

    const int maxp = 10, maxt = 1024, unknown = -1, infinity = 1000000000;

    int P, T, C[maxp + 1][maxt];
    long long data[maxp + 1][maxt][maxp + 1];

long long cost(int p, int i, int k)
{
    if (data[p][i][k] == unknown) {
        if (p == P)
            data[p][i][k] = C[p][i] < (P - k) ? infinity : 0;
        else
            data[p][i][k] = min(C[p][i] + cost(p + 1, 2*i, k + 1) + cost(p + 1, 2*i + 1, k + 1),
                                cost(p + 1, 2*i, k) + cost(p + 1, 2*i + 1, k));
    }
    return data[p][i][k];
}

long long solve()
{
    cin >> P;
    T = 1; for (int i = 0; i < P; i++) T *= 2;
    for (int i = 0; i < T; i++) {
        cin >> C[P][i];
        for (int k = 0; k <= P; k++)
            data[P][i][k] = unknown;
    }
    for (int i = P - 1; i >= 0; i--) {
        T /= 2;
        for (int j = 0; j < T; j++) {
            cin >> C[i][j];
            for (int k = 0; k <= P; k++)
                data[i][j][k] = unknown;
        }
    }
    /*
    for (int i = 0; i <= P; i++) {
        for (int j = 0; j < T; j++)
            cout << C[i][j] << " ";
        cout << endl;
        T *= 2;
    }
    */
    return cost(0, 0, 0);
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long long answer = solve();
        cout << "Case #" << t << ": " << answer << endl;
    }
    return 0;
}
