/******************************************************************************
* Name            : TrainTimetable.cpp
* Author          : Hoitan Adrian
* Email           : hoitanadrian@gmail.com
* Version         : 1.0
* Description     : Qualification Round for the Google Code Jam 2008.
*                   Problem: TrainTimetable
******************************************************************************/
#include <stdio.h>
#include <string.h>



//< Macro definition
#define _ErrorLabel Error
#define CPR(pPointer) if(NULL == (pPointer)) {printf("Invalid pointer: Line=%d, File=%s\n", __LINE__, __FILE__); goto _ErrorLabel;} 
#define DELETE_OBJ(p) {if (NULL != p){delete p; p = NULL;}}



//< Defines values
#define PATH_INPUT_DATA                 "Input1.in"
#define PATH_OUTPUT_DATA                "Output.out"



typedef struct tagTimetable
{
    int          iTime;             //< iTime will remember the time in minutes only format
    unsigned int uiTrainsNeeded;     //< Number of trains needed to depart at this time
    unsigned int uiTrainsAvailabile; //< Number of trains availabile to depart at this time

    tagTimetable *pttNextItem;
    tagTimetable *pttPrevItem;

    tagTimetable():
        iTime(0),
        uiTrainsNeeded(0),
        uiTrainsAvailabile(0),
        pttNextItem(NULL),
        pttPrevItem(NULL)
        {}
}TimeTable;



//< Forward function declaration
int SolveProblem();
void AddDepartArrivalTime(TimeTable *pttTrainStation, int iTime, bool bDeparting);
void MergeTrains(TimeTable *pttTrainStation);
int  CountTrains(TimeTable *pttTrainStation);
void Cleanup(TimeTable *pttTrainStation);



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
    FILE         *pFile            = NULL;
    FILE         *pOutputFile      = NULL;
    unsigned int uiCases           = 0;
    unsigned int uiTurnAround      = 0;
    unsigned int uiNA              = 0;
    unsigned int uiNB              = 0;
    int          iDepartH          = 0;
    int          iDepartM          = 0;
    int          iArrivalH         = 0;
    int          iArrivalM         = 0;
    int          iDepartTime       = 0;
    int          iArrivalTime      = 0;
    int          iTrainCountA      = 0;
    int          iTrainCountB      = 0;
    TimeTable    *pttTrainStationA = NULL;
    TimeTable    *pttTrainStationB = NULL;
   
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
        //< Read turnaround time
        fscanf(pFile, "%d", &uiTurnAround);
        //< Read the number of trips
        fscanf(pFile, "%d %d", &uiNA, &uiNB);

        pttTrainStationA = new TimeTable();
        CPR(pttTrainStationA);
        pttTrainStationA->iTime = -1;

        pttTrainStationB = new TimeTable();
        CPR(pttTrainStationB);
        pttTrainStationB->iTime = -1;

        //< Read all departing and arrivals from the A train station, and fill our list
        for (int jStep = 0; jStep < uiNA; jStep++)
        {
            fscanf(pFile, "%d:%d %d:%d", &iDepartH, &iDepartM, &iArrivalH, &iArrivalM);
            iDepartTime  = iDepartH * 60 + iDepartM;
            iArrivalTime = iArrivalH * 60 + iArrivalM;

            AddDepartArrivalTime(pttTrainStationA, iDepartTime, true);
            AddDepartArrivalTime(pttTrainStationB, iArrivalTime + uiTurnAround, false);
        }

        //< Read all departing and arrivals from the B train station, and fill our list
        for (int jStep = 0; jStep < uiNB; jStep++)
        {
            fscanf(pFile, "%d:%d %d:%d", &iDepartH, &iDepartM, &iArrivalH, &iArrivalM);
            iDepartTime  = iDepartH * 60 + iDepartM;
            iArrivalTime = iArrivalH * 60 + iArrivalM;

            AddDepartArrivalTime(pttTrainStationB, iDepartTime, true);
            AddDepartArrivalTime(pttTrainStationA, iArrivalTime + uiTurnAround, false);
        }

        MergeTrains(pttTrainStationA);
        MergeTrains(pttTrainStationB);

        iTrainCountA = CountTrains(pttTrainStationA);
        iTrainCountB = CountTrains(pttTrainStationB);

        fprintf(pOutputFile, "Case #%d: %d %d\n", iStep + 1, iTrainCountA, iTrainCountB);

        Cleanup(pttTrainStationA);
        Cleanup(pttTrainStationB);
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



