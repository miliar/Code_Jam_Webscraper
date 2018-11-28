#include <stdio.h>
#include <string.h>
#include <time.h>

int main(int argc, char* argv[])
{
    FILE *pIn = NULL;
    FILE *pOut = NULL;
    pIn = fopen("Input.txt", "r");
    pOut = fopen("Output.txt", "w");
    
    int letter = 0;
    int dictCnt = 0;
    int caseNum = 0;
    fscanf(pIn, "%d %d %d\n", &letter, &dictCnt, &caseNum);
    //printf("letter: %d, dictNum: %d, CaseNum: %d\n", letter, dictCnt, caseNum);
    
    char dict[5000][17];
    bool matchResult[5000][15];
    
    for(int i = 0; i < dictCnt; i++)
    {
        fgets(dict[i], letter + 2, pIn);
    }
    /*
    for(int i = 0; i < dictCnt; i++)
    {
        printf("%d %s", i, dict[i]);
    }
    */
    
    for(int i = 0; i < caseNum; i++)
    {
        for(int j = 0; j < dictCnt; j++)
        {
            for(int k = 0; k < letter; k++)
            {
                matchResult[j][k] = false;
            }
        }
        
        int pos = 0;
        int matchCnt = 0;
        char text[512];
        fgets(text, 512, pIn);
        //printf("Case: %d %s", i, text);
        
        
        int l = 0;
        while(text[l] != '\n' && text[l] != '\0')
        {
            if(text[l] == '(')
            {
                l++;
                while(text[l] != ')')
                {
                    for(int m = 0; m < dictCnt; m++)
                    {
                        if(dict[m][pos] == text[l])
                        {
                            matchResult[m][pos] = true;
                        }
                    }
                    l++;
                }
                pos++;
                l++;
            }
            else
            {
                for(int m = 0; m < dictCnt; m++)
                {
                    if(dict[m][pos] == text[l])
                    {
                        matchResult[m][pos] = true;
                    }
                }
                pos++;
                l++;
            }
        }
        
        for(int j = 0; j < dictCnt; j++)
        {
            bool flag = true;
            for(int k = 0; k < letter; k++)
            {
                if(!matchResult[j][k])
                {
                    flag = false;
                    break;
                }
            }
            if(flag)
                matchCnt++;
        }
        
        
        fprintf(pOut, "Case #%d: %d\n", i + 1, matchCnt);
    }
    
    
    fclose(pIn);
    fclose(pOut);
    
    return 0;
}
