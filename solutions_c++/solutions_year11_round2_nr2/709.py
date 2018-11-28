#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double solve()
{
    int c, d;
    cin >> c >> d;
    vector<long long> X;
    for (int i = 0; i < c; i++) {
        long x;
        int k;
        cin >> x >> k;
        for (int j = 0; j < k; j++)
            X.push_back(x);
    }
    sort(X.begin(), X.end());
    long long maxdist = 0;
    for (int i = 1; i < X.size(); i++)
        if (X[i] < X[i - 1] + d) {
            int dist = X[i - 1] + d - X[i];
            if (maxdist < dist)
                maxdist = dist;
            X[i] = X[i - 1] + d;
        }
    return (double) maxdist / 2;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        double answer = solve();
        cout << "Case #" << t << ": " << answer << endl;
    }
    return 0;
}
