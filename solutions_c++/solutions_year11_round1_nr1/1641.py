#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

bool parseSingleTestLine(char* sTempBuffer)
{
    int nN = atoi(strtok(sTempBuffer, " "));
    int nPD = atoi(strtok(NULL, " "));
    int nPG = atoi(strtok(NULL, " "));
    if(nPG == 0)
    {
        if(nPD != 0)
            return false;
    }
    if(nPD == 0)
    {
        if(nPG != 100)
        {
            return true;
        }
        return false;
    }
    if(nPG == 100)
    {
        if(nPD != 100)
            return false;
    }
    if(nPD == 100)
    {
        if(nPG <= 100)
            return true;
    }
    int nMaxIter = nN;// * nPD/100;
    float fTemp1;
    float fTemp2;
    int nTemp2;
    for(int i = nMaxIter; i > 0; --i)
    {
        //fTemp1 = i * 100.0/nPD;
        //nTemp2 = i * 100/nPD;
        //fTemp2 = (float) nTemp2;
        fTemp1 = i * nPD/100.0;
        nTemp2 = i * nPD/100;
        fTemp2 = (float) nTemp2;
        if(fTemp2 == fTemp1)
        {
            if(nTemp2 <= nN)
                return true;
        }
    }
    return false;
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
    char sTempBuffer[10024];
    fgets(sTempBuffer, 10000, fpInFile);
    int nNoOfTests = atoi(sTempBuffer);
    for(int iter = 0; iter < nNoOfTests; ++iter)
    {
        fgets(sTempBuffer, 10000, fpInFile);
        bool bflag = parseSingleTestLine(sTempBuffer);
        if(bflag)
        {
            fprintf(fpOutFile, "Case #%d: Possible\n", iter+1);
        }
        else
        {
            fprintf(fpOutFile, "Case #%d: Broken\n", iter+1);
        }
    }
    fclose(fpInFile);
    fclose(fpOutFile);
    return 0;
}
