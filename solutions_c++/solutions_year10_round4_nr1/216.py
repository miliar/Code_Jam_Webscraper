#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> vi;

vector<vi> diamond;
int k;

bool TestEqual(int x, int y, int p) {
    if (x < 0 || x >= 2 * k - 1 || y < 0 || y >= 2 * k - 1)
        return true;
    return (diamond[x][y] == p);
}

int main(void) {
    int TestNum;
    scanf("%d", &TestNum);
    for (int testNo = 1; testNo <= TestNum; testNo++) {
        scanf("%d", &k);
        diamond.assign(2 * k - 1, vi(2 * k - 1));
        for (int i = 0; i < 2*k-1; i++) {
            for (int j = 0; j <= i && j < k; j++) {
                if (i - j >= k)
                    continue;
                scanf("%d", &diamond[2 * (i - j)][2*j]);
            }
        }
        int bestx, besty;
        int bestSize = k * 4;
        for (int x = -4*k + 1; x < 4 * k; x++) {
            for (int y = -4*k; y < 4 * k; y++) {
                if ((x + y) % 2 != 0)
                    continue;
                bool good = true;
                for (int i = 0; i < 2 * k; i+=2) {
                    for (int j = 0; j < 2 * k; j+=2) {
                        if (!TestEqual(i + ((x + y) - (i + j)), j + ((x + y) - (i + j)), diamond[i][j])
                            || !TestEqual(i + ((x - y) - (i - j)), j - ((x - y) - (i - j)), diamond[i][j])
                            )
                        {
                            good = false;
                            goto label;
                        }
                    }
                }
label:
                if (!good)
                    continue;
                int size = max(x, y);
                size = max(size, 2 * k - 2 - x);
                size = max(size, 2 * k - 2 - y);
                size += 1;
                if (size < bestSize) {
                    bestx = x;
                    besty = y;
                    bestSize = size;
                }
            }
        }
        printf("Case #%d: %d\n", testNo, bestSize*bestSize - k*k);
    }
}
