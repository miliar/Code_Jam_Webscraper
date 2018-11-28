#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int BufferSize = 128;

int h, w;
int rock[BufferSize][BufferSize];
int aux[BufferSize][BufferSize];
int cases;
int r;
int offset[][2] = { {1, 2}, {2, 1} };

int main()
{
    scanf("%d", &cases);

    for (int index = 1; index <= cases; ++index)
    {
        scanf("%d %d %d", &h, &w, &r);

        fill_n(&rock[0][0], BufferSize*BufferSize, 0);
        fill_n(&aux[0][0], BufferSize*BufferSize, 0);

        for (int i = 0; i < r; ++i)
        {
            int x, y;
            scanf("%d %d", &x, &y);
            --x;
            --y;
            rock[x][y] = 1;
        }

        aux[0][0] = 1;
        for (int i = 0; i < h; ++i)
        {
            for (int j = 0; j < w; ++j)
            {
                aux[i][j] %= 10007;
                for (int k = 0; k < 2; ++k)
                {
                    int x = i + offset[k][0];
                    int y = j + offset[k][1];

                    if (rock[x][y] != 1)
                       aux[x][y] += aux[i][j];
                }
            }
        }

        printf("Case #%d: %d\n", index, aux[h-1][w-1]);
    }

    return 0;
}
