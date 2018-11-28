#include <stdio.h>
#include <conio.h>
#include <math.h>

void main ()
{
	FILE* pRFile = fopen("A-large.in", "rt");

	if(!pRFile)
	{
		printf("Cannot open file for reading");
		getch();
		return;
	}

	FILE* pWFile = fopen("A-large.out", "wt");
	
	if(!pWFile)
	{
		printf("Cannot open file for writing");
		fclose(pRFile);
		getch();
		return;
	}

	int t, n, i, j;
	int timer = 0, time2move, timeDelta, timeDeltaSum;	//manage time
	int button, buttonB, buttonO, *pButton;	//manage button
	char robotID, currentRobotID;	//manage robot
	const char ROBOT_B = 'B';
	const char ROBOT_O = 'O';

	fscanf(pRFile, "%d\n", &t);

//	printf("t = %d\n", t);	//test

	for(i = 1; i <= t; i++)
	{
		timer = 0, timeDelta = 0;	//init
		timeDeltaSum = 0;	//init
		currentRobotID = 'X';	//init
		buttonB = 1;	//init
		buttonO = 1;	//init
		pButton = NULL;	//init

		fscanf(pRFile, "%d", &n);

//		printf("n = %d\n", n);	//test

		for(j = 0; j < n; j++)
		{
			fscanf(pRFile, " %c", &robotID);
			fscanf(pRFile, " %d", &button);

//			printf("robotID = %c, button = %d\n", robotID, button);	//test

			if(robotID != currentRobotID)
			{
				currentRobotID = robotID;

				if(currentRobotID == ROBOT_B)
				{
					pButton = &buttonB;
				}
				else if(currentRobotID == ROBOT_O)
				{
					pButton = &buttonO;
				}

				time2move = abs(*pButton - button);	//time to move
				*pButton = button;	//set the current button

				timeDelta = time2move - timeDeltaSum;	//when a robot moves,
														//the other robot also moves
				if(timeDelta < 0)
					timeDelta = 0;	//waiting for the other robot

				timeDelta += 1;	//time to press

				timeDeltaSum = timeDelta;	//reset time aggregation

				timer += timeDelta;	//add to timer
			}
			else
			{
				timeDelta = abs(*pButton - button);	//time to move
				*pButton = button;	//set the current button

				timeDelta += 1;	//time to press

				timeDeltaSum += timeDelta;	//add to time aggregation of the robot

				timer += timeDelta;	//add to timer
			}
		}

		fprintf(pWFile, "Case #%d: %d\n", i, timer);
	}

	pButton = NULL;

	fclose(pRFile);
	fclose(pWFile);

	printf("Successful");
	getch();
}