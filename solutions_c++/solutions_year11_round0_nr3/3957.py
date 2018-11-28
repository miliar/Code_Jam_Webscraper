#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    int t, n;
    int mk[15];
    int opt = 0;
    int p[15];
    FILE *fin = fopen("B.in", "r");
    FILE *fout = fopen("B.out", "w");
    fscanf(fin, "%d", &t);
    for (int idx = 0; idx < t; idx++)
    {
        fscanf(fin, "%d", &n);
        for (int i = 0; i < n; i++)
            fscanf(fin, "%d", &p[i]);
        for (int i = 0; i < n; i++)
            fprintf(fin, "%d\n", p[i]);
        opt = -1;
        for (int x = 1; x < (1<<n); x++)
        {
            memset(mk, 0, sizeof(mk));
            int tmp = x;
            int k = 0;
            while (tmp)
            {
                mk[k++] = tmp%2;
                tmp /= 2;
            }
            int sum1 = 0;
            int sum2 = 0;
            int t = 0;
            for (int i = 0; i < n; i++)
            {
                if (mk[i] == 1)
                {
                    sum1 ^= p[i];
                    t += p[i];
                }
                else
                    sum2 ^= p[i];
            }
            if (sum1 > 0 && sum2 > 0 && sum1 == sum2 && t > opt)
                opt = t;
        }
        if (opt < 0)
            fprintf(fout, "Case #%d: NO\n", idx+1);
        else
            fprintf(fout, "Case #%d: %d\n", idx+1, opt);
    }
    return 0;
}

