#include <iostream>
#include <stdio.h>
#include <math.h>


using namespace std;

void solveCase(int caseN, FILE *fp);

int main()
{
    FILE *fp = fopen("output.txt", "w");

    int numberOfCases;
    fscanf(stdin, "%d", &numberOfCases);
    //printf("Lei %d casos\n", numberOfCases);
    for(int caseN = 0; caseN < numberOfCases; caseN++)
    {
        solveCase(caseN, fp);
    }

    fclose(fp);
    return 0;
}

void solveCase(int caseN, FILE *fp)
{
    int N, Pd, Pg;
    fscanf(stdin, "%d %d %d", &N, &Pd, &Pg);
    float Pdf = Pd / 100.0;
    float Pgf = Pg / 100.0;
    for(int D = 1; D <= N; D++)
    {
        if((Pd * D) % 100 == 0)
        {
            if(Pg == 100 && Pd != 100)
            {
                continue;
            }
            if(Pg == 0 && Pd != 0)
            {
                continue;
            }
            fprintf(fp, "Case #%d: Possible\n", (caseN + 1));
            return;
            /*
            for(int G = D; ; G++)
            {
                float ganadosG = G * Pgf;
                float ganadosD = D * Pdf;
                if(ganadosG >= ganadosD && (G - ganadosG) >= (D - ganadosD))
                {
                    if((G * Pg) % 100 == 0)
                    {
                        printf("Case #%d: Possible with D = %d and G = %d\n", (caseN + 1), D, G);
                        fprintf(fp, "Case #%d: Possible\n", (caseN + 1));
                        return;
                    }
                }
            }
            */
        }
    }


    fprintf(fp, "Case #%d: Broken\n", (caseN + 1));
    return;
}

