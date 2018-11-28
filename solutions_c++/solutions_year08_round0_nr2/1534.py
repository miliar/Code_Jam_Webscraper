#include <stdio.h>
#include <malloc.h>

void bubbleSort(int *array, int length)
{
  int i, j, temp;
  int test; 
  for(i = length - 1; i > 0; i--)
  {
    test=0;
    for(j = 0; j < i; j++)
    {
      if(array[j] > array[j+1]) 
      {
        temp = array[j];    
        array[j] = array[j+1];
        array[j+1] = temp;
        test=1;
      }
    } 
    if(test==0) break; 
  } 
      
}

int getTrains(int *startTimes, int startTimeCount, int *arrTimes, int arrivalTimeCount, int turnAround)
{
    int trainCount = 0;
    int i = 0, j = 0;

    for(;i < startTimeCount ; i++)
    {
        bool flag = false;

        for(j = 0;j < arrivalTimeCount; j++)
        {
	    if(arrTimes[j] != -1)
	    {
            	if(startTimes[i] >= arrTimes[j] + turnAround )
            	{
			arrTimes[j] = -1;
                	flag = true;
                	break;
            	}
	     }
        }

        if(false == flag)
        {
            trainCount++;
        }
    }

    return trainCount;
}


void getTrainSchedule(FILE *inputFile, int turnAround, int *trainFromA, int *trainFromB)
{
    int NA = 0;
    int NB = 0;
    int i = 0;
    
    
    int startHour = 0;
    int startMin = 0;
    int arrHour = 0;
    int arrMin = 0;

    int startTime = 0;
    int arrTime = 0;
    
    fscanf(inputFile, "%d %d\n", &NA, &NB);

    if(NA == 0 || NB == 0)
    {
        *trainFromB = NB;
        *trainFromA = NA;
    }
    else
    {
            int *startTimeForA = (int *)malloc(sizeof(int) * NA);
            int *arrTimeFromA = (int *)malloc(sizeof(int) * NA);
            int *startTimeForB = (int *)malloc(sizeof(int) * NB);
            int *arrTimeFromB = (int *)malloc(sizeof(int) * NB);

            for(;i < NA; i++)
            {
                fscanf(inputFile, "%d:%d %d:%d", &startHour,&startMin,  &arrHour, &arrMin);
                startTime = startHour * 60 + startMin;
                arrTime = arrHour * 60 + arrMin;

                startTimeForA[i] = startTime;
                arrTimeFromA[i] = arrTime;
            }

            for(i = 0 ;i < NB; i++)
            {
                fscanf(inputFile, "%d:%d %d:%d", &startHour,&startMin,  &arrHour, &arrMin);

                startTime = startHour * 60 + startMin;
                arrTime = arrHour * 60 + arrMin;
                startTimeForB[i] = startTime;
                arrTimeFromB[i] = arrTime;
            }
 		
	    bubbleSort(startTimeForA, NA);           
	    bubbleSort(arrTimeFromA, NA);
           
	    bubbleSort(startTimeForB, NB);           
	    bubbleSort(arrTimeFromB, NB);
            *trainFromA = getTrains(startTimeForA, NA, arrTimeFromB, NB, turnAround);
            *trainFromB = getTrains(startTimeForB, NB, arrTimeFromA, NA, turnAround);

            delete startTimeForA;
            delete arrTimeFromA ;
            delete startTimeForB;
            delete arrTimeFromB;
    }
}

void runTestCase(FILE *inputFile, FILE* outFile)
{
    int i = 0;

    int testCaseCount = 0;
    
    int turnAround = 0;
    int trainFromA = 0;
    int trainFromB = 0;

    fscanf(inputFile, "%d\n", &testCaseCount);
    //printf("Testcase count is %d\n", testCaseCount);

    i = 1;
    for(;i <= testCaseCount; i++)
    {
        int switchCount = 0;
	    
        fscanf(inputFile, "%d\n", &turnAround);

        getTrainSchedule(inputFile, turnAround, &trainFromA, &trainFromB);
        
        fprintf(outFile, "Case #%d: %d %d\n", i, trainFromA, trainFromB);
    }

}

int main(int argc, const char** argv)
{
    if(argc < 3)
    {
        printf("Wrong number of arguments. Usage: train input_filename output_filename \n");
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
