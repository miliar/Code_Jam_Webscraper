#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

FILE *fin = fopen("rotate.in", "r");
FILE *fout = fopen("rotate.out", "w");

long t, n, k, l, r, b, x, y;
bool fr, fb;
char g[100][100], p;

int main()
{
    fscanf(fin, "%ld\n", &t);
    for (long z = 1; z <= t; z ++)
    {
       // if (z != 65) continue;
        fr = false; fb = false;
        fscanf(fin, "%ld %ld\n", &n, &k);
        for (long i = 0; i < n; i ++)
        {
            fscanf(fin, "%s", g[i]);
            fscanf(fin, "\n");
        }        
        for (long i = 0; i < n; i ++)
            for (long j = n - 1; j >= 0; j --)
            {
                if (g[i][j] == '.') continue;
                l = j + 1;
                while (l < n && g[i][l] == '.') l ++;
                l --;
                if (l != j) {g[i][l] = g[i][j]; g[i][j] = '.';}
            } 
        for (long i = 0; i < n; i ++)
        {
            r = 0; b = 0; p = '.';
            for (long j = 0; j < n; j ++)
            {
                if (g[i][j] == 'R') 
                {
                   b = 0; r ++;
                }
                if (g[i][j] == 'B')
                {
                   r = 0; b++;
                }
                if (g[i][j] == '.')
                {
                   r = 0; b = 0;
                }
                if (r >= k) fr = true;
                if (b >= k) fb = true;
            } 
        }
        for (long i = 0; i < n; i ++)
        {
            r = 0; b = 0; p = '.';
            for (long j = 0; j < n; j ++)
            {
                if (g[j][i] == 'R') 
                {
                   b = 0; r ++;
                }
                if (g[j][i] == 'B')
                {
                   r = 0; b++;
                }
                if (g[j][i] == '.')
                {
                   r = 0; b = 0;
                }
                if (r >= k) fr = true;
                if (b >= k) fb = true;
            } 
        }
        for (long i = 0; i < n; i ++)
        {
            x = 0; y = i; r = 0; b = 0;
            while (x < n && y >= 0)
            {
                  if (g[x][y] == 'R') 
                  {
                      b = 0; r ++;
                  }
                  if (g[x][y] == 'B')
                  {
                     r = 0; b++;
                  }
                  if (g[x][y] == '.')
                  {
                     r = 0; b = 0;
                  }
                  if (r >= k) fr = true;
                  if (b >= k) fb = true;
                  y --; x ++;
            }
            x = 0; y = i; r = 0; b = 0;
            while (x < n && y < n)
            {
                  if (g[x][y] == 'R') 
                  {
                      b = 0; r ++;
                  }
                  if (g[x][y] == 'B')
                  {
                     r = 0; b++;
                  }
                  if (g[x][y] == '.')
                  {
                     r = 0; b = 0;
                  }
                  if (r >= k) fr = true;
                  if (b >= k) fb = true;
                  y ++; x ++;
            }
            x = n - 1; y = i; r = 0; b = 0;
            while (x >= 0 && y >= 0)
            {
                  if (g[x][y] == 'R') 
                  {
                      b = 0; r ++;
                  }
                  if (g[x][y] == 'B')
                  {
                     r = 0; b++;
                  }
                  if (g[x][y] == '.')
                  {
                     r = 0; b = 0;
                  }
                  if (r >= k) fr = true;
                  if (b >= k) fb = true;
                  y --; x --;
            }
            x = n - 1; y = i; r = 0; b = 0;
            while (y < n && x >= 0)
            {
                  if (g[x][y] == 'R') 
                  {
                      b = 0; r ++;
                  }
                  if (g[x][y] == 'B')
                  {
                     r = 0; b++;
                  }
                  if (g[x][y] == '.')
                  {
                     r = 0; b = 0;
                  }
                  if (r >= k) fr = true;
                  if (b >= k) fb = true;
                  x --; y ++;
            }
        }
        fprintf(fout, "Case #%ld: ", z);
        if (fr && fb) {fprintf(fout, "Both\n"); continue;}
        if (!fr && !fb) {fprintf(fout, "Neither\n"); continue;}
        if (fr) fprintf(fout, "Red\n"); else fprintf(fout, "Blue\n");
    }
    fclose(fin);
    fclose(fout);
}
