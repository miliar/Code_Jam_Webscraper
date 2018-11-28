#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

#define MAXRC 100

typedef pair<int, int> pii;

static int alt[MAXRC][MAXRC];
static pii sink[MAXRC][MAXRC];
static char label[MAXRC][MAXRC];

static int R, C;

static pii get_sink(int i, int j)
{
    static const int dr[4] = {-1, 0, 0, 1};
    static const int dc[4] = {0, -1, 1, 0};

    if (sink[i][j].first == -1)
    {
        int best = alt[i][j];
        pii best_sink(i, j);
        for (int d = 0; d < 4; d++)
        {
            int i2 = i + dr[d];
            int j2 = j + dc[d];
            if (i2 >= 0 && i2 < R && j2 >= 0 && j2 < C && alt[i2][j2] < best)
            {
                best = alt[i2][j2];
                best_sink = pii(i2, j2);
            }
        }
        if (best < alt[i][j])
            sink[i][j] = get_sink(best_sink.first, best_sink.second);
        else
            sink[i][j] = best_sink;
    }
    return sink[i][j];
}

static void solve()
{
    cin >> R >> C;
    assert(R <= MAXRC && C <= MAXRC);
    char next_label = 'a';

    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
        {
            cin >> alt[i][j];
            sink[i][j] = pii(-1, -1);
            label[i][j] = '\0';
        }

    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
        {
            pii s = get_sink(i, j);
            if (!label[i][j])
            {
                if (!label[s.first][s.second])
                {
                    label[s.first][s.second] = next_label++;
                }
                label[i][j] = label[s.first][s.second];
            }
            cout << label[i][j];
            cout << (j == C - 1 ? '\n' : ' ');
        }
}

int main()
{
    int N;

    cin >> N;
    for (int cas = 1; cas <= N; cas++)
    {
        cout << "Case #" << cas << ":\n";
        solve();
    }
    return 0;
}
