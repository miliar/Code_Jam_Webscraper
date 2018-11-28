#include <stdio.h>
#include <string.h>

int matchCnt = 0;
void Match(char *string, char *subStr);

int main(int argc, char* argv[])
{
    FILE *pIn = NULL;
    FILE *pOut = NULL;
    pIn = fopen("Input.txt", "r");
    pOut = fopen("Output.txt", "w");
    
    int caseNum = 0;
    fscanf(pIn, "%d\n", &caseNum);
    //printf("CaseNum: %d", caseNum);
    
    char wel[] = "welcome to code jam";
    
    for(int i = 0; i < caseNum; i++)
    {
        matchCnt = 0;
        char textAll[501];
        fgets(textAll, 501, pIn);
        
        Match(textAll, wel);
        
        fprintf(pOut, "Case #%d: %04d\n", i + 1, matchCnt);
    }
    
    fclose(pIn);
    fclose(pOut);
    
    return 0;
}

void Match(char *string, char *subStr)
{
    //printf("string: %s", string);
    //printf("subStr: %s\n", subStr);
    while(*string != '\n' && *string != '\0')
    {
        if(*string == *subStr)
        {
            if(*(subStr + 1) == '\0')
            {
                matchCnt++;
                if(matchCnt > 10000)
                    matchCnt -= 10000;
            }
            else
            {
                Match(string + 1, subStr + 1);
            }
        }
        string++;
    }

}