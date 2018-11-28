/******************************************************************************
* Name            : SavingTheUniverse.cpp
* Author          : Hoitan Adrian
* Email           : hoitanadrian@gmail.com
* Version         : 1.0
* Description     : Qualification Round for the Google Code Jam 2008.
*                   Problem: Saving the Universe
******************************************************************************/
#include <stdio.h>
#include <string.h>



//< Macro definition
#define _ErrorLabel Error
#define CPR(pPointer) if(NULL == (pPointer)) {printf("Invalid pointer: Line=%d, File=%s\n", __LINE__, __FILE__); goto _ErrorLabel;} 



//< Defines values
#define PATH_INPUT_DATA                 "Input1.in"
#define PATH_OUTPUT_DATA                "Output.out"
#define MAX_LENGTH_SEARCH_ENGINE        102               //< 2 more character for the end of line character and end of text
#define MAX_SEARCH_ENGINES              100
#define MAX_QUERIES                     1000



typedef struct tagSearchEngine
{
    int  iUsageTimes;                                     //< Number of times was accesed this SearchEngine
    char chName[MAX_LENGTH_SEARCH_ENGINE];                //< Engine name
}SearchEngine;



//< Forward function declaration
int SolveProblem();



/******************************************************************************
* Name:   main
* Desc:   Main function
* Args:   None
* Return: int value result
******************************************************************************/
int main()
{
    SolveProblem();

    return 0;
}



/******************************************************************************
* Name:   SolveProblem
* Desc:   Solve problem
* Args:   None
* Return: int value result
******************************************************************************/
int SolveProblem()
{
    FILE         *pFile          = NULL;
    FILE         *pOutputFile    = NULL;
    unsigned int uiCases         = 0;
    unsigned int uiSearchEngines = 0;
    unsigned int uiQueries       = 0;
    bool         bFounded        = false;
    unsigned int uiSwitches      = 0;
    bool         bSwitch         = false;
    int          iLastQuery      = 0;
    SearchEngine seEngines[MAX_SEARCH_ENGINES];
    char         chQuery[MAX_LENGTH_SEARCH_ENGINE];
    char         chGarbage[MAX_LENGTH_SEARCH_ENGINE];
    
    //< Open input file
    pFile = fopen (PATH_INPUT_DATA,"r");
    CPR(pFile);
    pOutputFile = fopen (PATH_OUTPUT_DATA,"w");
    CPR(pOutputFile);

    //< Read the number of cases that we have
    fscanf(pFile, "%d", &uiCases);

    //< Solve all test cases one by one
    for (int iStep = 0; iStep < uiCases; iStep++)
    {
        //< Reinitialize all variables for a new test case
        uiSwitches      = 0;
        uiSearchEngines = 0;
        uiQueries       = 0;
        chQuery[0]      = '\0';
        for (int jStep = 0; jStep < MAX_SEARCH_ENGINES; jStep++)
        {
            seEngines[jStep].iUsageTimes = 0;
            seEngines[jStep].chName[0]   = '\0';
        }

        //< Read the number of search engines
        fscanf(pFile, "%d", &uiSearchEngines);
        fgets(chGarbage, MAX_LENGTH_SEARCH_ENGINE, pFile);    //< There are some garbage caracters after the number
        
        //< Get all search engines
        for (int jStep = 0; jStep < uiSearchEngines; jStep++)
        {
            seEngines[jStep].iUsageTimes = 0;    //< Initialize usage time
            fgets(seEngines[jStep].chName, MAX_LENGTH_SEARCH_ENGINE, pFile);
            seEngines[jStep].chName[strlen(seEngines[jStep].chName) - 1] = '\0';    //< Cut end of line
        }

        //< Read the number of queries
        fscanf(pFile, "%d", &uiQueries);
        fgets(chGarbage, MAX_LENGTH_SEARCH_ENGINE, pFile);    //< There are some garbage caracters after the number

        //< Get all queries
        for (int jStep = 0; jStep < uiQueries; jStep++)
        {
            fgets(chQuery, MAX_LENGTH_SEARCH_ENGINE, pFile);
            chQuery[strlen(chQuery) - 1] = '\0';    //< Cut end of line

            //< Find the matching search engine for this query
            bFounded = false;
            for (int qStep = 0; (qStep < uiSearchEngines) && (bFounded == false); qStep++)
            {
                if (0 == strcmp(chQuery, seEngines[qStep].chName))
                {
                    bFounded   = true;
                    seEngines[qStep].iUsageTimes++;
                    iLastQuery = qStep;
                }
            }

            //< If we still have Search engines that have iUsageTimes == 0 we can still continue to go down without increasing 
            //< the number of switches
            bSwitch = true;
            for (int qStep = 0; (qStep < uiSearchEngines) && (bSwitch == true); qStep++)
            {
                if (0 == seEngines[qStep].iUsageTimes)
                {
                    //< We don't have to switch
                    bSwitch = false;
                }
            }

            //< We have to switch
            if (true == bSwitch)
            {
                uiSwitches++;
                //< Reinitilaize all our search engines with iUsageTimes = 0 
                for (int qStep = 0; qStep < uiSearchEngines; qStep++)
                {
                    seEngines[qStep].iUsageTimes = 0;
                }
                //< Add our last query
                seEngines[iLastQuery].iUsageTimes = 1;
            }
        }

        //< Output our results
        fprintf(pOutputFile, "Case #%d: %d\n", iStep + 1, uiSwitches);
    }

Error:
    //< Cleanup
    if (NULL != pFile)
    {
        fclose(pFile);
    }
    if (NULL != pOutputFile)
    {
        fclose(pOutputFile);
    }
    return 0;
}
