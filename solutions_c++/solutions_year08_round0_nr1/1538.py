#include <iostream.h>
#include <map>
#include <math.h>
#include <string>
#include <stdio.h>

#define SEARCH_ENGINE_NAME_LEN 102
#define SEARCH_COUNT 1000

int getMinNumberOfSwitch(std::map<std::string, int> *searchEngineMap, char ** searchList, 
            int startIndex, int searchCount, bool isRecursiveCall= false)
{
    int minSwitch = -1;
    int switchCount = 0;
    int lastFirstSearchString = -1;
    int i = startIndex;

    //printf("-------Entering getMinNumberOfSwitch-----------\n");
    for(;i < searchCount; i++)
    {
        if(0 == (*searchEngineMap)[searchList[i]])
        {
            lastFirstSearchString = i;
        }
    
        if(i != startIndex ||
           ( i == startIndex && isRecursiveCall == false))
        {
            (*searchEngineMap)[searchList[i]]++;
        }

        //printf("%s count is %d\n", searchList[i], (*searchEngineMap)[searchList[i]]);
    }
    
    std::map<std::string, int>::iterator startIter = searchEngineMap->begin();
    std::map<std::string, int>::iterator endIter   = searchEngineMap->end();


    for(;startIter != endIter; startIter++)
    {
        if(minSwitch == -1 ||
           minSwitch > (*startIter).second)
        {
            minSwitch = (*startIter).second;
        }
        
        if(minSwitch == 0)
        {
            break;
        }
    }
    

    if(minSwitch != 0)
    {
        std::map<std::string, int>::iterator startIter = searchEngineMap->begin();
        std::map<std::string, int>::iterator endIter   = searchEngineMap->end();

        std::map<std::string, int> newMap;
        
        switchCount++;
        for(;startIter != endIter; startIter++)
        {
            newMap[(*startIter).first] = 0;
        }

        int nextSearchListStart = lastFirstSearchString;

        //printf("Last searched string is %s, at index %d\n", searchList[lastFirstSearchString], lastFirstSearchString);
        if(nextSearchListStart < searchCount - 1)
        {
            switchCount += getMinNumberOfSwitch(&newMap, searchList, nextSearchListStart, searchCount);
        }
    }
    else
    {
        switchCount = minSwitch;
    }

    
    return switchCount;
}

int getSwitchCountForTestCase(FILE *inputFile)
{
    int switchCount = 0;
    char searchEngineName[SEARCH_ENGINE_NAME_LEN] = {'\0'};

    std::map<std::string, int> searchEngineMap;
    char **searchList = NULL;
    int searchEngineCount = 0;
    int searchCount = 0;
    int i = 0;

    fscanf(inputFile, "%d\n", &searchEngineCount);

    //printf("searchEngineCount is %d\n", searchEngineCount);
    for(;searchEngineCount;searchEngineCount--)
    {
        fgets(searchEngineName, SEARCH_ENGINE_NAME_LEN, inputFile);

        int strLen = strlen(searchEngineName);

        //printf("Search Engine Name is %s\n", searchEngineName);
        std::string engineName = std::string(searchEngineName);
        searchEngineMap[engineName] = 0;
    }

    fscanf(inputFile, "%d\n", &searchCount);

    //printf("searchCount is %d\n", searchCount);

    if(searchCount > 0)
    {
        searchList = (char**) malloc(sizeof(char*) * searchCount);

        for(i = 0; i < searchCount; i++)
        {
            searchList[i] = (char*) malloc(sizeof(char) * SEARCH_ENGINE_NAME_LEN);
            searchList[i][0] = '\0';
        }
        
        for(i = 0; i < searchCount; i++)
        {
            fgets(searchList[i], SEARCH_ENGINE_NAME_LEN, inputFile);

            //printf("searchList[%d]: %s\n", i, searchList[i]);
        }
        
        switchCount = getMinNumberOfSwitch(&searchEngineMap, searchList, 0,searchCount);

        for(i = 0; i < searchCount; i++)
        {
            delete(searchList[i]);
        }

        delete searchList;
    }
    return switchCount;
}

void runTestCase(FILE *inputFile, FILE* outFile)
{
    int i = 0;

    int testCaseCount = 0;
    fscanf(inputFile, "%d", &testCaseCount);
    //printf("Testcase count is %d\n", testCaseCount);

    i = 1;
    for(;i <= testCaseCount; i++)
    {
        int switchCount = 0;

        //printf("-------Handling testcase %d--------\n", i);
        switchCount = getSwitchCountForTestCase(inputFile);

        //cout<< "TargetNumber = " << targetNumber<< "\n";

        fprintf(outFile, "Case #%d: %d\n", i, switchCount);
    }

}

int main(int argc, const char** argv)
{
    if(argc < 3)
    {
        printf("Wrong number of arguments. Usage: universe input_filename output_filename \n");
    }

    FILE* inputFile = fopen(argv[1], "r");
    FILE *outFile = fopen(argv[2], "w");

    if(NULL != inputFile )
    {
        if(NULL != outFile)
        {
            runTestCase(inputFile, outFile);
            fclose(outFile);
        }

        fclose(inputFile);
    }
    else if(NULL != outFile)
    {
            fclose(outFile);
    }

    return 0;
}
