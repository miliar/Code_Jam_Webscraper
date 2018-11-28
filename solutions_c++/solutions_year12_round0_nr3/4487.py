#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BIT_LEN 10

int T;
int n, m;

int Bit(int num)
{
    int bit = 0;
    while(num)
    {
        num /= 10;
        bit++;
    }
    return bit;
}

bool Judge(int a, int b)
{
    int ba = Bit(a);
    int bb = Bit(b);
    int ta = a;
    int tb = b;
    if(ba != bb)
        return 0;

    int temp[2][MAX_BIT_LEN];
    for(int i = 0; i < 2; ++i)
        for(int j = 0; j < ba; ++j)
        {
            if(i == 0)
            {
                temp[i][j] = ta % 10;
                ta /= 10;
            }
            else
            {
                temp[i][j] = tb % 10;
                tb /= 10;
            }
        }
    for(int i = 0; i < ba; ++i)
    {
        int count = 0;
        for(int j = 0; j < ba; ++j)
            if(temp[0][j] != temp[1][(j+i)%ba])
                break;
            else
                count++;
        if(count == ba)
        {
            //printf("%d %d  ", a, b);
            return 1;
        }
    }
    return 0;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for(int i = 0; i < T; ++i)
    {
        int count = 0;
        scanf("%d %d", &n, &m);
        for(int j = n; j < m; ++j)
            for(int k = j + 1; k <= m; ++k)
                if(Judge(j, k)) count++;

        printf("Case #%d: %d\n", i + 1, count);
    }
    return 0;
}
