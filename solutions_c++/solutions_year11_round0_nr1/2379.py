#include <iostream>
#include <stdio.h>
#include <math.h>


using namespace std;

int solveCase(int numberOfButtons);

int main()
{
    FILE *fp = fopen("output.txt", "w");

    int numberOfCases;
    fscanf(stdin, "%d", &numberOfCases);
    //printf("Lei %d casos\n", numberOfCases);
    for(int caseN = 0; caseN < numberOfCases; caseN++)
    {
        int numberOfButtons;
        fscanf(stdin, "%d", &numberOfButtons);
        //printf("El caso %d tiene %d botones\n", caseN, numberOfButtons);

        int result = solveCase(numberOfButtons);
        fprintf(fp, "Case #%d: %d\n", (caseN + 1), result);
    }

    return 0;
}

int solveCase(int numberOfButtons)
{
    int result = 0;

    int orangeTime = 0;
    int orangePosition = 1;

    int blueTime = 0;
    int bluePosition = 1;

    for(int i=0; i < numberOfButtons; i++)
    {
        char color[10];
        int number;

        fscanf(stdin, "%s %d", color, &number);
        //printf("Saque boton %s %d\n", color, number);

        if(color[0] == 'O')
        {
            int timeToCompleteTask = fabs(number - orangePosition) + 1;
            orangePosition = number;

            orangeTime += timeToCompleteTask;
            if(orangeTime <= blueTime) orangeTime = blueTime + 1;

            //printf("Orange presiona %d en el segundo %d\n", number, orangeTime);
        }
        else if(color[0] == 'B')
        {
            int timeToCompleteTask = fabs(number - bluePosition) + 1;
            bluePosition = number;

            blueTime += timeToCompleteTask;
            if(blueTime <= orangeTime) blueTime = orangeTime + 1;

            //printf("blue presiona %d en el segundo %d\n", number, blueTime);
        }
        //printf("Orange: but %d, time %d\n", orangePosition, orangeTime);
        //printf("Blue: but %d, time %d\n", bluePosition, blueTime);
    }

    result = max(blueTime, orangeTime);
    return result;
}

