#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, s, p;
int scores[105];

#define fori(i, lim) for (int i = 0; i < lim; i++)

void magic() {
    // (n, s, num >= p)
    int cache[105][105];
    memset(cache, -1, sizeof(cache));

    for (int i = 0; i <= n; i++)
        cache[i][s] = 0;

    for (int i = n-1; i >= 0; i--) {
        for (int k = 0; k <= s; k++) {
            bool can_surprise = false;
            bool can_attain = false;
            bool can_both = false;

            fori (a, 11) {
                fori (b, 11) {
                    int c = scores[i] - a - b;
                    if (c < 0 || c > 10) continue;
                    int diff = max(max(a, b), c) - min(min(a, b), c);
                    if (diff > 2) continue;

                    bool surprises = (diff == 2);
                    bool attains = max(max(a, b), c) >= p;

                    if (surprises && attains) {
                        can_both = true;
                    } else if (surprises) {
                        can_surprise = true;
                    } else if (attains) {
                        can_attain = true;
                    }
                }
            }

            if (can_surprise) {
                cache[i][k] += cache[i+1][k+1];
            }

            if (can_attain) {
                cache[i][k] += cache[i+1][k] + 1;
            }

            if (can_both) {
                cache[i][k] += cache[i+1][k+1] + 1;
            }
        }
    }

    printf("%d\n", cache[0][0]);
}

void solve() {
    scanf("%d %d %d", &n, &s, &p);
    for (int i = 0; i < n; i++) {
        scanf("%d", &scores[i]);
    }

    sort(scores, scores+n);
    int i = 0;
    // printf("%d %d %d\n", n, s, i);
    // reverse(scores+i, scores+n);
    int attain = 0;
    for (; i < n; i++) {
        int score = scores[i];
        // printf("%2.1d -> ", score);

        if (s && score >= 2) {
            s--;
            // score is 3x + 2 or +3 or +4
            score -= 2;
            // now it is 3x + 0 or + 1 or +2
            score /= 3;
            if (score+2 >= p) {
                attain++;
            } else {
                s++;
            }
            // printf("%d\n", score+2);
        } else {
            // score is 3x + 0 or +1 or +2
            score /= 3;
            if (scores[i] % 3) {
                score++;
            }

            if (score >= p) {
                attain++;
            }
            // printf("%d\n", score);
        }
/*
0 0 0   mod 0
0 0 1   mod 1
0 0 2 * mod 2
0 1 1   mod 2
0 1 2 * mod 0
0 2 2 * mod 1
*/
    }

    printf("%d\n", attain);
}

int main() {
    int nt;
    scanf("%d", &nt);
    for (int i = 0; i < nt; i++) {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
