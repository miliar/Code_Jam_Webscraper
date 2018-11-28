#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;

    FILE *fp = NULL ;
    fstream inputFile;
    ofstream outputFile;


bool GetNumberofCases(int *TotalNoCases)
{
    string s1;
    inputFile.getline((char*)s1.c_str(),80);
    *TotalNoCases = atoi(s1.c_str());
    return true;
}

bool GetTurnAroundTime(int *TurnAroundTime)
{
    string s1;
    inputFile.getline((char*)s1.c_str(),80);
    *TurnAroundTime = atoi(s1.c_str());
    return true;
}

bool GetNumTrips(int *NA, int *NB)
{
    string s1;
    inputFile.getline((char*)s1.c_str(),80);
    *NA = atoi(strtok((char*)s1.c_str()," "));
    *NB = atoi(strtok(NULL," "));

    return true;
}

bool GetTripDetails(int *dt, int *at, int turnaroundtime)   
{

    string s1;
    inputFile.getline((char*)s1.c_str(),80);

    *dt = ( atoi(strtok((char*)s1.c_str()," :")) ) * 60 ;
    *dt += atoi(strtok(NULL," :"));

    *at = ( atoi(strtok(NULL," :")) ) * 60;
    *at += atoi(strtok(NULL," :"));
    *at += turnaroundtime ;

    return true;
}

bool Sort(int *arr, int Num)
{
    int temp ;
    for(int i = 0; i < Num - 1 ; i++)
    {
        for(int j = i+1 ; j < Num  ; j++)
        {
            if(arr[i] > arr[j] )
            {
                temp = arr[i] ;
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    return true ;
}

void main(int argc, char*argv[])
{
    int TotalNoCases = 0;
    int TurnAroundTime = 0;
    int NA, NB ;
    int *DTA, *ATA, *DTB, *ATB;


    inputFile.open(argv[1]);
    GetNumberofCases(&TotalNoCases);

    outputFile.open(argv[2]);

    for(int i = 0; i < TotalNoCases; i++ )
    {

        int TrainsA = 0, TrainsB = 0;
        int OldTrainA = 0, OldTrainB = 0;

        printf("CASE %d\n",i );
        GetTurnAroundTime(&TurnAroundTime);
        GetNumTrips(&NA, &NB);

        DTA = (int*) malloc(sizeof(int)*NA);
        ATB = (int*) malloc(sizeof(int)*NA);

        DTB = (int*) malloc(sizeof(int)*NB);
        ATA = (int*) malloc(sizeof(int)*NB);

        for(int j = 0; j < NA; j++)
        {
            GetTripDetails(&DTA[j], &ATB[j], TurnAroundTime);
            printf("A to B - DTA = %d, ATB = %d\n",DTA[j], ATB[j] );
        }
        for(int k = 0; k < NB; k++) 
        {
            GetTripDetails(&DTB[k], &ATA[k], TurnAroundTime);
            printf("B to A - DTA = %d, ATB = %d\n",DTB[k], ATA[k] );
        }

        Sort(DTA, NA);
        printf("\nDTA ");
        for(int tt = 0; tt < NA; tt++)
        {
            printf("%d ",DTA[tt]);
        }

        Sort(ATB, NA);
        printf("\n ATB ");
        for(int tt = 0; tt < NA; tt++)
        {
            printf("%d ",ATB[tt]);
        }

        Sort(DTB, NB);
        printf("\n DTB ");
        for(int tt = 0; tt < NB; tt++)
        {
            printf("%d ",DTB[tt]);
        }

        Sort(ATA, NB);
        printf("\n ATA ");
        for(int tt = 0; tt < NB; tt++)
        {
            printf("%d ",ATA[tt]);
        }
        printf("\n");

        for(int m = 0; m < NA; m++)
        {
            if(OldTrainA < NB)
            {
                if(DTA[m] >= ATA[OldTrainA])
                {
                    OldTrainA++;
                }
                else
                {
                    TrainsA++ ;
                }
            }
            else
            {
                TrainsA++ ;
            }
        }

        printf("\nTrains at Station A = %d\n", TrainsA);

        for(int n = 0; n < NB; n++)
        {
            if(OldTrainB < NA)
            {
                if(DTB[n] >= ATB[OldTrainB])
                {
                    OldTrainB++;
                }
                else
                {
                    TrainsB++ ;
                }
            }
            else
            {
                TrainsB++ ;
            }
        }

        printf("\nTrains at Station B = %d\n", TrainsB);

        int ncase = i + 1 ;
        outputFile << "Case #" << ncase << ": " << TrainsA << " " <<TrainsB << endl ;

        free(DTA);
        free(ATA);
        free(DTB);
        free(ATB);

    }

    inputFile.close();
    outputFile.close();

}