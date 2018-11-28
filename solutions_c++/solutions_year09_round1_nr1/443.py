#include <stdio.h>
#include <string.h>
#include <time.h>

bool CheckUnHappy(int num, int base);
bool CheckHappy(int num, int base);

int main(int argc, char* argv[])
{
    FILE *pIn = NULL;
    FILE *pOut = NULL;
    pIn = fopen("Input.txt", "r");
    pOut = fopen("Output.txt", "w");

    int caseNum = 0;
    fscanf(pIn, "%d\n", &caseNum);
    
    for(int i = 0; i < caseNum; i++)
    {
        printf("case: %d\n", i);
        int baseCnt = 0;
        int bases[10];
        fscanf(pIn, "%d", &bases[baseCnt]);
        baseCnt++;
        while(fgetc(pIn) != '\n')
        {
            fscanf(pIn, "%d", &bases[baseCnt]);
            baseCnt++;
        }

        for(int j = 0; j < baseCnt; j++)
        {
            printf("%d ", bases[j]);
        }
        printf("\n");

        for(int j = 2; j <= 100000000; j++)
        {
            bool allPass = false;
            for(int k = 0; k < baseCnt; k++)
            {
                if(bases[k] == 2 || bases[k] == 4)
                {
                    if(k == baseCnt - 1)
                        allPass = true;
                    continue;
                }
                if(!CheckHappy(j, bases[k]))
                    break;
                if(k == baseCnt - 1)
                    allPass = true;
            }
            if(allPass)
            {
                fprintf(pOut, "Case #%d: %d\n", i + 1, j);
                break;
            }
        }


  
    }

    fclose(pIn);
    fclose(pOut);
    
    return 0;
}

bool CheckUnhappy(int num, int base)
{
    switch(base)
    {
    case 2:
    case 4:
        return false;
    case 3: if(num == 2 || num == 5 || num == 8) { return true; } break;
    case 5: if(num == 4 || num == 13 || num == 18) { return true;} break;
    case 6: if(num == 20 || num == 5 || num == 13 || num == 25 || num == 17 || num == 29 || num == 26 || num == 41) { return true; } break;
    case 7: if(num == 2 || num == 10 || num == 17 || num == 25 || num == 32 || num == 45) { return true; } break;
    case 8: if(num == 4 || num == 5 || num == 20 || num == 26 || num == 52) { return true; } break;
    case 9: if(num == 41 || num == 50 || num == 53 || num == 68) { return true;} break;
    case 10: if(num == 4) { return true;} break;
    }
    return false;
}



bool CheckHappy(int num, int base)
{
    if(CheckUnhappy(num, base))
        return false;

    int result = 0;
    while(num > 0)
    {
        result += (num % base) * (num % base);
        num = (num - (num % base)) / base;
    }
    if(result == 1)
        return true;
    
    return CheckHappy(result, base);
}
