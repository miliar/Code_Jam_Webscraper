#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define uint unsigned int

#define FOR(i, n) for (int i = 0; i < (n); i++)
#define FORU(i, n) for (uint i = 0; i < (n); i++)
#define FORR(i, n) for (int i = (n)-1; i >= 0; i--)
#define FORRU(i, n) for (uint i = (n)-1; i >= 0; i--)
#define FOREACH(it, v) for (__typeof__(v.begin()) it = (v).begin(); it != (v).end(); ++it)

int lab[512][512];
int used[512][512];

int main() {
    int cases;
    scanf("%d", &cases);

    FOR(tcase, cases) {
        int h, w;
        scanf("%d %d", &h, &w);

        map<int, int> res;

        FOR(y, h) {
            FOR(i, w/4) {
                int w4;
                scanf("%1x", &w4);
                FOR(j, 4) {
                    lab[y][i * 4 + j] = ((w4 & (1 << (3 - j))) == (1 << (3 - j)));
                }
            }
            FOR(x, w) {
                used[y][x] = 0;
            }
        }

        // FOR(y, h) {
            // FOR(x, w) {
                // printf("%d", lab[y][x]);
            // }
            // printf("\n");
        // }

        int f;
        for (int s = min(h, w); s > 0; s--) {
            FOR(y, h-s+1) {
                FOR(x, w-s+1) {
                    if (used[y][x]) continue;

                    // int k, l;
                    // f = lab[y][x];
                    // for (k = y; k < h; k++) {
                        // if (lab[k][x] != f) {
                            // break;
                        // }
                        // f ^= 1;
                    // }
                    // if (k == y) continue;

                    // f = lab[y][x];
                    // for (l = x; l < w; l++) {
                        // if (lab[y][l] != f) {
                            // break;
                        // }
                        // f ^= 1;
                    // }
                    // if (l == x) continue;

                    // int s = min(k-y, l-x);
                    int g, h;
                    bool found = true;
                    f = lab[y][x];
                    for (g = y; g < y+s; g++) {
                        for (h = x; h < x+s; h++) {
                            if (lab[g][h] != f || used[g][h]) {
                                found = false;
                                break;
                            }
                            f ^= 1;
                        }
                        if (s % 2 == 0) {
                            f ^= 1;
                        }
                    }

                    if (found) {
                        res[s]++;
                        for (g = y; g < y+s; g++) {
                            for (h = x; h < x+s; h++) {
                                used[g][h] = s;
                            }
                        }
                        // fprintf(stderr, "FOO: %d: %d %d\n", s, y, x);
                    }
                }
            }
        }

        // FOR(y, h) {
            // FOR(x, w) {
                // printf("%d", used[y][x]);
            // }
            // printf("\n");
        // }

        printf("Case #%d: %u\n", tcase+1, (uint) res.size());
        for (map<int, int>::reverse_iterator it = res.rbegin(); it != res.rend(); ++it) {
            printf("%d %d\n", it->first, it->second);
        }
    }

    return 0;
}
