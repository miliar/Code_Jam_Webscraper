#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <map>

// T test cases 1<=T<=50
// N == number
// small -> 1<=N<=10^6
// large -> 1<=N<=10^20
#define BUFSZ 10000



int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;
    int i;

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
/*
    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    subtoken = strtok_r(token, " ", &sptr2);
    L = atoi(subtoken);
    subtoken = strtok_r(NULL, " ", &sptr2);
    D = atoi(subtoken);
    subtoken = strtok_r(NULL, " ", &sptr2);
    N = atoi(subtoken);
    */


    char numvals[62];

    for (i=0; i<T; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        int len = strlen(token);
        std::map<char,int> letters;
        std::map<char,int>::iterator it;
        int j;
        int curr = 1;
        for (j=0; j<len; j++)
        {
            it = letters.find(token[j]);
//            if (letters[token[j]] == NULL)
            if (it == letters.end()) // not found
            {
//                printf("adding letter: %c\n", token[j]);
                letters[token[j]] = curr;
                numvals[j] = curr;
                if (curr == 1) curr = 0;
                else if (curr == 0) curr = 2;
                else curr++;
            }
            else
            {
//                printf("found letter: %c\n", token[j]);
                numvals[j] = letters[token[j]];
            }
        }
        int base;
        if (curr == 0) base = 2;
        else base = curr;
//        for (j=0; j<len; j++) printf("%d",numvals[j]);
//        printf(": base %d\n", base);

        long long total = 0;
        for (j=0; j<len; j++) total = total*base + numvals[j];
            
        printf("Case #%d: %lld\n", i+1, total);


        /*
        tokens
            4+3*4+2*16+1 12
            102
            tot = 1*n
            tot = tot * n + newdig
            tot = tot * n + newdig

102  92
1023 64+8+3
10234
*/
    }


    fclose(fp);
    return 0;
}
