#include <stdio.h>
#include <string.h>
#include <time.h>

char label = 'a';
int height = 0;
int width = 0;
int map[100][100];
int flowMap[100][100];
char result[100][100];
int resultFound = 0;

void FindResult(int posV, int posH);
bool IsFlow(int posV1, int posH1, int posV2, int posH2);
int ToFlow(int posV, int posH);

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
        //printf("case: %d\n", i);
 
        label = 'a';
        height = 0;
        width = 0;
        resultFound = 0;
        
        fscanf(pIn, "%d %d\n", &height, &width);
        //printf("height: %d, width: %d\n", height, width);
        for(int j = 0; j < height; j++)
        {
            for(int k = 0; k < width; k++)
            {
                //printf("%d %d\n", j, k);
                fscanf(pIn, "%d", &map[j][k]);
                flowMap[j][k] = -1;
                result[j][k] = 0;
            }
        }

        for(int j = 0; j < height; j++)
        {
            for(int k = 0; k < width; k++)
            {
                flowMap[j][k] = ToFlow(j, k);
            }
        }
        
        while(resultFound < height * width)
        {
            for(int j = 0; j < height; j++)
            {
                for(int k = 0; k < width; k++)
                {
                    if(result[j][k] == 0)
                    {
                        result[j][k] = label;
                        label++;
                        resultFound++;
                        FindResult(j, k);
                    }
                }
            }
        }
        
        fprintf(pOut, "Case #%d:\n", i + 1);
        for(int j = 0; j < height; j++)
        {
            for(int k = 0; k < width; k++)
            {
                fprintf(pOut, "%c ", result[j][k]);
            }
            fprintf(pOut, "\n");
        }
        
    }
        
    fclose(pIn);
    fclose(pOut);
    
    return 0;
}


void FindResult(int posV, int posH)
{
    if(posV - 1 >= 0)
    {
        if(result[posV - 1][posH] == 0)
        {
            if(IsFlow(posV, posH, posV - 1, posH))
            {
                result[posV - 1][posH] = result[posV][posH];
                resultFound++;
                FindResult(posV - 1, posH);
            }
        }
    }
    if(posH - 1 >= 0)
    {
        if(result[posV][posH - 1] == 0)
        {
            if(IsFlow(posV, posH, posV, posH - 1))
            {
                result[posV][posH - 1] = result[posV][posH];
                resultFound++;
                FindResult(posV, posH - 1);
            }
        }
    }
    if(posH + 1 <= width)
    {
        if(result[posV][posH + 1] == 0)
        {
            if(IsFlow(posV, posH, posV, posH + 1))
            {
                result[posV][posH + 1] = result[posV][posH];
                resultFound++;
                FindResult(posV, posH + 1);
            }
        }
    }
    if(posV + 1 <= height)
    {
        if(result[posV + 1][posH] == 0)
        {
            if(IsFlow(posV, posH, posV + 1, posH))
            {
                result[posV + 1][posH] = result[posV][posH];
                resultFound++;
                FindResult(posV + 1, posH);
            }
        }
    }
}

bool IsFlow(int posV1, int posH1, int posV2, int posH2)
{
    //printf("IsFlow: (%d %d) (%d %d)\n", posV1, posH1, posV2, posH2);
    switch(flowMap[posV1][posH1])
    {
    case 0: if(posV1 - 1 == posV2 && posH1 == posH2) {return true;} break;
    case 1: if(posV1 == posV2 && posH1 - 1 == posH2) {return true;} break;
    case 2: if(posV1 == posV2 && posH1 + 1 == posH2) {return true;} break;
    case 3: if(posV1 + 1 == posV2 && posH1 == posH2) {return true;} break;
    }
    switch(flowMap[posV2][posH2])
    {
    case 0: if(posV2 - 1 == posV1 && posH2 == posH1) {return true;} break;
    case 1: if(posV2 == posV1 && posH2 - 1 == posH1) {return true;} break;
    case 2: if(posV2 == posV1 && posH2 + 1 == posH1) {return true;} break;
    case 3: if(posV2 + 1 == posV1 && posH2 == posH1) {return true;} break;
    }
    return false;
}

int ToFlow(int posV, int posH)
{
    int fourDirection[4] = {10002, 10002, 10002, 10002};
    if(posV - 1 >= 0)
        fourDirection[0] = map[posV - 1][posH];
    if(posH - 1 >= 0)
        fourDirection[1] = map[posV][posH - 1];
    if(posH + 1 < width)
        fourDirection[2] = map[posV][posH + 1];
    if(posV + 1 < height)
        fourDirection[3] = map[posV + 1][posH];

    int min = map[posV][posH];
    int ret = -1;
    for(int i = 0; i < 4; i++)
    {
        if(fourDirection[i] < min)
        {
            min = fourDirection[i];
            ret = i;
        }
    }
    return ret;
}
