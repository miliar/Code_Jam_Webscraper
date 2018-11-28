#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

FILE *fin = fopen("make.in", "r");
FILE *fout = fopen("make.out", "w");

long t, d, m, ii, n, a[110], f[110][300], x, ans;

long getabs(long x)
{
     if (x < 0) return -x; else return x;
}

long getmax(long x, long y)
{
     if (x > y) return x; else return y;
}

long getmin(long x, long y)
{
     if (x < y) return x; else return y;
}

int main()
{
    fscanf(fin, "%ld\n", &t);
    for (long z = 1; z <= t; z ++)
    {
        fscanf(fin, "%ld %ld %ld %ld\n", &d, &ii, &m, &n);
        for (long i = 1; i <= n; i ++) fscanf(fin, "%ld", &a[i]);
      //  if (z != 13) continue;
      //  fprintf(fout, "%ld %ld %ld %ld\n", d, ii, m, n);
      //  for (long i = 1; i <= n; i ++) fprintf(fout, "%ld ", a[i]);
        memset(f, 0, sizeof(f));
        for (long i = 1; i <= n; i ++) for (long j = 0; j <= 255; j ++) f[i][j] = -1;
        for (long i = 1; i <= n; i ++)
        {
            for (long j = 0; j <= 255; j++)
            {
                x = getabs(a[i] - j);
                f[i][j] = (i - 1) * d + x;
                for (long k = 1; k < i; k ++)
                    for (long l = 0; l <= 255; l ++)
                    {
                        if (f[k][l] == -1) continue;
                        if (getabs(j - l) <= m)
                           if (f[k][l] + (i - k - 1) * d + x < f[i][j] || f[i][j] == -1)
                              f[i][j] = f[k][l] + (i - k - 1) * d + x; else ;
                        if (m != 0)
                        {
                        if (f[k][l] + ii * ((getabs(j - l) - 1) / m)+ x + (i - k - 1) * d 
                            < f[i][j] || f[i][j] == -1)
                           f[i][j] = f[k][l] + ii * ((getabs(j - l) - 1) / m)+ x + (i - k - 1) * d;
                        }
                    }
                
            }
        }
        ans = -1;
        for (long j = 1; j <= n; j ++)
        for (long i = 0; i <= 255; i ++) 
            if ((f[j][i] != -1) && (f[j][i] + (n - j) * d< ans || ans == -1))
               ans = f[j][i] + (n - j) * d;
        fprintf(fout, "Case #%ld: %ld\n", z, ans);
    }
    fclose(fin);
    fclose(fout);
}
