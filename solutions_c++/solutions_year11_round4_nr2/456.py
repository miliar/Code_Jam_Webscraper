#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 500 + 10;

int R, C, D, T;
long long vx[MAXN][MAXN], vy[MAXN][MAXN];
long long sx[MAXN][MAXN], sy[MAXN][MAXN];
long long v[MAXN][MAXN], sv[MAXN][MAXN];

void Init ()
{
    scanf ("%d%d%d", &R, &C, &D);
    char line[1000];

    for (int i = 1; i <= R; i++) {
        scanf ("%s", line);

        for (int j = 1; j <= C; j++) {
            int x = i * 2 - 1;
            int y = j * 2 - 1;


            v[i][j] = (line[j - 1] - '0') + D;
            vx[i][j] = x * v[i][j];
            vy[i][j] = y * v[i][j];

            sx[i][j] = sx[i - 1][j] + sx[i][j - 1] - sx[i - 1][j - 1] + vx[i][j];
            sy[i][j] = sy[i - 1][j] + sy[i][j - 1] - sy[i - 1][j - 1] + vy[i][j];
            sv[i][j] = sv[i - 1][j] + sv[i][j - 1] - sv[i - 1][j - 1] + v[i][j];
        }
        //printf ("\n");
    }
}

long long getsum (long long sum[MAXN][MAXN], int x0, int y0, int x1, int y1)
{
    return sum[x1][y1] - sum[x0 - 1][y1] - sum[x1][y0 - 1] + sum[x0 - 1][y0 - 1];
}

void update (long long &_sv, long long &_sx, long long &_sy, int x, int y)
{
    _sv -= v[x][y];
    _sx -= vx[x][y];
    _sy -= vy[x][y];
}


void getgv (long long &mx, long long &my, int x0, int y0, int x1, int y1)
{
    mx = (x0 * 2 + x1 * 2 - 2) / 2;
    my = (y0 * 2 + y1 * 2 - 2) / 2;
}

int checkS (int x0, int y0, int x1, int y1)
{
    long long _sv = getsum (sv, x0, y0, x1, y1);
    long long _sx = getsum (sx, x0, y0, x1, y1);
    long long _sy = getsum (sy, x0, y0, x1, y1);

    update (_sv, _sx, _sy, x0, y0);
    update (_sv, _sx, _sy, x0, y1);
    update (_sv, _sx, _sy, x1, y0);
    update (_sv, _sx, _sy, x1, y1);

    long long _mx, _my;

    getgv (_mx, _my, x0, y0, x1, y1);

    return (_mx * _sv == _sx) && (_my * _sv == _sy); 
}

int check (int L)
{
    for (int i = 1; i <= R - L + 1; i ++)
        for (int j = 1; j <= C - L + 1; j++)
            if (checkS (i, j, i + L - 1, j + L - 1)) return 1;

    return 0;
}

void Solve ()
{
    int max = R < C ? R : C;

    for (int k = max; k >= 3; k--) {
        if (check (k)) {
            printf ("%d\n", k);
            return;
        }
    }

    printf ("IMPOSSIBLE\n");
}

int main ()
{
    //freopen ("in.txt", "r", stdin);

    scanf ("%d", &T);
    for (int i = 1;i <= T; i++) {

        printf ("Case #%d: ", i);

        Init ();

        Solve ();

    }
    return 0;
}


