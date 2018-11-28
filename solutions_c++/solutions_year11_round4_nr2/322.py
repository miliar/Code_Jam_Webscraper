#include <cstring>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cassert>
#include <queue>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

const int N = 600;

int n, m, d;
int z[N][N];
int sum[N][N];

void read()
{
    cin >> n >> m >> d;
    char b[N];
    forn(i, n)
    {
        scanf("%s", b);
        forn(j, m)
            z[i + 1][j + 1] = b[j] - '0';
        //z[i + 1][j + 1] = 0;
    }
}

int re(int x1, int y1, int x2, int y2)
{
    return sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1];
}

void process()
{
    memset(sum, 0, sizeof(sum));

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + z[i][j];

    int result = 0;

    // even
    for (int x = 2; x <= n - 2; x++)
        for (int y = 2; y <= m - 2; y++)
        {
            int lim = min(min(x, n - x), min(y, m - y));
            for (int size = 2; size <= lim; size++)
            {
                long long sx = 0, sy = 0;
                for (int g = 1; g <= size; g++)
                {
                    long long mul = 2 * g - 1;

                    sx += re(x - g + 1, y - size + 1, x - g + 1, y + size) * mul;
                    sx -= re(x + g, y - size + 1, x + g, y + size) * mul;

                    sy += re(x - size + 1, y - g + 1, x + size, y - g + 1) * mul;
                    sy -= re(x - size + 1, y + g, x + size, y + g) * mul;
                }

                sx -= (2 * size - 1) * z[x - size + 1][y - size + 1];
                sx -= (2 * size - 1) * z[x - size + 1][y + size];
                sx += (2 * size - 1) * z[x + size][y - size + 1];
                sx += (2 * size - 1) * z[x + size][y + size];

                sy -= (2 * size - 1) * z[x - size + 1][y - size + 1];
                sy -= (2 * size - 1) * z[x + size][y - size + 1];
                sy += (2 * size - 1) * z[x - size + 1][y + size];
                sy += (2 * size - 1) * z[x + size][y + size];

                if (sx == 0 && sy == 0)
                {
                    //cerr << x << " " << y << " " << size << endl;
                    result = max(result, 2 * size);
                }
            }
        }

    // odd
    for (int x = 1; x <= n - 1; x++)
        for (int y = 1; y <= m - 1; y++)
        {
            int lim = min(min(x - 1, n - x), min(y - 1, m - y));
            for (int size = 1; size <= lim; size++)
            {
                long long sx = 0, sy = 0;
                for (int g = 1; g <= size; g++)
                {
                    long long mul = g;

                    sx += re(x - g, y - size, x - g, y + size) * mul;
                    sx -= re(x + g, y - size, x + g, y + size) * mul;

                    sy += re(x - size, y - g, x + size, y - g) * mul;
                    sy -= re(x - size, y + g, x + size, y + g) * mul;
                }

                sx -= (size) * z[x - size][y - size];
                sx -= (size) * z[x - size][y + size];
                sx += (size) * z[x + size][y - size];
                sx += (size) * z[x + size][y + size];

                sy -= (size) * z[x - size][y - size];
                sy += (size) * z[x - size][y + size];
                sy -= (size) * z[x + size][y - size];
                sy += (size) * z[x + size][y + size];

                if (sx == 0 && sy == 0)
                {
                    //cerr << x << " " << y << " " << size << endl;
                    result = max(result, 2 * size + 1);
                }
            }
        }

    if (result > 0)
        cout << result << endl;
    else
        cout << "IMPOSSIBLE" << endl;
}

int main(int argc, char* argv[])
{
    freopen("input.txt", "rt", stdin);
    
    int cases;
    scanf("%d", &cases);

    int from = (argc > 1 ? atoi(argv[1]) : 1);
    int to = (argc > 2 ? atoi(argv[2]) : cases);

    for (int i = 1; i <= cases; i++)
    {
        read();
        if (from <= i && i <= to)
        {
            printf("Case #%d: ", i);
            process();
        }
    }

    return 0;
}

