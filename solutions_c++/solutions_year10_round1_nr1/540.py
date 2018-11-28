#include <cstdio>
#include <cstring>

int n;
char init[60][60], final[60][60];

int main()
{
    FILE *input = fopen("Alarge.in", "r");
    FILE *output = fopen("Alarge.out", "w");
    int t, ca = 0, i, j, w, v, k, count;
    bool Rok, Bok;
    fscanf(input, "%d", &t);
    while (t > 0)
    {
        fscanf(input, "%d%d\n", &n, &k);
        for (i = 0; i < n; i++) fgets(init[i], 60, input);
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++) final[i][j] = '.';
        }
        for (i = 0; i < n; i++)
        {
            w = n - 1;
            for (j = n - 1; j >= 0; j--) if (init[i][j]!='.')
            {
                final[w--][n - 1 - i] = init[i][j];
            }
        }
        Rok = Bok = false;
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++) if (final[i][j]!='.')
            {
                if (final[i][j] == 'R' && !Rok)
                {
                    w = j; count = 0;
                    while (w < n && final[i][w] == 'R' && count < k)
                    {
                        count++;
                        w++;
                    }
                    if (count >= k)    Rok = true;
                    w = i; count = 0;
                    while (w < n && final[w][j] == 'R' && count < k)
                    {
                        count++;
                        w++;
                    }
                    if (count >= k)    Rok = true;
                    w = i; v = j; count = 0;
                    while (w < n && v < n && final[w][v] == 'R' && count < k)
                    {
                        count++;
                        w++; v++;
                    }
                    if (count >= k)    Rok = true;
                    w = i; v = j; count = 0;
                    while (w < n && v >= 0 && final[w][v] == 'R' && count < k)
                    {
                        count++;
                        w++; v--;
                    }
                    if (count >= k)    Rok = true;
                }
                else if (final[i][j] == 'B' && !Bok)
                {
                    w = j; count = 0;
                    while (w < n && final[i][w] == 'B' && count < k)
                    {
                        count++;
                        w++;
                    }
                    if (count >= k)    Bok = true;
                    w = i; count = 0;
                    while (w < n && final[w][j] == 'B' && count < k)
                    {
                        count++;
                        w++;
                    }
                    if (count >= k)    Bok = true;
                    w = i; v = j; count = 0;
                    while (w < n && v < n && final[w][v] == 'B' && count < k)
                    {
                        count++;
                        w++; v++;
                    }
                    if (count >= k)    Bok = true;
                    w = i; v = j; count = 0;
                    while (w < n && v >= 0 && final[w][v] == 'B' && count < k)
                    {
                        count++;
                        w++; v--;
                    }
                    if (count >= k)    Bok = true;
                }
            }
        }
        fprintf(output, "Case #%d: ", ++ca);
        if (Rok && Bok) fprintf(output, "Both\n");
        else if (Rok) fprintf(output, "Red\n");
        else if (Bok) fprintf(output, "Blue\n");
        else fprintf(output, "Neither\n");
        t--;
    }
}
