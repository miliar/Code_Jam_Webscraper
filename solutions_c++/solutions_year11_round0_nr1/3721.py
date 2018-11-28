#include <stdio.h>
#include <math.h>


int main()
{
//	freopen("in.in","r",stdin);freopen("out.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int moves[101];
	// 0 - orange
	// 1 - blue
	int* robotColor;
	robotColor = new int[101];

	int buttonsCount = 0;

	int testcase = 0;
	scanf("%d",&testcase);

	for (int caseId=1; caseId<=testcase; caseId++)
	{
		scanf("%d",&buttonsCount);

		int orangeMustPress = 0;
		int blueMustPress = 0;

		int orangePressed = 0;
		int bluePressed = 0; 

		for (int i = 0; i < buttonsCount; i++)
		{
			char s='O';
			scanf("%c",&s);
			scanf("%c",&s);

			if (s == 'O')
			{
				robotColor[i] = 0;
				orangeMustPress++;
			}
			else 
			{
				blueMustPress++;
				robotColor[i] = 1;
			}

			scanf("%d",&moves[i]);
		}

		int orangeWay = -1;
		int blueWay = -1;
		int orangePos = 1;
		int bluePos = 1;
		int orangeCurrentAim = 0;
		int blueaCurrentAim = 0;
		unsigned long long numSec = 0;

		bool isBlueMoved = false;
		bool isOrangeMoved = false;

		bool exit = false;
		bool k1 = true;
		bool k2 = true;

		do
		{
			numSec++;
			isBlueMoved = false;
			isOrangeMoved = false;

			for (int i = orangeCurrentAim; i <= buttonsCount; i++)
			{
				if (robotColor[i] == 0)
				{
					orangeCurrentAim = i;
					orangeWay = moves[i];
					break;
				}

				if (buttonsCount == i && robotColor[orangeCurrentAim] == 1)
				{
					orangeCurrentAim = 101;
				}
			}

			for (int i = blueaCurrentAim; i <= buttonsCount; i++)
			{
				if (robotColor[i] == 1)
				{
					blueaCurrentAim = i;
					blueWay = moves[i];
					break;
				}

				if (buttonsCount == i && robotColor[blueaCurrentAim] == 0)
				{
					blueaCurrentAim = 101;
				}
			}

			// orange
			if (orangeWay != (-1))
			{
				if (orangePos < orangeWay)
				{
					orangePos++;
					isOrangeMoved = true;
					//printf("orange moved to %d - %d", orangePos, numSec++);
				}
				else 
				{
					if (orangePos > orangeWay)
					{
						isOrangeMoved = true;
						orangePos--;
						//printf("orange moved to %d - %d", orangePos, numSec++);
					}
					else 
					{
						//printf("orange stoit at %d - %d", bluePos, numSec++);
					}
				}
			}

			// blue
			if (blueWay != (-1))
			{
				if (bluePos < blueWay)
				{
					isBlueMoved = true;
					bluePos++;
					//printf("blue moved to %d - %d", bluePos, numSec++);
				}
				else 
				{
					if (bluePos > blueWay)
					{
						isBlueMoved = true;
						bluePos--;
						//printf("blue moved to %d - %d", bluePos, numSec++);
					}
					else 
					{
						//printf("blue stoit at %d - %d", bluePos, numSec++);
					}
				}
			}

			if (orangeCurrentAim < blueaCurrentAim)
			{
				if (orangeWay == orangePos)
				{
					if (isOrangeMoved == false)
					{
						// push button
						orangeCurrentAim++;
						orangePressed++;
						//printf("orange pressed button - %dsec", numSec++);
					}
				}
			}
			else 
			{
				if (blueWay == bluePos)
				{
					if (isBlueMoved == false)
					{
						// push button
						blueaCurrentAim++;
						bluePressed++;
						//printf("Blue pressed button - %dsec", numSec++);
					}
				}
			}

			
			k1 = (bluePressed < blueMustPress);
			
			k2 = (orangePressed < orangeMustPress);

			exit = (k1) && (k2);
			if (k1 == false)
				if (k2 == false)
					break;
		} while(1);

		//int k = numSec;
		printf("Case #%d: %llu\n", caseId, numSec);
	}

	delete [] robotColor;
	return 0;
}