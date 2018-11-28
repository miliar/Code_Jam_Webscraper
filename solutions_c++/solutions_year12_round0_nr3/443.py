#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

const int ten[] = {
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000
};

inline int right_shift(int a, int t, int d)
{
    if (a % ten[t] == 0)
        return 0;
    return (a / ten[t]) + (a % ten[t]) * (ten[d - t]);
}

inline int get_digits(int a)
{
    int result = 0;
    while (a)
        a /= 10, ++result;
    return result;
}

int occur[2012414];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T, a, b, i, t, d, r;

    scanf("%d", &T);
    for (int cs = 1; cs <= T; ++cs)
    {
        memset(occur, 0, sizeof occur);

        long long result = 0;
        scanf("%d %d", &a, &b);
        for (i = a; i <= b; ++i)
        {
            d = get_digits(i);
            for (t = 1; t < d; ++t)
            {
                r = right_shift(i, t, d);
                if (r > i && r <= b && get_digits(r) == d && occur[r] < i)
                    ++result, occur[r] = i;
            }
        }

        printf("Case #%d: %lld\n", cs, result);
    }

    return 0;
}
