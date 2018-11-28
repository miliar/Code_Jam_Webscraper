#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000

bool combo(long int win, int num)
{
    return ((win & num) == num);
}
bool wincheck(long int win)
{
    int possible[] = {0x000f,
                      0x00f0,
                      0x0f00,
                      0xf000,
                      0x8888,
                      0x4444,
                      0x2222,
                      0x1111,
                      0x8421,
                      0x1248};
    for (int i=0; i<10; i++)
    {
        if (combo(win,possible[i]))
        {
            return true;
        }
    }
    return false;
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1;
    int T;       // loops
    int i, j, k, l;

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
        long int o = 0;
        long int x = 0;

        /* eat an extra line */
        if (i > 0)
        {
            fgets(strBuf, BUFSZ, fp);
        }
        for (j=0; j<4; j++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);

            for (l=0; l<4; l++)
            {
                switch (token[l])
                {
                    case 'X':
                        x = x | (1 << (j*4+l));
                        break;
                    case 'O':
                        o = o | (1 << (j*4+l));
                        break;
                    case 'T':
                        x = x | (1 << (j*4+l));
                        o = o | (1 << (j*4+l));
                        break;
                }
            }
        }

        printf("Case #%d: ", i+1);

//        printf(" x:%04x o:%04x ", x, o);
        if (wincheck(x))
        {
            printf("X won\n");
        }
        else if (wincheck(o))
        {
            printf("O won\n");
        }
        else if ((x | o) == 65535)
        {
            printf("Draw\n");
        }
        else
        {
            printf("Game has not completed\n");
        }
    }

    fclose(fp);
    return 0;
}
