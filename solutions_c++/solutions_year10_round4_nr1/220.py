#include <stdio.h>

#include <algorithm>

char map[1000][1000];

int br[1000], er[1000];

int k;

bool ac(int x, int y, int xt, int yt) {
    if (xt < 0 || xt >= 2 * k - 1 || yt < br[xt] || yt >= er[xt]) {
        return true;
    }
    if (map[x][y] != map[xt][yt]) {
        return false;
    }
    return true;
}

bool check(int x, int y) {
    for (int i = 0; i < 2 * k - 1; i++) {
        for (int j = br[i]; j < er[i]; j++) {
            int xt = 2 * x - i, yt = 2 * y - j;
            if (!ac(i, j, xt, j) || !ac(i, j, i, yt)) {
                return false;
            }
       }
    }
    return true;
}

int main() {
    int caseSize;
    scanf("%d", &caseSize);
    for (int T = 1; T <= caseSize; T++) {
        scanf("%d", &k);
        gets(map[0]);
        for (int i = 0; i < 2 * k - 1; i++) {
            gets(map[i]);
        }
        for (int i = 0; i < 2 * k - 1; i++) {
            br[i] = 0;
            while (map[i][br[i]] == ' ') {
                br[i]++;
            }
            er[i] = 2 * k - 1 - br[i];
        }
        int result = 1000;
        for (int i = 0; i < 2 * k - 1; i++) {
            for (int j = 0; j < 2 * k - 1; j++) {
                if (check(i, j)) {
                    int s = 0, t = i + j;
                    s = std::max(s, std::abs(3 * k - 3 - t));
                    s = std::max(s, std::abs(t - k + 1));
                    t = i - j;
                    s = std::max(s, std::abs(k - 1 - t));
                    s = std::max(s, std::abs(t + k - 1));
                    s = (s + 1) / 2 * 2 + ((s + 1) & 1);
                    result = std::min(s, result);
                }
            }
        }
        printf("Case #%d: %d\n", T, result * result - k * k);
    }
    return 0;
}
