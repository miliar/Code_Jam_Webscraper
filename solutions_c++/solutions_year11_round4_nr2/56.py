#include <cstdio>
#include <complex>
#include <algorithm>
using namespace std;

const int MAX = 505;

int R, C, D;
char grid [MAX][MAX];
int grid_psum [MAX][MAX];
complex <int> center_psum [MAX][MAX];

inline complex <int> get_vector (int r, int c)
{
    return (int) grid [r][c] * complex <int> (r, c);
}

inline int grid_sum (int r, int c, int k)
{
    return grid_psum [r + k][c + k] - grid_psum [r][c + k] - grid_psum [r + k][c] + grid_psum [r][c] - grid [r][c] - grid [r][c + k - 1] - grid [r + k - 1][c] - grid [r + k - 1][c + k - 1];
}

inline complex <int> center_sum (int r, int c, int k)
{
    return center_psum [r + k][c + k] - center_psum [r][c + k] - center_psum [r + k][c] + center_psum [r][c] - get_vector (r, c) - get_vector (r, c + k - 1) - get_vector (r + k - 1, c) - get_vector (r + k - 1, c + k - 1);
}

void solve_case ()
{
    scanf ("%d %d %d", &R, &C, &D);

    for (int i = 0; i < R; i++)
    {
        scanf ("%s", grid [i]);

        for (int j = 0; j < C; j++)
        {
            grid [i][j] -= '0';
            grid_psum [i + 1][j + 1] = grid_psum [i][j + 1] + grid_psum [i + 1][j] - grid_psum [i][j] + grid [i][j];
            center_psum [i + 1][j + 1] = center_psum [i][j + 1] + center_psum [i + 1][j] - center_psum [i][j] + get_vector (i, j);
        }
    }

    for (int k = min (R, C); k >= 3; k--)
        for (int i = 0; i + k <= R; i++)
            for (int j = 0; j + k <= C; j++)
            {
                int gsum = grid_sum (i, j, k);
                complex <int> csum = center_sum (i, j, k);

                if (2 * csum == gsum * complex <int> (2 * i + k - 1, 2 * j + k - 1))
                {
                    printf ("%d\n", k);
                    return;
                }
            }

    puts ("IMPOSSIBLE");
}

int main ()
{
    int T; scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        printf ("Case #%d: ", tc);
        solve_case ();
    }

    return 0;
}
