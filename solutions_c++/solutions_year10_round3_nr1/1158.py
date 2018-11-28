#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
// installed "libgmp3-dev" package on ubuntu
#include <gmpxx.h>

using namespace std;

#define BUFSZ 10000

int A[10000];
int B[10000];

int getints(int a, int b, int N)
{
    int intersections = 0;

    if (N == 0)
    {
        A[N] = a;
        B[N] = b;
        return 0;
    }
    for (int i=0; i<N; i++)
    {
        if (A[i] > a && B[i] < b) intersections++;
        else if (A[i] < a && B[i] > b) intersections++;
    }

    A[N] = a;
    B[N] = b;
    // returns the number of intersections
    return intersections;
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int N;
    int a, b;
    int i, j, k;
    long int count;

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
        count = 0;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        N = atoi(token);

        for (j=0; j<N; j++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);

            subtoken = strtok_r(token, " ", &sptr2);
            a = atoi(subtoken);
            subtoken = strtok_r(NULL, " ", &sptr2);
            b = atoi(subtoken);

            count += getints(a, b, j);
        }

        printf("Case #%d: %ld\n", i+1, count);
//        printf("asdf = %ld\n", asdf);
//        cout << "Case #" << i+1 << ": " << setiosflags(ios::fixed) << setprecision(6) << sum << "\n";
//        cout << "Case #" << i+1 << ": " << getcount(n) << "\n";
    }

    fclose(fp);
    return 0;
}
