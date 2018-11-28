#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

long long cum[505][505] = {{}};

long long getsum(int l, int r, int t, int b) {
    b++, t++;
    return cum[b][r] + cum[t-1][l-1] - cum[b][l-1] - cum[t-1][r];
}

int solve() {
    int w, h, mass;
    char _masses[505][505] = {{}};
    long long masses[505][505] = {{}};

    scanf("%d %d %d", &h, &w, &mass);
    for (int i = 0; i < h; i++) {
        scanf("%s", _masses[i]);
        long long sum = 0;
        for (int k = 0; k < w; k++) {
            masses[i][k] = _masses[i][k]-'0' + mass;
            sum += masses[i][k];
            cum[i+1][k] = cum[i][k] + sum;
        }
    }

    int best = -1;
    for (int y = 1; y < h; y++) {
        for (int x = 1; x < w; x++) {
            for (int s = 1; s <= 500; s++) {
                if (x-s <0 || y-s < 0 || y+s >= h || x+s >= w)
                    break;
                long long top = 0, lef = 0, rig = 0, bot = 0;
                for (int i = 0; i <= s; i++) {
                    for (int k = 0; k <= s; k++) {
                        if (!(i == s && k == s)) {
                            top += masses[y-i][x+k] * i + (k?masses[y-i][x-k] * i:0);
                            bot += masses[y+i][x+k] * i + (k?masses[y+i][x-k] * i:0);
                            lef += masses[y-i][x-k] * k + (i?masses[y+i][x-k] * k:0);
                            rig += masses[y-i][x+k] * k + (i?masses[y+i][x+k] * k:0);
                        }
                    }
                }

                if (top == bot && lef == rig) {
                    best = max(best, 2*s+1);
                }
            }

            for (int s = 2; s <= 500; s++) {
                if (x-s < -1 || y-s < -1 || y+s >= h || x+s >= w)
                    break;
                long long top = 0, lef = 0, rig = 0, bot = 0;
                for (int i = 1; i <= s; i++) {
                    for (int k = 1; k <= s; k++) {
                        if (!(i == s && k == s)) {
                            top += masses[y-i+1][x+k] * i + masses[y-i+1][x-k+1] * i;
                            bot += masses[y+i][x+k] * i + masses[y+i][x-k+1] * i;
                            lef += masses[y-i+1][x-k+1] * k + masses[y+i][x-k+1] * k;
                            rig += masses[y-i+1][x+k] * k + masses[y+i][x+k] * k;
                        }
                    }
                }

                if (top == bot && lef == rig) {
                    best = max(best, 2*s);
                }
            }
        }
    }

    return best;
}

int main() {
    int T;
    scanf ("%d\n", &T);
    for (int i = 1; i <= T; i++) {
        int sol = solve();
        if (sol != -1)
            printf("Case #%d: %d\n", i, sol);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }

    return 0;
}
