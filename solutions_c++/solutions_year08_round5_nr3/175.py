#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void gen(const vector<bool>& possible, int x, int W, vector<int>& dp, int cnt,
    int state)
{
    if (x >= W) {
        dp[state] = max(dp[state], cnt);
        return;
    }

    gen(possible, x + 1, W, dp, cnt, state);

    if (possible[x])
        gen(possible, x + 2, W, dp, cnt + 1, state | (1 << x));

    return;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cs = 0; cs < cases; ++cs) {
        int H, W;
        cin >> H >> W;
        vector<string> field;
        for (int i = 0; i < H; ++i) {
            string l;
            cin >> l;
            field.push_back(l);
        }

        vector<int> dp(1 << W, -1);
        dp[0] = 0;

        for (int y = 0; y < H; ++y) {
            vector<int> ndp(1 << W, -1);
            for (int s = 0; s < (1<<W); ++s) {
                if (dp[s] == -1) continue;
                vector<bool> possible(W, true);
                for (int x = 0; x < W; ++x)
                    if (field[y][x] == 'x')
                        possible[x] = false;
                for (int x = 0; x < W; ++x)
                    if (s & (1<<x)) {
                        if (x > 0) possible[x-1] = false;
                        if (x < W-1) possible[x+1] = false;
                    }

                gen(possible, 0, W, ndp, dp[s], 0);
            }

            dp.swap(ndp);
        }

        int best = 0;
        for (int i = 0; i < (1<<W); ++i)
            best = max(best, dp[i]);

        cout << "Case #" << cs + 1 << ": " << best << '\n';
    }

    return 0;
}
