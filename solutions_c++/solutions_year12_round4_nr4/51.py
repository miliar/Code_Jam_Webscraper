#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;

#include <ext/hash_map>

using namespace __gnu_cxx;

typedef bitset<100> board;

board input, mask;
board cave[10];
board caveSet[10];
bool occur[10];
char G[16][16];
int n, m;

struct myhash {
    std::hash<board> hash_fn;
    unsigned operator()(const board &b) const {
        return hash_fn(b);
    }
};

hash_map<board, bool, myhash> M;

bool go(board b)
{
    if ((b & ~mask).any())
        return false;
    if (M.count(b))
        return M[b];
    bool &ret = M[b];
    if (go(b << m & input | (b << m & ~input) >> m))
        return ret = true;
    if (go(b << 1 & input | (b << 1 & ~input) >> 1))
        return ret = true;
    if (go(b >> 1 & input | (b >> 1 & ~input) << 1))
        return ret = true;
    return ret = false;
}

int main()
{
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%s", G+i);
        input.reset();
        memset(occur, false, sizeof(occur));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (G[i][j] != '#') {
                    input.set(i * m + j);
                }
                if (G[i][j] >= '0' && G[i][j] <= '9') {
                    int num = G[i][j] - '0';
                    occur[num] = true;
                    cave[num].reset();
                    cave[num].set(i * m + j);
                }
            }
        printf("Case #%d:\n", ++cas);
        for (int i = 0; i < 10; i++) {
            if (!occur[i])
                continue;
            board b = cave[i];
            for (;;) {
                board nb = b | b >> m | b << 1 | b >> 1;
                nb &= input;
                if (nb == b)
                    break;
                b = nb;
            }
            caveSet[i] = b;
            mask = caveSet[i];
            M.clear();
            M[cave[i]] = true;
            printf("%d: %d %s\n", i, caveSet[i].count(), go(mask) ? "Lucky" : "Unlucky");
        }
    }
}
