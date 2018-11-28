#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <list>
#include <math.h>
using namespace std;

#define BUFSZ 1000000

#if 0
#define mling(...)
#else
#define mling printf
#endif

typedef struct
{
    double time;
    double pos;
} vals;

vals mylist[2000];
int listcount;

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    double D;
    double mydist, mytime;
    int N, A;
    double t, x;
    double lastt, lastx;
    double a;

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

        subtoken = strtok_r(token, " ", &sptr2);
        D = atof(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        N = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        A = atoi(subtoken);

        mydist = 0;
        mytime = 0;

        listcount = 0;

        // figure out the time it takes to reach D
        for (j=0; j<N; j++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);

            subtoken = strtok_r(token, " ", &sptr2);
            t = atof(subtoken);
            subtoken = strtok_r(NULL, " ", &sptr2);
            x = atof(subtoken);

            if (x >= D)
            {
                if (j == 0)
                {
                    // no cars blocking!  done!
                    mytime = 0;
                }
                else
                {
                    // last segment; calculate partial time of leg
                    mytime += (t-lastt)/(x-lastx) * (D-mydist);
                    mylist[listcount].time = mytime;
                    mylist[listcount++].pos = D;
                }
                for (j++; j<N; j++) fgets(strBuf, BUFSZ, fp);
                break;
            }
            else
            {
                mytime = lastt = t;
                mydist = lastx = x;
                if (j > 0)
                {
                    mylist[listcount].time = t;
                    mylist[listcount++].pos = x;
                }
            }
        }

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        printf("Case #%d:\n", i+1);
//        printf("%s\n", token);

        // accelerations
        for (j=0; j<A; j++)
        {
            double shortesttime;
            double addtime = 0;
            subtoken = strtok_r(((j==0)?token:NULL), " ", &sptr2);
            a = atof(subtoken);

            shortesttime = sqrt(2 * D / a);
//            printf("shortesttime: %f\n", shortesttime);
//            printf("mytime: %f\n", mytime);
//

            for (k=0; k<listcount; k++)
            {
                double temptime = mylist[k].time - sqrt(2 * mylist[k].pos / a);
                // is point k below graph
                if (temptime > 0 &&
                    temptime > addtime)
                {
                    addtime = temptime;
                }
            }

            printf("%0.6f\n", shortesttime+addtime);
        }
    }


    fclose(fp);
    return 0;
}
