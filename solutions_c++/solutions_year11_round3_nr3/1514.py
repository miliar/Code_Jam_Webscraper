#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
int a[10000];
int nN;

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
        nN = atoi(strtok(sTempBuffer, " "));
        int nLF = atoi(strtok(NULL, " "));
        int nHF = atoi(strtok(NULL, " "));
        fgets(sTempBuffer, 10000, fpInFile);
        a[0] = atoi(strtok(sTempBuffer, " "));
        for(int i = 1; i < nN; ++i)
        {
            a[i] = atoi(strtok(NULL, " "));
        }
        bool bFound = false;
        int nF = 0;
        for(int i = nLF; i <= nHF; ++i)
        {
            bFound = false;
            for(int j = 0; j < nN; ++j)
            {
                if((a[j]%i == 0) || (i%a[j] == 0))
                {
                    bFound = true;
                    continue;
                }
                else
                {
                    bFound = false;
                    break;
                }
            }
            if(bFound)
            {
                nF = i;
                break;
            }
        }
        if(nF != 0)
        {
            fprintf(fpOutFile, "Case #%d: %d\n", iter+1, nF);
        }
        else
        {
            fprintf(fpOutFile, "Case #%d: NO\n", iter+1);
        }
    }
    fclose(fpInFile);
    fclose(fpOutFile);
    return 0;
}
