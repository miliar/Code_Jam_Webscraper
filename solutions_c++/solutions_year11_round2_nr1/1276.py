/* 
 * File:   main.cpp
 * Author: Stefan
 *
 * Created on May 7, 2011, 8:27 PM
 */

#include <cstdlib>
#include <cstdio>

#define NMAX 100

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    FILE *fin = fopen("date.in", "rt");
    FILE *fout = fopen("date.out", "wt");
    double wp[NMAX], owp[NMAX], oowp[NMAX];
    char m[NMAX][NMAX];
    int i, j, t, k, n, nr[NMAX];
    fscanf(fin, "%d", &t);
    for (k = 1; k <= t; k++)
    {
        fscanf(fin, "%d", &n);
        for (i = 0; i < n; i++)
        {
            fgetc(fin);
            for (j = 0; j < n; j++)
            {
                fscanf(fin, "%c", &(m[i][j]));
            }
        }
        for (i = 0; i < n; i++)
        {
            wp[i] = 0;
            nr[i] = 0;
            for (j = 0; j < n; j++)
                if (m[i][j] != '.')
                {
                    if (m[i][j] == '1') wp[i]++;
                    nr[i]++;
                }
            wp[i] /= nr[i];
        }
        for (i = 0; i < n; i++)
        {
            owp[i] = 0;
            for (j = 0; j < n; j++)
            {
                if (m[i][j] == '0') owp[i] += (wp[j] * nr[j] - 1) / (nr[j] - 1);
                else if (m[i][j] == '1') owp[i] += (wp[j] * nr[j]) / (nr[j] - 1);
            }
            owp[i] /= nr[i];
        }
        for (i = 0; i < n; i++)
        {
            oowp[i] = 0;
            for (j = 0; j < n; j++)
                if (m[i][j] != '.')
                {
                   oowp[i] += owp[j];
                }
            oowp[i] /= nr[i];
        }
        fprintf(fout, "Case #%d:\n", k);
        for (i = 0; i < n; i++) fprintf(fout, "%lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}

