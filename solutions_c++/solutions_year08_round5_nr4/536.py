#include <iostream>

using namespace std;

int A[101][101];
int H, W, R;
int zb[2][2] = {{2, 1},{1, 2}};

int main()
{
    int Case;

    freopen("D-small-attempt0.in","r",stdin);
    freopen("Dout.txt","w",stdout);

    cin >> Case;

    for (int ii = 1; ii <= Case; ++ii)
    {
        cin >> H >> W >> R;

        memset(A, 0, sizeof(A));
        for (int j = 1; j <= R; ++j)
        {
            int X, Y;

            cin >> X >> Y;
            A[X][Y] = -1;
        }

        A[1][1] = 1;
        for (int i = 1; i <= H; ++i)
            for (int j = 1; j <= W; ++j)
                if (A[i][j] > 0)
                for (int k = 0; k < 2; ++k)
                {
                    int XX = i + zb[k][0];
                    int YY = j + zb[k][1];

                    if (XX >= 1 && XX <= H && YY >= 1 && YY <= W && A[XX][YY] != -1)
                        A[XX][YY] = (A[i][j] + A[XX][YY]) % 10007;
                }
        printf("Case #%d: %d\n", ii, A[H][W]);
    }
}
