// Google Code Jam 2011 - Qualification Round
// by vdave, Hungary, 2011

#include <cstdio>


////////////////////////
// PROBLEM A - BOT TRUST
////////////////////////


char robotID[8];
int isOrange[128];
int buttonIndex[128];

int A_main(int argc, char *argv[])
{
	int T;

	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		int resVal = -1;
		
		int N, btnIndex;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%s %d", robotID, &btnIndex);
			buttonIndex[i] = btnIndex;
			isOrange[i] = robotID[0] == 'O';
		}

		int posO = 1, posB = 1, nextAction = 0, currentTime = 0;
		while (nextAction < N)
		{
			int nextO = posO;
			for (int i = nextAction; i < N; ++i)
			{
				if (isOrange[i])
				{
					nextO = buttonIndex[i];
					break;
				}
			}

			int nextB = posB;
			for (int i = nextAction; i < N; ++i)
			{
				if (!isOrange[i])
				{
					nextB = buttonIndex[i];
					break;
				}
			}

			bool buttonPressed = false;
			
			if (posO < nextO)
				posO++;
			else if (posO > nextO)
				posO--;
			else if (posO == nextO && isOrange[nextAction])
				buttonPressed = true;
			
			if (posB < nextB)
				posB++;
			else if (posB > nextB)
				posB--;
			else if (posB == nextB && !isOrange[nextAction])
				buttonPressed = true;

			if (buttonPressed)
				nextAction++;
			currentTime++;
		}
		resVal = currentTime;

		printf("Case #%d: %d\n", tc, resVal);
	}

	return 0;
}


int main(int argc, char *argv[])
{
	return A_main(argc, argv);
}