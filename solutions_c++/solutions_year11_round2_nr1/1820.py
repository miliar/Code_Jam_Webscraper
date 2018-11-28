#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000


int wpn[100];
int wpd[100];
double owp[100];
double oowp[100];
int state[100][100];

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int N;
    int i, j, k;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }


    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (i=0; i<T; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        N = atoi(token);

        for (j=0; j<N; j++)
        {
            wpn[j] = 0;
            wpd[j] = 0;
        }
        for (j=0; j<N; j++) // column team
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);

            for (k=0; k<N; k++) // row team
            {
                if (token[k] == '0')
                {
                    state[j][k] = 0;
                    wpd[j]++;
                }
                else if (token[k] == '1')
                {
                    state[j][k] = 1;
                    wpn[j]++;
                    wpd[j]++;
                }
                else
                {
                    state[j][k] = 2; // didn't play
                }
            }
        }

        for (k=0; k<N; k++) // row team
        {
            double total = 0;
            int teams = 0;

            for (j=0; j<N; j++) // column team
            {
                if (state[j][k] == 2) continue;
                else if (state[j][k] == 1)
                {
                    total += 1.0*(wpn[j]-1)/(wpd[j]-1);
                }
                else
                {
                    total += 1.0*(wpn[j])/(wpd[j]-1);
                }
                teams++;
            }
            owp[k] = total/teams;
        }

        for (j=0; j<N; j++) // column team
        {
            double total = 0;
            int teams = 0;

//            printf("team %d\n", k);
            for (k=0; k<N; k++) // row team
            {
                if (state[j][k] == 2) continue;
                else
                {
//                    printf("adding [%d][%d]: %f\n", j, k, owp[k]);
                    total += owp[k];
                    teams++;
                }
            }
            oowp[j] = 1.0*total/teams;
//            printf("oowp[%d]: %f\n", j, oowp[j]);
        }

        printf("Case #%d:\n", i+1);
        for (j=0; j<N; j++)
        {
            printf("%0.7f\n",
                   0.25 * wpn[j]/wpd[j] +
                   0.50 * owp[j] +
                   0.25 * oowp[j]);
        }
    }


    fclose(fp);
    return 0;
}
