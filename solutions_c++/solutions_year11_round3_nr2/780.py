#include <vector>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

int main ()
{
    int T, L, H, N;
    vector<int> freqs;
    bool harmony;



    cin >> T;
    for (int test = 0; test < T; ++test) {
        printf ("Case #%d: ", test + 1);

        cin >> N;
        cin >> L >> H;
        freqs.assign (N, 0);
        harmony = true;

        for (int i = 0; i < N; ++i) {
            scanf ("%d", &freqs[i]);
        }

        for (int i = L; i < H + 1; ++i) {
            harmony = true;

            for (int j = 0; j < N; ++j) {
                if (freqs[j] % i != 0 && i % freqs[j] != 0 ) {
                    harmony = false;
                    break;
                }
            }

            if (harmony) {
                printf ("%d\n", i);
                break;
            }
        }

        if (!harmony)
            printf ("NO\n");
    }
    return 0;
}
