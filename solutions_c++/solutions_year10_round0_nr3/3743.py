#include <iostream>
using namespace std;

int main()
{
    long long t, r, k, n, a[1002], cnt, p, c, s, sum;
    FILE *in, *out;
    in = fopen("C-small-attempt00.in", "r");
    out = fopen("C-small-attempt00.out", "w");

    fscanf(in, "%lld", &t);
    for (int i = 1; i <= t; i++)
    {
        sum = 0;
        cnt = 0;
        p = 0;

        fscanf(in, "%lld %lld %lld", &r, &k, &n);
        for (int j = 0; j < n; j++)
        {
            fscanf(in, "%lld", &a[j]);
            sum += a[j];
        }

        if (sum <= k)
            cnt = r * sum;
        else
        {
            for (c = 1; c <= r; c++)
            {
                s = 0;
                for (int j = p; ; j = (j + 1) % n)
                {
                    s += a[j];
                    if ((j + 1) % n == p || s + a[(j + 1) % n] > k)
                    {
                        cnt += s;
                        p = (j + 1) % n;
                        break;
                    }
                }
                if (!p || c == r)
                    break;
            }
            cnt = (r / c) * cnt;
            r = r % c;
            p = 0;
            while (r--)
            {
                s = 0;
                for (int j = p; ; j = (j + 1) % n)
                {
                    s += a[j];
                    if ((j + 1) % n == p || s + a[(j + 1) % n] > k)
                    {
                        cnt += s;
                        p = (j + 1) % n;
                        break;
                    }
                }
            }
        }

        fprintf(out, "Case #%d: %lld\n", i, cnt);
    }

    return 0;
}

