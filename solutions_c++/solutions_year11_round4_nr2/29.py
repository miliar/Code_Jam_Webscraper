#include <iostream>
using namespace std;

const int len = 505;

long long w[len][len], s[len][len][3];

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);
    
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        int N, M, D;
        cin >> N >> M >> D;
        for (int i = 1; i <= N; ++i)
            for (int j = 1; j <= M; ++j) {
                char c;
                cin >> c;
                w[i][j] = c - '0';
                s[i][j][0] = w[i][j] + s[i][j - 1][0] + s[i - 1][j][0] - s[i - 1][j - 1][0];
                s[i][j][1] = i * w[i][j] + s[i][j - 1][1] + s[i - 1][j][1] - s[i - 1][j - 1][1];
                s[i][j][2] = j * w[i][j] + s[i][j - 1][2] + s[i - 1][j][2] - s[i - 1][j - 1][2];
            }
        int ret = 0;
        for (int i = 3; i <= N; ++i)
            for (int j = 3; j <= M; ++j)
                for (int k = 3; k <= i && k <= j; ++k) {
                    long long S[3];
                    for (int l = 0; l < 3; ++l)
                        S[l] = s[i][j][l] + s[i - k][j - k][l] - s[i - k][j][l] - s[i][j - k][l];
                    long long w0 = w[i][j], w1 = w[i - k + 1][j], w2 = w[i][j - k + 1], w3 = w[i - k + 1][j - k + 1];
                    S[0] -= w0 + w1 + w2 + w3;
                    S[1] -= (w0 + w2) * i + (w1 + w3) * (i - k + 1);
                    S[2] -= (w0 + w1) * j + (w2 + w3) * (j - k + 1);
                    if (S[1] * 2 == S[0] * (2 * i - k + 1) && S[2] * 2 == S[0] * (2 * j - k + 1) && k > ret)
                        ret = k;
                }
        cout << "Case #" << t2 << ": ";
        if (ret) cout << ret << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    
    return 0;
}
