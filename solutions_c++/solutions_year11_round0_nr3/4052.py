#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <string.h>
#include <iostream>
#include <map>
#include <utility>
#include <math.h>

using namespace std;
#include<stdio.h>

int a[1024];
char sFlag[1024];
int nNoOfElements;
int bDone, bResultFound;
int nResult;
void checkIfThisIsTheCombi(char* sBin)
{
    int exorS = 0;
    int exorP = 0;
    int nSumS = 0;
    int nSumP = 0;
    for(int i = 0; i < nNoOfElements; ++i)
    {
        if(sBin[i] == '1')
        {
            exorS ^= a[i];
            nSumS += a[i];
        }
        else
        {
            exorP ^= a[i];
            nSumP += a[i];
        }
    }
    //printf("\n%s: %d, %d\n", sBin, nSumS, nSumP);
    if(exorP == exorS)
    {
        if(nResult < nSumS)
        {
            nResult = nSumS;
        }
    }
}
void parseSingleTestLine(char* sTempBuffer)
{
    a[0] = atoi(strtok(sTempBuffer, " "));
    for(int i = 1; i < nNoOfElements; ++i)
    {
        a[i] = atoi(strtok(NULL, " "));
    }
    //sort
    int t;
    for(int i = 0; i < nNoOfElements; ++i)
    {
        for(int j=i+1;j<nNoOfElements;j++)
        {
            if(a[i]>a[j])
            {
                t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
    int sum = 0, exor = 0;
    for(int i = 0; i < nNoOfElements; ++i)
    {
        sFlag[i] = '0';
        sum += a[i];
        exor ^= a[i];
    }
    int nMaxNoOfCombi = (int)pow(2, nNoOfElements);
    int nTemp;
    char sBin[nNoOfElements + 1];
    // avoid all 1s and 0s
    for(int i = 1; i < nMaxNoOfCombi - 1; ++i)
    {
        nTemp = i;
        for(int j = 0; j < nNoOfElements; ++j)
        {
            sBin[j] = '0';
        }
        int iter = nNoOfElements - 1;
        while(nTemp)
        {
            if(nTemp%2)
            {
                sBin[iter] = '1'; 
            }
            nTemp /= 2;
            --iter;
        }
        checkIfThisIsTheCombi(sBin);
    }
}


int main(int argc, char** argv)
{
    if(argc != 2)
    {
        printf("Usage: ./a.out <test-case-file-name>\n");
        return 1;
    }
    FILE* fpInFile, *fpOutFile;
    fpInFile = fopen(argv[1], "r");
    if(!fpInFile)
    {
        printf("Cound not open the test file %s.\n", argv[1]);
        return 1;
    }
    fpOutFile = fopen("out_file.txt", "w");
    if(!fpOutFile)
    {
        printf("Cound not open the output file %s.\n", argv[1]);
        return 1;
    }
    // parse the input test file.
    // first line of the test is the number of testcases.
    char sTempBuffer[1024];
    char sTempBuffer2[1024];
    fgets(sTempBuffer, 100, fpInFile);
    int nNoOfTests = atoi(sTempBuffer);
    for(int iter = 0; iter < nNoOfTests; ++iter)
    {
        fgets(sTempBuffer, 1024, fpInFile);
        nNoOfElements = atoi(sTempBuffer);
        fgets(sTempBuffer, 1024, fpInFile);
        nResult = 0;
        parseSingleTestLine(sTempBuffer);
        if(nResult)
        {
            fprintf(fpOutFile, "Case #%d: %d\n", iter+1, nResult);
        }
        else
        {
            fprintf(fpOutFile, "Case #%d: NO\n", iter+1);
        }
//        fprintf(fpOutFile, "Case #%d: [", iter+1);
        // for debug
//#define DEBUG 0
#ifdef DEBUG
        {
            printf("Case #%d: %d\n", iter, nNoOfMinSec);
            printf("Test %d:\n\tButt = %d\n\tTargets = %s\n\t",
                 iter, nNoOfButtons, sNextInQ);
            for(int iter2 = 0; iter2 < nNoOfButtons; ++iter2)
            {
                if(nOArray[iter2] == 0)
                {
                    break;
                }
                printf("%d ", nOArray[iter2]);
            }
            printf("\n\t");
            for(int iter2 = 0; iter2 < nNoOfButtons; ++iter2)
            {
                if(nBArray[iter2] == 0)
                {
                    break;
                }
                printf("%d ", nBArray[iter2]);
            }
            printf("\n");
        }
#endif
    }
    fclose(fpInFile);
    fclose(fpOutFile);
    return 0;
}
