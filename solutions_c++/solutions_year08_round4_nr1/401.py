#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int BufferSize = 100000;
const int MaxNum = 1000000000;

int change[BufferSize];
int is_gate[BufferSize];
int value[BufferSize];
int minimum[BufferSize][2];
int cases;
int n, v;

void cheat(int x);
int evaluate(int op, int x, int y);

int main()
{
    scanf("%d", &cases);

    for (int index = 1; index <= cases; ++index)
    {
        scanf("%d %d", &n, &v);

        for (int i = 0; i < (n-1)/2; ++i)
        {
            is_gate[i] = true;
            scanf("%d %d", &value[i], &change[i]);
        }

        for (int i = (n-1)/2; i < n; ++i)
        {
            is_gate[i] = false;
            scanf("%d", &value[i]);
        }

        cheat(0);

        if (minimum[0][v] == MaxNum)
            printf("Case #%d: IMPOSSIBLE\n", index);
        else
            printf("Case #%d: %d\n", index, minimum[0][v]);
    }

    return 0;
}

void cheat(int x)
{
    if (is_gate[x])
    {
        cheat(2*x + 1);
        cheat(2*x + 2);

        minimum[x][0] = minimum[x][1] = MaxNum;

        for (int i = 0; i < 2; ++i)
        {
            for (int j = 0; j < 2; ++j)
            {
                int result = evaluate(value[x], i, j);
                int count = minimum[2*x+1][i] + minimum[2*x+2][j];

                if (count < minimum[x][result])
                    minimum[x][result] = count;
                
                if (change[x])
                {
                    result = evaluate(value[x]^1, i, j);
                    count = minimum[2*x+1][i] + minimum[2*x+2][j] + 1;

                    if (count < minimum[x][result])
                        minimum[x][result] = count;
                }
            }
        }
    }
    else
    {
        minimum[x][0] = minimum[x][1] = MaxNum;
        minimum[x][value[x]] = 0;
    }
}

int evaluate(int op, int x, int y)
{
    if (op == 0)
    {
        return x || y;
    }
    else
    {
        return x && y;
    }
}