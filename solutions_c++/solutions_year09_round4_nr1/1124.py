#include <stdio.h>
#include <string.h>
#include <time.h>


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
        
        int rowNum = 0;
        int rows[50];
        
        fscanf(pIn, "%d\n", &rowNum);
        //printf("rows: %d\n", rowNum);
        
        for(int j = 0; j < rowNum; j++)
        {
            int rowW = 0;
            int charCnt = 0;
            char temp;
            while(temp = fgetc(pIn))
            {
                //printf("%c", temp);
                charCnt++;
                if(temp == '\n')
                    break;
                if(temp == '1')
                    rowW = charCnt;
            }
            rows[j] = rowW;
            //printf("%d\n", rows[j]);
        }

        int moves = 0;
        for(int j = 0; j < rowNum; j++)
        {
            if(rows[j] <= j + 1)
                continue;

            for(int k = j + 1; k < rowNum; k++)
            {
                if(rows[k] <= j + 1)
                {
                    for(int m = k; m > j; m--)
                    {
                        int tmp = 0;
                        tmp = rows[m];
                        rows[m] = rows[m - 1];
                        rows[m - 1] = tmp;
                        moves++;
                    }
                    break;
                }
            }

        }
        //printf("Case #%d: %d\n", i + 1, moves);
        fprintf(pOut, "Case #%d: %d\n", i + 1, moves);
        

    }

    fclose(pIn);
    fclose(pOut);
    
    return 0;
}
