#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 500;

int R, C, D;
int W[MAX + 1][MAX + 1];

int H[MAX + 1][MAX + 1];
int V[MAX + 1][MAX + 1]; 

void precalc()
{
    for (int i = 1; i <= R; i++) {
        H[i][0] = 0;
        for (int j = 1; j <= C; j++)
            H[i][j] = H[i][j - 1] + W[i][j];
    }
    for (int j = 1; j <= C; j++) {
        V[0][j] = 0;
        for (int i = 1; i <= R; i++)
            V[i][j] = V[i - 1][j] + W[i][j];
    }
}

inline int rowWeight(int row, int from, int to)
{
    return H[row][to] - H[row][from - 1];
}

inline int colWeight(int col, int from, int to)
{
    return V[to][col] - V[from - 1][col];
}

bool isBalanced(int K, int x, int y) // top left corner
{
    int left = x;
    int right = x + K - 1;
    int top = y;
    int bottom = y + K - 1;
    int cx = x + K / 2;
    int cy = y + K / 2;
    int hbalance = 0, vbalance = 0;
    if (K % 2 == 0) {
        for (int i = 1, w = 1; i <= K / 2; i++, w += 2)
            hbalance += w * colWeight(cx - i, top, bottom);
        for (int i = 0, w = 1; i  < K / 2; i++, w += 2)
            hbalance -= w * colWeight(cx + i, top, bottom);
        hbalance -= (K - 1) * 
            (W[top][left] + W[bottom][left] - W[top][right] - W[bottom][right]);

        for (int i = 1, w = 1; i <= K / 2; i++, w += 2)
            vbalance += w * rowWeight(cy - i, left, right);
        for (int i = 0, w = 1; i  < K / 2; i++, w += 2)
            vbalance -= w * rowWeight(cy + i, left, right);
        vbalance -= (K - 1) * 
            (W[top][left] + W[top][right] - W[bottom][left] - W[bottom][right]);
    }
    else {
        for (int i = 1; i <= K / 2; i++) {
            hbalance += i * colWeight(cx - i, top, bottom)
                      - i * colWeight(cx + i, top, bottom);
        }
        hbalance -= K / 2 * 
            (W[top][left] + W[bottom][left] - W[top][right] - W[bottom][right]);

        for (int i = 1; i <= K / 2; i++) {
            vbalance += i * rowWeight(cy - i, left, right)
                      - i * rowWeight(cy + i, left, right);
        }
        vbalance -= K / 2 * 
            (W[top][left] + W[top][right] - W[bottom][left] - W[bottom][right]);
        /*
        if (K == 5 && x == 2 && y == 2) {
            cout << "corners = " << corners << endl;
            cout << "hbalance = " << hbalance << endl;
            cout << "vbalance = " << vbalance << endl;
        }
        */
    }
    return (hbalance == 0 && vbalance == 0);
}

int solve()
{
    cin >> R >> C >> D;
    for (int i = 1; i <= R; i++)
        for (int j = 1; j <= C; j++) {
            char c; cin >> c;
            W[i][j] = c - '0';
        }

    /*
    cout << endl;
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            cout << W[i][j];
        }
        cout << endl;
    }
    */
    precalc();

    for (int K = min(R, C); K >= 3; K--) {
        for (int x = 1; x + K - 1 <= C; x++)
            for (int y = 1; y + K - 1 <= R; y++)
                if (isBalanced(K, x, y))
                    return K;
    }

    return 0;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cerr << t << endl;
        int answer = solve();
        if (answer)
            cout << "Case #" << t << ": " << answer << endl;
        else
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
}
