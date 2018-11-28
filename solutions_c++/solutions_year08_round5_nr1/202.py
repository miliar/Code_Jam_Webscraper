#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int North = 0;
const int East = 1;
const int South = 2;
const int West = 3;
const int BufferSize = 1000;

int offset[][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

int hori[BufferSize][BufferSize];
int vert[BufferSize][BufferSize];
int r[BufferSize][BufferSize];
int aux[BufferSize][BufferSize];
int cases;
int n;
char s[BufferSize];
int t;
int x, y;
int d;

int process(char *s)
{
    for (int i = 0; s[i]; ++i)
    {
        if (s[i] == 'L')
        {
            d = (d + 3)%4;
        }
        else if (s[i] == 'R')
        {
            d = (d + 1) % 4;
        }
        else
        {
            int _x = x;
            int _y = y;

            x += offset[d][0];
            y += offset[d][1];

            if (d == North)
            {
                vert[_x][_y] = 1;
            }
            else if (d == East)
            {
                hori[_x][_y] = 1;
            }
            else if (d == South)
            {
                vert[x][y] = 1;
            }
            else if (d == West)
            {
                hori[x][y] = 1;
            }
        }
    }

    return 0;
}

int main()
{
    scanf("%d", &cases);

    for (int index = 1; index <= cases; ++index)
    {
        fill_n(&hori[0][0], BufferSize*BufferSize, 0);
        fill_n(&vert[0][0], BufferSize*BufferSize, 0);
        fill_n(&aux[0][0], BufferSize*BufferSize, 0);
        fill_n(&r[0][0], BufferSize*BufferSize, 0);

        x = BufferSize/2;
        y = BufferSize/2;
        d = 0;

        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            scanf("%s %d", s, &t);

            for (int k = 0; k < t; ++k)
                process(s);
        }

        for (int i = 0; i < BufferSize; ++i)
        {
            int f = 0;
             while (f < BufferSize && hori[i][f] == 0)
                 ++f;

            int t = BufferSize;
             while (t > f && hori[i][t] == 0)
                 --t;

            int sum = 0;
            for (int j = f; j < t; ++j)
            {
                sum ^= hori[i][j];

                if (sum)
                {
                    aux[i][j] = 1;
                }
                else if (aux[i][j] != 1)
                {
                    aux[i][j] = 2;
                }
            }
        }

        for (int i = 0; i < BufferSize; ++i)
        {
            int f = 0;
             while (f < BufferSize && vert[f][i] == 0)
                 ++f;

            int t = BufferSize;
             while (t > f && vert[t][i] == 0)
                 --t;

            int sum = 0;
            for (int j = f; j < t; ++j)
            {
                sum ^= vert[j][i];

                if (sum)
                {
                    aux[j][i] = 1;
                }
                else if (aux[j][i]  != 1)
                {
                   aux[j][i]   = 2;
                }
            }
        }

        int total = 0;
        for (int i = 0; i < BufferSize; ++i)
        {
            for (int j = 0; j < BufferSize; ++j)
            {
                if (aux[i][j] == 2)
                    ++total;
            }
        }

        printf("Case #%d: %d\n", index, total);
    }

    return 0;
}
