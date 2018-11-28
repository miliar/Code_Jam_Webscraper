#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void parseSingleTestLine(char* sTempBuffer,
        int* nNoOfButts, int** nOArray, int** nBArray,
        char** sNextInQ)
{
//    char* token = strtok(sTempBuffer, " ");
//    while(token)
//    {
//        printf("\n%s\n", token);
//        token = strtok(NULL, " ");
//    }
//    return;
    *nNoOfButts = atoi(strtok(sTempBuffer, " "));
    *nOArray = new int[*nNoOfButts + 1];
    *nBArray = new int[*nNoOfButts + 1];
    *sNextInQ = new char[*nNoOfButts + 1];
    // initialize
    for(int iter = 0; iter < *nNoOfButts + 1; ++iter)
    {
        *(*nOArray + iter) = 0;
        *(*nBArray + iter) = 0;
        *(*sNextInQ +iter) = '\0';
    }
    // parsing ..
    char* sTemp;
    int nTemp;
    int Oiter = 0;
    int Biter = 0;
    
    for(int iter = 0; iter < *nNoOfButts; ++iter)
    {
        sTemp = strtok(NULL, " ");
        assert((sTemp[0] == 'O') || (sTemp[0] == 'B'));
        *(*sNextInQ + iter) = sTemp[0];
        nTemp = atoi(strtok(NULL, " "));
        if(sTemp[0] == 'O')
        {
            *(*nOArray + Oiter) = nTemp;
            ++Oiter;
        }
        else
        {
            *(*nBArray + Biter) = nTemp;
            ++Biter;
        }
    }
}

int getNewPosBasedOnCurrPosAndTargetPos(int nCurrPos, int nTargetPos)
{
    if(!nTargetPos || (nTargetPos == nCurrPos))
    {
        return nTargetPos;
    }
    if(nTargetPos > nCurrPos)
    {
        return nCurrPos + 1;
    }
    else
    {
        return nCurrPos - 1;
    }
}
int findMinNoOfSec(int nNoOfButtons, int nOArray[], int nBArray[], char* sNextInQ)
{
    int nNoOfSec = 0;
    int nOPos = 1;
    int nBPos = 1;
    int nOIter = 0;
    int nBIter = 0;
    int nIter = 0;
    bool bOCantMove, bBCantMove;
    for(;sNextInQ[nIter] != '\0';++nNoOfSec)
    {
        bOCantMove = false;
        bBCantMove = false;
        if(sNextInQ[nIter] == 'O')
        {
            if(nOPos == nOArray[nOIter])
            {
                bOCantMove = true;
                ++nOIter;
                ++nIter;
            }
        }
        else if(sNextInQ[nIter] == 'B')
        {
            if(nBPos == nBArray[nBIter])
            {
                bBCantMove = true;
                ++nBIter;
                ++nIter;
            }
        }
        if(!bOCantMove)
        {
            nOPos = getNewPosBasedOnCurrPosAndTargetPos(nOPos, nOArray[nOIter]);
        }
        if(!bBCantMove)
        {
            nBPos = getNewPosBasedOnCurrPosAndTargetPos(nBPos, nBArray[nBIter]);
        }
    }
    return nNoOfSec;
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
    for(int iter = 0; iter < nNoOfTests; ++iter)
    {
        nNoOfButtons = 0;
        nOArray = NULL;
        nBArray = NULL;
        sNextInQ = NULL;
        fgets(sTempBuffer, 1024, fpInFile);
        parseSingleTestLine(sTempBuffer, &nNoOfButtons,
                &nOArray, &nBArray, &sNextInQ);
        nNoOfMinSec = findMinNoOfSec(nNoOfButtons, nOArray, nBArray, sNextInQ);
        fprintf(fpOutFile, "Case #%d: %d\n", iter+1, nNoOfMinSec);
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
