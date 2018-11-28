#include <Windows.h>
#include <stdio.h>
#include <string.h>

int main()
{
	int T, N;
	int steps[2][100];
	int orangePos[100], nOrange;
	int bluePos[100], nBlue;
	int seconds;
	int Ocurrent, Bcurrent;
	char c;
	int k;
	int currentStep;
	bool moveNext;

	scanf("%d", &T);

	for(int test = 1; test <= T; test++)
	{
		seconds = 0;
		nOrange = 0;
		nBlue = 0;
		Ocurrent = 1;
		Bcurrent = 1;
		currentStep = 0;

		scanf("%d ", &N);

		for(int i = 0; i < N; i++)
		{
			scanf("%c%d ", &c, &k);

			if(c == 'O')
			{
				orangePos[nOrange] = k;
				nOrange++;
				steps[0][i] = 0;
			}
			else
			{
				bluePos[nBlue] = k;
				nBlue++;
				steps[0][i] = 1;
			}

			steps[1][i] = k;
		}
		
		int curO = 0, curB = 0;

		while(currentStep < N)
		{
			moveNext = false;

			// move Orange
			if(curO < nOrange) // if Orange has assignments
			{
				if(Ocurrent < orangePos[curO]) // move foward
				{
					Ocurrent++;
				}
				else if(Ocurrent > orangePos[curO]) // move backwards
				{
					Ocurrent--;
				}
				else if(steps[0][currentStep] == 0) // push button
				{
					moveNext = true;
					curO++;
				}
			}

			// move Blue
			if(curB < nBlue) // if Blue has assignments
			{
				if(Bcurrent < bluePos[curB]) // move foward
				{
					Bcurrent++;
				}
				else if(Bcurrent > bluePos[curB]) // move backwards
				{
					Bcurrent--;
				}
				else if(steps[0][currentStep] == 1) // push button
				{
					moveNext = true;
					curB++;
				}
			}

			if(moveNext)
				currentStep++;

			seconds++;
		}

		printf("Case #%d: %d\n", test, seconds);
	}

	return 0;
}