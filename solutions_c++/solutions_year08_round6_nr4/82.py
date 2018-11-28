#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool small[8][8];
bool large[8][8];

int main()
{
    int cases;
    cin >> cases;
    for (int cs = 0; cs < cases; ++cs) {
        fill(small[0], small[0] + 64, false);
        fill(large[0], large[0] + 64, false);
        int el, es;
        int N = 0, M = 0;
        cin >> el;
        for (int i = 0; i < el - 1; ++i) {
            int x, y;
            cin >> x >> y;
            N = max(N, max(x, y));
            --x;
            --y;
            large[x][y] = large[y][x] = true;
        }

        cin >> es;
        for (int i = 0; i < es - 1; ++i) {
            int x, y;
            cin >> x >> y;
            M = max(M, max(x, y));
            --x;
            --y;
            small[x][y] = small[y][x] = true;
        }

        bool ans = false;

        if (N >= M) {
            vector<int> repl;
            for (int i = 0; i < N; ++i)
                repl.push_back(i);

            do {
//                 cout << "=================\n";
                bool ok = true;
                for (int i = 0; i < M; ++i)
                    for (int j = i + 1; j < M; ++j) {
                        int p = repl[i];
                        int q = repl[j];
//                         cout << "s " << i << ' ' << j << ": " << small[i][j]
//                              << endl;
//                         cout << "l " << p << ' ' << q << ": " << large[p][q]
//                              << endl;
                        if (small[i][j] && !large[p][q])
                            ok = false;
                    }
                if (ok) {
//                     for (int i = 0; i < N; ++i)
//                         cout << repl[i] << ' ';
//                     cout << endl;
                    ans = true;
                    break;
                }
            } while (next_permutation(repl.begin(), repl.end()));

        }

        cout << "Case #" << cs + 1 << ": ";
        if (ans) cout << "YES\n";
        else cout << "NO\n";
    }

    return 0;
}

