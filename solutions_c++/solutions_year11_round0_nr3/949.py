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





//////////////////////
// PROBLEM B - MAGICKA
//////////////////////

char combine[128][4];
int opposeMask[128];
char sourceList[512];
char targetList[512];
int targetLength = 0;

int B_main(int argc, char *argv[])
{
	int T;

	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		int C, D, N;
		scanf("%d", &C);
		for (int i = 0; i < C; ++i)
		{
			scanf("%s", combine[i]);
		}

		scanf("%d", &D);
		for (int i = 0; i < D; ++i)
		{
			scanf("%s", combine[127]);
			opposeMask[i] = (1 << (combine[127][0] - 'A')) | (1 << (combine[127][1] - 'A'));
		}

		scanf("%d", &N);
		scanf("%s", sourceList);
		targetLength = 0;

		for (int i = 0; i < N; ++i)
		{
			char ch1 = sourceList[i];
			if (targetLength == 0)
			{
				targetList[0] = ch1;
				targetLength = 1;
			}
			else
			{
				char ch2 = targetList[targetLength - 1];
				char chc = '#';
				for (int c = 0; c < C; ++c)
				{
					if (combine[c][0] == ch1 && combine[c][1] == ch2)
					{
						chc = combine[c][2];
					}
					if (combine[c][0] == ch2 && combine[c][1] == ch1)
					{
						chc = combine[c][2];
					}
				}

				if (chc != '#')
				{
					targetList[targetLength - 1] = chc;
				}
				else
				{
					targetList[targetLength] = ch1;
					targetLength++;

					int charMask = 0;
					for (int j = 0; j < targetLength; ++j)
					{
						charMask |= 1 << (targetList[j] - 'A');
					}

					for (int d = 0; d < D; ++d)
					{
						if ((charMask & opposeMask[d]) == opposeMask[d])
							targetLength = 0;
					}
				}
			}
		}

		printf("Case #%d: [", tc);
		for (int i = 0; i < targetLength; ++i)
		{
			if (i > 0)
				printf(", ");
			printf("%c", targetList[i]);
		}
		printf("]\n");
	}

	return 0;
}





//////////////////////////////
// PROBLEM C - CANDY SPLITTING
//////////////////////////////

int candyValues[4096];

int C_main(int argc, char *argv[])
{
	int T;

	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &candyValues[i]);
		}

		// Patrick: addition is XOR
		// Possible, if all XORed together gives 0, in that case Sean can have all but least valueable
		int resVal = -1, xorAll = 0, sumVal = 0, minVal = 999999999;
		for (int i = 0; i < N; ++i)
		{
			xorAll ^= candyValues[i];
			sumVal += candyValues[i];
			if (candyValues[i] < minVal)
				minVal = candyValues[i];
		}

		if (xorAll == 0)
		{
			resVal = sumVal - minVal;
		}

		if (resVal == -1)
		{
			printf("Case #%d: NO\n", tc);
		} else {
			printf("Case #%d: %d\n", tc, resVal);
		}
	}

	return 0;
}






int main(int argc, char *argv[])
{
	//return A_main(argc, argv);
	//return B_main(argc, argv);
	return C_main(argc, argv);
}