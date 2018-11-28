#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int fact[][2] =
{
    {0, -4},
    {1, 6},
};

void mul(int a[2][2], int b[2][2], int c[2][2]);
void assign(int a[2][2], int b[2][2]);

int n;

int main()
{
    int t;
    scanf("%d", &t);

    for (int index = 1; index <= t; ++index)
    {
        scanf("%d", &n);

        int m = n-1;
        int d[2][2] = { {0, -4}, {1, 6} };
        int r[2][2] = { {1, 0}, {0, 1} };
        int tmp[2][2];

        for (int i = 0; i < 32; ++i)
        {
            if ((1<<i) & m)
            {
                mul(r, d, tmp);
                assign(tmp, r);
            }

            mul(d, d, tmp);
            assign(tmp, d);
        }
            
        int result = ((6*r[1][1] + 2*r[0][1]) % 1000 + 999) % 1000;
        printf("Case #%d: %03d\n", index, result);
    }

    return 0;
}

void mul(int a[2][2], int b[2][2], int c[2][2])
{
    for (int i = 0; i < 2; ++i)
    {
        for (int j = 0; j < 2; ++j)
        {
            c[i][j] = 0;
            for (int k = 0; k < 2;++k)
            {
                c[i][j] += a[i][k]*b[k][j];
            }
            c[i][j] %= 1000;
        }
    }
}

void assign(int a[2][2], int b[2][2])
{
    for (int i = 0; i < 2; ++i)
    {
        for (int j = 0; j < 2; ++j)
        {
            b[i][j] = a[i][j];
        }
    }
}
