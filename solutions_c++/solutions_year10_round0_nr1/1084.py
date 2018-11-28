#include <stdio.h>
#include <string.h>
#include <time.h>
#include <math.h>



int main(int argc, char* argv[])
{
    FILE *pIn = NULL;
    FILE *pOut = NULL;
    pIn = fopen("A-large.in", "r");
    pOut = fopen("Output.txt", "w");

    int caseNum = 0;
    fscanf(pIn, "%d\n", &caseNum);
    
    for(int i = 0; i < caseNum; i++)
    {
        //printf("case: %d\n", i);

        char *pOn = "ON";
        char *pOff = "OFF";
        char *pRet = NULL;
        int n, k;
        n = k = 0;

        fscanf(pIn, "%d %d\n", &n, &k);

        unsigned int fn;
        fn = 0x1 << n;

        int r = k % fn;

        if(r + 1 == fn)
            pRet = pOn;
        else
            pRet = pOff;

        //printf("Case #%d: %d\n", i + 1, moves);
        fprintf(pOut, "Case #%d: %s\n", i + 1, pRet);
        

    }

    fclose(pIn);
    fclose(pOut);
    
    return 0;
}