/******************************************************************************
* Name:   AddDepartArrivalTime
* Desc:   Add a new departing or arriving time
* Args:   TimeTable *pttTrainStation - TimeTable where to add
*         int iTime                  - Time of the departing/arrival
*         bool bDeparting            - If true, the trains is a departing train, if not is an arriving train
* Return: int value result
******************************************************************************/
void AddDepartArrivalTime(TimeTable *pttTrainStation, int iTime, bool bDeparting)
{
    TimeTable *pttIteration = NULL;
    bool      bFounded      = false;
    TimeTable *pttTempItem  = NULL;

    //< Try to find the specified time or the closest one
    pttIteration = pttTrainStation;
    do
    {
        //< We found an exact match, just increase the number of required trains
        if (pttIteration->iTime == iTime)
        {
            bFounded = true;
            if (true == bDeparting)
            {
                pttIteration->uiTrainsNeeded++;
            }
            else
            {
                pttIteration->uiTrainsAvailabile++;
            }
        }
        else
        {
            if (pttIteration->iTime > iTime)
            {
                //< We are to far in our list, insert in front of the current item
                pttTempItem = new TimeTable();
                CPR(pttTempItem);

                pttTempItem->iTime                 = iTime;
                if (true == bDeparting)
                {
                    pttTempItem->uiTrainsNeeded     = 1;
                }
                else
                {
                    pttTempItem->uiTrainsAvailabile = 1;
                }

                //< Edit linking
                pttTempItem->pttNextItem  = pttIteration;
                pttTempItem->pttPrevItem  = pttIteration->pttPrevItem;
                pttIteration->pttPrevItem = pttTempItem;
                if (NULL != pttTempItem->pttPrevItem)
                {
                    pttTempItem->pttPrevItem->pttNextItem = pttTempItem;
                }
                bFounded = true;
            }
        }

        //< If there are no more items and we didnt add our item, we should add it
        if ((NULL == pttIteration->pttNextItem) && (false == bFounded))
        {
            pttTempItem = new TimeTable();
            CPR(pttTempItem);

            pttTempItem->iTime                 = iTime;
            if (true == bDeparting)
            {
                pttTempItem->uiTrainsNeeded     = 1;
            }
            else
            {
                pttTempItem->uiTrainsAvailabile = 1;
            }

            //< Edit linking
            pttIteration->pttNextItem  = pttTempItem;
            pttTempItem->pttNextItem   = NULL;
            pttTempItem->pttPrevItem   = pttIteration;

            bFounded = true;
        }

        //< Go to the next item
        pttIteration = pttIteration->pttNextItem;
    }
    while ((NULL != pttIteration) && (false == bFounded));

Error:
    return;
}



/******************************************************************************
* Name:   MergeTrains
* Desc:   Eliminate the trains that are avialabile and the needed ones
* Args:   IN TimeTable *pttTrainStation - TimeTable to alalize
* Return: None
******************************************************************************/
void MergeTrains(TimeTable *pttTrainStation)
{
    TimeTable *pttIteration  = NULL;
    TimeTable *pttFirstItem  = NULL;
    TimeTable *pttSecondItem = NULL;
    bool      bFounded       = false;

    do
    {
        bFounded      = false;
        pttFirstItem  = NULL;
        pttSecondItem = NULL;
        pttIteration  = pttTrainStation;
        do
        {
            if (-1 != pttIteration->iTime)
            {
                if (pttIteration->uiTrainsAvailabile > 0)
                {
                    pttFirstItem  = pttIteration;
                    pttSecondItem = NULL;             //< Allways the availabile train should be the first one
                }
                
                if (pttIteration->uiTrainsNeeded > 0)
                {
                    pttSecondItem = pttIteration;
    
                    if (NULL != pttFirstItem)
                    {
                        bFounded = true;
                        pttFirstItem->uiTrainsAvailabile--;
                        pttSecondItem->uiTrainsNeeded--;
                        pttFirstItem = NULL;
                        pttSecondItem = NULL;
                    }
                }
            }
            //< Go to the next item
            pttIteration = pttIteration->pttNextItem;
        }
        while ((NULL != pttIteration) && (false == bFounded));
    }
    while (true == bFounded);
}



/******************************************************************************
* Name:   CountTrains
* Desc:   Count trains needed
* Args:   IN TimeTable *pttTrainStation - TimeTable to count
* Return: int value result with the number of trains
******************************************************************************/
int CountTrains(TimeTable *pttTrainStation)
{
    int       iTrains       = 0;
    TimeTable *pttIteration = NULL;

    pttIteration = pttTrainStation;
    do
    {
        if (-1 != pttIteration->iTime)
        {
            iTrains += pttIteration->uiTrainsNeeded;
        }
        //< Go to the next item
        pttIteration = pttIteration->pttNextItem;
    }
    while (NULL != pttIteration);

    return iTrains;
}



/******************************************************************************
* Name:   Cleanup
* Desc:   Cleanup one traintable
* Args:   IN TimeTable *pttTrainStation - TimeTable to clear
* Return: None
******************************************************************************/
void Cleanup(TimeTable *pttTrainStation)
{
    TimeTable *pttIteration = NULL;
    TimeTable *pttTempItem  = NULL;

    pttIteration = pttTrainStation;
    do
    {
        pttTempItem = pttIteration;

        //< Go to the next item
        pttIteration = pttIteration->pttNextItem;

        DELETE_OBJ(pttTempItem);
    }
    while (NULL != pttIteration);
}
