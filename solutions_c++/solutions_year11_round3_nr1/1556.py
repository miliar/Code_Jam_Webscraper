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
    int R, C;
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

    char outbuf[3000];
    for (i=0; i<T; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr1);
        R = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr1);
        C = atoi(subtoken);

        char *bufp = outbuf;
        char row1[51] = "..................................................";
        char row2[51] = "..................................................";
        char *lastrow = row1;
        char *thisrow = row2;
        bool impossible = false;

        for (j=0; j<R; j++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);
            if (impossible) continue; // to suck out remaining lines

            for (k=0; k<C; k++) // row team
            {
                if (token[k] == '.')
                {
                    if (lastrow[k] != '.')
                    {
                        impossible = true;
                        break;
                    }
                    thisrow[k] = '.';
                    *bufp++ = thisrow[k];
                }
                // otherwise, current spot is a "#"
                else if (lastrow[k] == '.')
                {
                    // first or second?
                    if (k == 0 ||
                        (thisrow[k-1] == '.') ||
                        (thisrow[k-1] == '\\'))
                    {
                        thisrow[k] = '/';
                    }
                    else if (thisrow[k-1] == '/')
                    {
                        thisrow[k] = '\\';
                    }
                    else
                    {
                        impossible = true;
                        break;
                    }
                    *bufp++ = thisrow[k];
                }
                else if (lastrow[k] == '/')
                {
                    // finishing off a row, so don't carry state
                    thisrow[k] = '.';
                    *bufp++ = '\\';
                }
                else if (lastrow[k] == '\\')
                {
                    // finishing off a row, so don't carry state
                    thisrow[k] = '.';
                    *bufp++ = '/';
                }
            }
            *bufp++ = '\n';

            if (thisrow[C-1] == '/')
            {
                impossible = true;
                continue;
            }

            char *temp = lastrow;
            lastrow = thisrow;
            thisrow = temp;
        }
        *bufp++ = '\0';
        for (k=0; k<C; k++) // row team
        {
            if (lastrow[k] != '.')
            {
                impossible = true;
                break;
            }
        }

        printf("Case #%d:\n", i+1);
        if (impossible)
        {
            printf("Impossible\n");
        }
        else
        {
            printf("%s", outbuf);
        }
    }


    fclose(fp);
    return 0;
}
