#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int BufferSize = 1024;

int from[BufferSize*BufferSize];
int to[BufferSize*BufferSize];
int len;
int cases;
int room[BufferSize];
int m, n;
char buf[BufferSize];
int bits[BufferSize];
int aux[100][BufferSize];

bool check(int x)
{
    for (int i = 0; i < n-1; ++i)
    {
        if ((x & (1<<i)) && (x & (1<<i+1)))
            return false;
    }
    return true;
}

bool check(int x, int y)
{
    if (!check(x) || !check(y))
        return false;

    for (int i = 0; i < n; ++i)
    {
        if (y & (1<<i))
        {
            if (i > 0 && (x & (1<<i-1)))
                return false;
            if (i < n-1 && (x & (1<<i+1)))
                return false;
        }
    }
    return true;
}

int main()
{
    scanf("%d", &cases);

    bits[0] = 0;
    for (int i = 1; i < BufferSize; ++i)
        bits[i] = bits[i&(i-1)] + 1;
    
    for (int index = 1; index <= cases; ++index)
    {
        scanf("%d %d", &m, &n);
     
        for (int i = 0; i < m; ++i)
        {
            scanf("%s", buf);
            int s = 0;
            for (int j = 0; j < n; ++j)
            {
                if (buf[j] == 'x')
                    s |= (1 << j);
            }

            room[i] = s;
        }

        len = 0;
        for (int i = 0; i < (1 << n); ++i)
        {
            for (int j = 0; j < (1 << n); ++j)
            {
                if (check(i, j))
                {
                    from[len] = i;
                    to[len] = j;
                    ++len;
                }
            }
        }

        for (int i = 0; i < m; ++i)
            fill_n(aux[i], BufferSize, 0);

        for (int i = 0; i < (1<<n); ++i)
        {
            if (check(i) && (i & room[0]) == 0)
                aux[0][i] = bits[i];
            else
                aux[0][i] = 0;
        }

        for (int i = 0; i < m-1; ++i)
        {
            for (int k = 0; k < len; ++k)
            {
                int f = from[k];
                int t = to[k];

                int count = aux[i][f] + bits[t];

                if ((f & room[i]) == 0 && (t & room[i+1]) == 0 && count > aux[i+1][t])
                    aux[i+1][t] = count;
            }
        }

        int maximum = 0;
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < (1<<n); ++j)
            {
                if (aux[i][j] > maximum)
                    maximum = aux[i][j];
            }
        }

        printf("Case #%d: %d\n", index, maximum);
    }

    return 0;
}
