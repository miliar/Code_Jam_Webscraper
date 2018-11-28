#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000
typedef struct
{
    char let1;
    char let2;
    char waitingfor;
    char elem;
} combine;

typedef struct
{
    char let1;
    char let2;
    char got;
    char waitingfor;
    bool safe;
} oppose;

combine comb[36];
oppose oppo[28];


bool comboproc(char testchar, char *output, int len, int comboarraylen, char &consumed)
{
    int i;
    for (i=0; i<comboarraylen; i++)
    {
        if (testchar == comb[i].waitingfor)
        {
            consumed = output[len-1];
            output[len-1] = comb[i].elem;
            return true;
        }
    }
    return false;
}

void safewaitingoppos(char consumed, int oppoarraylen)
{
    int i;
    for (i=0; i<oppoarraylen; i++)
    {
        if (oppo[i].safe) continue;
        if (oppo[i].got == '\0') continue;
        if (oppo[i].got == consumed)
        {
            // clear it
            oppo[i].got = '\0';
            oppo[i].waitingfor = '\0';
        }
        else
        {
            oppo[i].safe = true;
        }
    }
}

bool oppoproc(char testchar, int oppoarraylen)
{
    int i;
    for (i=0; i<oppoarraylen; i++)
    {
        if (oppo[i].waitingfor == testchar)
        {
            return true;
        }
    }
    return false;
}

void clearcombos(int comboarraylen)
{
    int i;
    for (i=0; i<comboarraylen; i++)
    {
        comb[i].waitingfor = '\0';
    }
}
void clearcomboppos(int comboarraylen, int oppoarraylen)
{
    int i;
    for (i=0; i<comboarraylen; i++)
    {
        comb[i].waitingfor = '\0';
    }
    for (i=0; i<oppoarraylen; i++)
    {
        oppo[i].got = '\0';
        oppo[i].waitingfor = '\0';
        oppo[i].safe = false;
    }
}

void initcomboppos(char testchar, int comboarraylen, int oppoarraylen)
{
    int i;
    for (i=0; i<comboarraylen; i++)
    {
        if (comb[i].let1 == testchar)
        {
            comb[i].waitingfor = comb[i].let2;
        }
        else if (comb[i].let2 == testchar)
        {
            comb[i].waitingfor = comb[i].let1;
        }
        else
        {
            comb[i].waitingfor = '\0';
        }
    }
    for (i=0; i<oppoarraylen; i++)
    {
        if (oppo[i].got != '\0')
        {
            oppo[i].safe = true;
            continue;
        }
        if (oppo[i].let1 == testchar)
        {
            oppo[i].got = oppo[i].let1;
            oppo[i].waitingfor = oppo[i].let2;
            oppo[i].safe = false;
        }
        else if (oppo[i].let2 == testchar)
        {
            oppo[i].got = oppo[i].let2;
            oppo[i].waitingfor = oppo[i].let1;
            oppo[i].safe = false;
        }
    }
}
void printlist(char *output, int len)
{
    if (len == 0) return;
    int i;
    for (i=0; i<len-1; i++)
    {
        printf("%c, ", output[i]);
    }
    printf("%c", output[i]);
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int C, D, N;
    int i, j;

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
        C = atoi(subtoken);

        for (j=0; j<C; j++)
        {
            subtoken = strtok_r(NULL, " ", &sptr2);
            comb[j].let1=subtoken[0];
            comb[j].let2=subtoken[1];
            comb[j].waitingfor='\0';
            comb[j].elem=subtoken[2];
        }

        subtoken = strtok_r(NULL, " ", &sptr2);
        D = atoi(subtoken);

        for (j=0; j<D; j++)
        {
            subtoken = strtok_r(NULL, " ", &sptr2);
            oppo[j].let1=subtoken[0];
            oppo[j].let2=subtoken[1];
            oppo[j].got='\0';
            oppo[j].waitingfor='\0';
            oppo[j].safe=false;
        }

        subtoken = strtok_r(NULL, " ", &sptr2);
        N = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        int len = 0;
        char consumed;
        char output[101];
        for (j=0; j<N; j++)
        {
            // if combo processed
            if (comboproc(subtoken[j], output, len, C, consumed))
            {
//printf("1:==>j=%d\n", j);
                clearcombos(C);
//printf("consumed: %c\n", consumed);
                safewaitingoppos(consumed, D);
            }
            // check if list will be cleared
            else if (oppoproc(subtoken[j], D))
            {
//printf("2:==>j=%d\n", j);
                clearcomboppos(C, D);
                len = 0;
            }
            // not combined, not opposed
            else
            {
//printf("3:==>j=%d\n", j);
//printf("3:==>len=%d\n", len);
                initcomboppos(subtoken[j], C, D);
                output[len++] = subtoken[j];
//printf("3:==>len=%d\n", len);
            }
//printf("j=%d: ", j);
//printlist(output, len);
//printf("\t len=%d\n", len);

        }

        printf("Case #%d: [", i+1);
        printlist(output, len);
        printf("]\n");
    }


    fclose(fp);
    return 0;
}
