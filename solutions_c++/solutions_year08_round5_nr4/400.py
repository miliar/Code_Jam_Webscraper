#include <iostream>

using namespace std;

const int MOD = 10007;

int H, W, R;
int col[100], row[100];
int d[200][200];

bool rock(int i, int j)
{
    for (int k=0; k < R; k++)
        if (row[k] == i && col[k] == j)
            return true;

    return false;
}

int solve()
{
    memset(d, 0, sizeof(d));

    d[0][0] = 1;

    for (int i=1; i < H; i++)
        for (int j=1; j < W; j++)
            if (!rock(i, j))
            {
                for (int di=-3; di < 0; di++)
                    for (int dj=-3; dj < 0; dj++)
                        if (di*di + dj*dj == 5 && i + di >= 0 && j + dj >= 0)
                            d[i][j] = (d[i][j] + d[i+di][j+dj])%MOD;
//                cout << i << " " << j << ": " << d[i][j]  << endl;
            }

    return d[H-1][W-1];
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T;
    cin >> T;
    for (int tt=1; tt <= T; tt++)
    {
        cin >> H >> W >> R;

        for (int i=0; i < R; i++)
        {
            cin >> row[i] >> col[i];
            row[i]--;
            col[i]--;
        }

        cout << "Case #" << tt << ": " << solve() << endl;
    }

    return 0;
}
