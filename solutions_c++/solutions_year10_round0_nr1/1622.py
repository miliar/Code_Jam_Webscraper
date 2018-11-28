#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

// L lowercase letters in every word
// D words in the language
//
// L D N
#define BUFSZ 10000


// if N were 2, mod by 4 to give num between 0-3
// then divide by 2
// config snaps
// 00       0
// 01       1
// 10       2
// 11       3
// 00       4
// 01       5
// 10       6
// 11       7
// 00       8
// ie. mod by 2^N, check if all bits are 1s
// procedure can be to add 1, then AND with 2^N - 1
int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int N;       // snappers
    long int K;  // snaps
    long int onbits;
    int i;
    bool on;

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
        N = atoi(subtoken);
        subtoken = strtok_r(NULL, " ", &sptr2);
        K = atol(subtoken);

        onbits = (1 << N) - 1;
//        printf("2^%d - 1: %ld\n", N, onbits);
        on = (onbits == (onbits & K));

        printf("Case #%d: %s\n", i+1, on ? "ON" : "OFF");
    }


    fclose(fp);
    return 0;
}
