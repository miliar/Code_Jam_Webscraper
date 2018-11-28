#include <iostream>
#include <cstring>
using namespace std;
const int maxn = 1000;

int f[maxn][maxn];

int main(void)
{
        int T;

        cin >> T;
        for (int loop = 1; loop <= T; loop++) {
                int n;
                int pos[10000 + 10], len[10000 + 10];

                cin >> n;
                for (int k = 1; k <= n; k++)
                        cin >> pos[k] >> len[k];
                len[0] = pos[0];

                int target;
                cin >> target;

                bool gotIt = false;
                /*
                int k = 0;
                while (pos[k] + len[k] < target) {

                        int i;
                        int maxl, r = -1;
                        for (i = k + 1; i < n; i++) {
                                if (pos[i] - pos[k] > len[k])
                                        break;
                                if (pos[i] + min(len[k]))
                        for (i = n - 1; i > k; i--)
                                if (pos[i] - pos[k] <= len[k])//&& pos[i] - pos[k] <= len[i])
                                        break;
                        if (i <= k)
                                break;

                        len[i] = pos[i] - pos[k];
                        k = i;
                }
                */

                memset(f, 0, sizeof(f));
                f[0][1] = pos[1] + min(len[1], pos[1]);
                if (f[0][1] >= target)
                        gotIt = true;

                for (int i = 0; i <= n && !gotIt; i++)
                        for (int j = i + 1; j <= n; j++)
                                if (f[i][j]) {
                                        for (int k = j + 1; k <= n; k++)
                                                if (pos[k] <= f[i][j]) {
                                                        f[j][k] = pos[k] + min(pos[k] - pos[j], len[k]);
                                                        if (f[j][k] >= target)
                                                                gotIt = true;
                                                }
                                }

                cout << "Case #" << loop << ": " << (gotIt ? "YES" : "NO") << endl;
        }
        return 0;
}
