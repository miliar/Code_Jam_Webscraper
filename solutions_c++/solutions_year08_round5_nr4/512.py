
#include <cstdio>
#include <cstring>
using namespace std;

const int MOD = 10007;

int am [128][128][128];
bool bad [128][128];

int N, H, W, R;

const int dx [] = {1, 2};
const int dy [] = {2, 1};

int main ()
{
    scanf ("%d", &N);
    for (int t = 1; t <= N; ++t)
    {
        memset (am, 0, sizeof (am));
        memset (bad, 0, sizeof (bad));
        scanf ("%d %d %d", &H, &W, &R);
        for (int i = 0; i < R; ++i)
        {
            int x, y;
            scanf ("%d %d", &x, &y);
            bad [x][y] = true; //!
        }
        
        am [0][1][1] = 1;
        for (int m = 0; m < 128; ++m)
            for (int i = 1; i <= H; ++i)
                for (int j = 1; j <= W; ++j)
                    if (!bad [i][j] && am [m][i][j] > 0)
                        for (int k = 0; k < 2; ++k)
                        {
                            int ni = i + dx [k];
                            int nj = j + dy [k];
                            if (ni <= H && nj <= W && !bad [ni][nj])
                                (am [m + 1][ni][nj] += am [m][i][j]) %= MOD;
                        }
        int res = 0;
        for (int i = 0; i < 128; ++i)
            (res += am [i][H][W]) %= MOD;
        printf ("Case #%d: %d\n", t, res); 
    }
    return 0;
}
