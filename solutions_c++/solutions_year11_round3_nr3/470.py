#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int num[10000];

int gcd(int x, int y)
{
    int temp;
    if (x < y)
    {
        temp = x;
        x = y;
        y = temp;
    }
    while (y != 0)
    {
        temp = x % y;
        x = y;
        y = temp;
    }
    return x;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int T;
    int cases = 1;

    scanf("%d", &T);

    int N, L, H;
    while (T-- > 0)
    {
        scanf("%d %d %d\n", &N, &L, &H);
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &num[i]);
        }

//        int temp, rem;
//
//        if (num[0] == 1)
//        {
//            temp = num[0];
//        }
//        else if (num[1] == 1)
//        {
//            temp = num[1];
//        }
//        else
//        {
//            temp = num[1] / gcd(num[0], num[1]) * num[0];
//        }

        int flag = 0;
        int i, j;
        for (i = L; i <= H; i++)
        {
            for (j = 0; j < N; j++)
            {
                if (i % num[j] != 0 && num[j] % i != 0)
                {
                    break;
                }
            }
            if (j >= N)
            {
                flag = 1;
                break;
            }
        }
        if (i <= H && flag == 1)
        {
            printf("Case #%d: %d\n", cases++, i);
        }
        else
        {
            printf("Case #%d: NO\n", cases++);
        }
    }
    return 0;
}
