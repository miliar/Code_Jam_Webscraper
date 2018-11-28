#include "stdio.h"
#include "string.h"
#include "stdlib.h"
/*class searchEngineList
{
    public:
        char name[101];
        bool visited;
        searchEngineList()
        {
            visited = false;
        }
        searchEngineList(char* engineName)
        {
            strcpy(name,engineName);
            visited = false;
        }
 
        ~searchEngineList()
        {
        }
};*/
struct searchEngineList
{
        char name[101];
        bool visited;
        /*searchEngineList()
        {
            visited = false;
        }
        searchEngineList(char* engineName)
        {
            strcpy(name,engineName);
            visited = false;
        }
 
        ~searchEngineList()
        {
        }*/
};


int main()
{
    searchEngineList objects[100];
    FILE *inputFilePtr = NULL;
    FILE *outputFilePtr = NULL;
    char inFileName[100];
    size_t constant = 101;
    size_t *size;
    size = &constant;
    printf("\nEnter input file name: \n");
    scanf("%s",inFileName);
    inputFilePtr = fopen(inFileName,"r");
    outputFilePtr = fopen("output.file","w");
    char *line = NULL;
    int numOfCases, numOfEngines, numOfQueries;
    if(getline(&line,size,inputFilePtr) != -1)
    {
        numOfCases = atoi(line);
    }
    else
    {
        printf("\nWRONG INPUT FILE\n");
        return -1;
    }
    for(int i = 0; i < numOfCases; i++)
    {
        if(getline(&line,size,inputFilePtr) != -1)
        {
            numOfEngines = atoi(line);
        }
        else
        {
            printf("\nWRONG INPUT FILE\n");
            return -1;
        }
        for(int j = 0; j < numOfEngines; j++)
        {
            if(getline(&line,size,inputFilePtr) != -1)
            {
                strcpy((objects[j]).name,line);
                (objects[j]).visited = false;
            }
            else
            {
                printf("\nWRONG INPUT FILE\n");
                return -1;
            }
        }
        if(getline(&line,size,inputFilePtr) != -1)
        {
            numOfQueries = atoi(line);
        }
        else
        {
            printf("\nWRONG INPUT FILE\n");
            return -1;
        }
        if(numOfQueries <= 1 || numOfQueries < numOfEngines)
        {
            fprintf(outputFilePtr,"Case #%d: 0\n",i+1);
            //printf("Case #%d: 0\n",i);
            continue;
        }
        char prevQuery[101];
        strcpy(prevQuery,"");
        int indexOfPrevQueryObj = -1;
        int nSwitches = 0;
        int nVisited = 0;

        for(int k = 0; k < numOfQueries; k++)
        {
            if(getline(&line,size,inputFilePtr) == -1)
            {
                printf("\nWRONG INPUT FILE\n");
                return -1;
            }
            if(strcmp(prevQuery, line))
            {
                strcpy(prevQuery,line);
                for(int j = 0; j < numOfEngines; j++)
                {
                    if(!strcmp(line, (objects[j]).name))
                    {
                        if((objects[j]).visited == false)
                        {
                            (objects[j]).visited = true;
                            nVisited++;
                            if(nVisited == numOfEngines)
                            {
                                nVisited = 1;
                                int a = 0;
                                while(a < numOfEngines)
                                {
                                    if(a != j)
                                        (objects[a]).visited = false;
                                    a++;
                                }
                                nSwitches++;
                            }
                            break;
                        }
                    }
                }
            }
        }
        fprintf(outputFilePtr,"Case #%d: %d\n",i+1,nSwitches);
    }
    fclose(inputFilePtr);
    fclose(outputFilePtr);
    return 0;
}
