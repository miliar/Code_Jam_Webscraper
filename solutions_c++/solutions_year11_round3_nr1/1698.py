/* 
 * File:   main.cpp
 * Author: Stefan
 *
 * Created on May 7, 2011, 8:27 PM
 */

#include <cstdlib>
#include <cstdio>

#define NMAX 50

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    FILE *fin = fopen("date.in", "rt");
    FILE *fout = fopen("date.out", "wt");
    int i, j, t, k, n, m, ok;
    char a[NMAX][NMAX];
    fscanf(fin, "%d", &t);
    for (k = 1; k <= t; k++)
    {
        ok = 1;
        fscanf(fin, "%d %d", &m, &n);
        for (i = 0; i < m; i++)
        {
            fgetc(fin);
            for (j = 0; j < n; j++)
                fscanf(fin, "%c", &(a[i][j]));
            
        }
        for (i = 0; i < m-1; i++)
            for (j = 0; j < n-1; j++)
                if (a[i][j] == '#')
                {
                    if (a[i][j+1] != '#')
                    {
                        ok = 0;
                        break;
                    }
                    if (a[i+1][j+1] != '#')
                    {
                        ok = 0;
                        break;
                    }
                    if (a[i+1][j] != '#')
                    {
                        ok = 0;
                        break;
                    }
                    a[i][j] = '/';
                    a[i][j+1] = '\\';
                    a[i+1][j] = '\\';
                    a[i+1][j+1] = '/';
                }
        if (ok)
        {
            for (i = 0; i < n; i++)
                if (a[m-1][i] == '#')
                {
                    ok = 0;
                    break;
                }

            if (ok)
                for (i = 0; i < m; i++)
                    if (a[i][n-1] == '#')
                    {
                        ok = 0;
                        break;
                    }
        }
        fprintf(fout, "Case #%d:\n", k);
        if (!ok) fprintf(fout, "Impossible\n");
        else
            for (i = 0; i < m; i++)
            {
                for (j = 0; j < n; j++) fprintf(fout, "%c", a[i][j]);
                fprintf(fout, "\n");
            }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}

