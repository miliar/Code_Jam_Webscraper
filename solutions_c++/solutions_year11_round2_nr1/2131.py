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
    double fTemp1;
    double fTemp2;
    int nTemp2;
    for(int i = nMaxIter; i > 0; --i)
    {
        //fTemp1 = i * 100.0/nPD;
        //nTemp2 = i * 100/nPD;
        //fTemp2 = (double) nTemp2;
        fTemp1 = i * nPD/100.0;
        nTemp2 = i * nPD/100;
        fTemp2 = (double) nTemp2;
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
        int nN = atoi(sTempBuffer);
        double fp[1000][1000];
        double wp[1000];
        double owp[1000];
        double oowp;
        
        for(int j = 0; j < nN; ++j)
        {
            fgets(sTempBuffer, 10000, fpInFile);
            wp[j] = 0;
            int nPlayed = 0;
            for(int k = 0; k < nN; ++k)
            {
                if(sTempBuffer[k] == '.')
                {
                    fp[j][k] = -1;
                }
                else if(sTempBuffer[k] == '1')
                {
                    fp[j][k] = 1;
                    ++nPlayed;
                    wp[j] += 1;
                }
                else
                {
                    ++nPlayed;
                    fp[j][k] = 0;
                }
            }
            wp[j] /= nPlayed;
            printf("%d - wp = %lf\n", j, wp[j]);
        }

        // owp
        for(int j = 0; j < nN; ++j)
        {
            owp[j] = 0;
            int nOpponents = 0;
            for(int k = 0; k < nN; ++k)
            {
                if(j == k)
                    continue;
                double fTemp = 0;
                int nPlayed = 0;
                bool bPlayed = false;
                for(int l = 0; l < nN; ++l)
                {
                    if(l == j)
                    {
                        if(fp[k][l] != -1)
                        {
                            bPlayed = true;
                            ++nOpponents;
                        }
                        continue;
                    }
                    if(fp[k][l] == 1)
                    {
                        ++nPlayed;
                        fTemp += 1;
                    }
                    else if(fp[k][l] == 0)
                    {
                        ++nPlayed;
                    }
                }
                if(bPlayed)
                {
                    if(nPlayed != 0)
                    {
                        owp[j] += fTemp/nPlayed;
                    }
                }
            }
            owp[j] /= nOpponents;
            printf("%d - owp = %lf\n", j, owp[j]);

        }
        oowp = 0;
        for(int j = 0; j < nN; ++j)
        {
            oowp += owp[j];
        }
        fprintf(fpOutFile, "Case #%d:\n", iter+1);
        for(int j = 0; j < nN; ++j)
        {
            oowp = 0;
            int nPlayed = 0;
            for(int k = 0; k < nN; ++k)
            {
                if(j == k)
                    continue;
                bool bPlayed = 0;
                for(int l = 0; l < nN; ++l)
                {
                    if(j == l)
                    {
                        if(fp[k][l] != -1)
                        {
                            ++nPlayed;
                            oowp += owp[k];
                            break;
                        }
                    }
                }
            }
            double nTemp = (oowp)/(nPlayed);
            //double nTemp = (oowp - owp[j])/(nN - 1);
            printf("%d - oowp = %lf\n", j, nTemp);
            double rpi = (0.25 * wp[j]) + (0.5 * owp[j])
                + (0.25*nTemp);
            fprintf(fpOutFile, "%lf\n", rpi);
        }
    }
    fclose(fpInFile);
    fclose(fpOutFile);
    return 0;
}
