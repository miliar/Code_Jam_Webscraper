#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <string.h>
#include <iostream>
#include <map>
#include <utility>

using namespace std;
char* parseSingleTestLine(char* sTempBuffer)
{
    map<string, char> Replace;
    map<string, char> Clear;
    
    int C;
    int D;
    int N;
    char *sN;
    char sTemp[10];
    char* sToken;
    char x,y,z;
    C = atoi(strtok(sTempBuffer, " "));
    if(C)
    {
        for(int iter = 0; iter < C; ++iter)
        {
            sToken = strtok(NULL, " ");
            x = sToken[0];
            y = sToken[1];
            z = sToken[2];
            sprintf(sTemp, "%c%c", x, y);
            Replace[sTemp] = z;
            sprintf(sTemp, "%c%c", y, x);
            Replace[sTemp] = z;
        }
    }
    D = atoi(strtok(NULL, " "));
    if(D)
    {
        for(int iter = 0; iter < D; ++iter)
        {
            sToken = strtok(NULL, " ");
            x = sToken[0];
            y = sToken[1];
            sprintf(sTemp, "%c%c", x, y);
            Clear[sTemp] = 'a';
            sprintf(sTemp, "%c%c", y, x);
            Clear[sTemp] = 'a';
            // to identify the characters that can clear the string.
            sprintf(sTemp, "%c", x);
            Clear[sTemp] = 'a';
            sprintf(sTemp, "%c", y);
            Clear[sTemp] = 'a';
        }
    }
    N = atoi(strtok(NULL, " "));
    sN = strtok(NULL, " ");
    static char sResult[1024];
    int nResIter = 0;
    bool bCheckForClear;
    
    for(int iter = 0; iter < N; ++iter)
    {
        bCheckForClear = true;
        sResult[nResIter] = sN[iter];
        if(nResIter > 0)
        {
            x = sResult[nResIter];
            y = sResult[nResIter - 1];
            sprintf(sTemp, "%c%c", x,y);
            if(Replace[sTemp])
            {
                --nResIter;
                sResult[nResIter] = Replace[sTemp];
                bCheckForClear = false;
            }
        }
        if(bCheckForClear && (nResIter > 0))
        {
            x = sResult[nResIter];
            sprintf(sTemp, "%c", x);
            if(Clear[sTemp])
            {
                for(int j = 0; j < nResIter; ++j)
                {
                    y = sResult[j];
                    sprintf(sTemp, "%c%c", y,x);
                    if(Clear[sTemp])
                    {
                        nResIter = -1;
                        break;
                    }
                }
            }
        }
        ++nResIter;
    }
    sResult[nResIter] = '\0';
    return sResult;
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
    fgets(sTempBuffer, 100, fpInFile);
    int nNoOfTests = atoi(sTempBuffer);
    int nNoOfButtons = 0;
    int *nOArray = NULL;
    int *nBArray = NULL;
    char* sNextInQ = NULL;
    int nNoOfMinSec;
    char* sResult;
    for(int iter = 0; iter < nNoOfTests; ++iter)
    {
        fgets(sTempBuffer, 1024, fpInFile);
        char* sResult = parseSingleTestLine(sTempBuffer);
        //printf("Case #%d: %s\n", iter+1, sResult);
        fprintf(fpOutFile, "Case #%d: [", iter+1);
        bool bFirstTime = true;
        for(int iter = 0; iter < strlen(sResult); ++iter)
        {
            if(!bFirstTime)
            {
                fprintf(fpOutFile, ", ");
            }
            fprintf(fpOutFile, "%c", sResult[iter]);
            bFirstTime = false;
        }
        fprintf(fpOutFile, "]\n");
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
