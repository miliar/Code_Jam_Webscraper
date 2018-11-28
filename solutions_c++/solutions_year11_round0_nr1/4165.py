#include <iostream>
#include <cstdio>
#include <cstdlib>

typedef struct
{
	bool isBlue;
	int nextButton;
} button;

#define min(a,b) ((a)<(b)?(a):(b))

void nextIndices (const button* button, int numButtons, int& blue, int& orange)
{
	blue = -1;
	orange = -1;
	for (int i = 0; i < numButtons; i++)
	{
		if (blue == -1 && button[i].isBlue) blue = i;
		if (orange == -1 && !button[i].isBlue) orange = i;
		if (blue > -1 && orange > -1) break;
	}
}

int main()
{
	char* buffer = new char[1000];
	std::cin.getline(buffer, 1000);
	int numTests = strtol(buffer, NULL, 10);
	for (int test = 1; test <= numTests; test++)
	{
		std::cin.getline(buffer, 1000);
		char* tmpBuf = buffer;
		int numSteps = strtol(tmpBuf, &tmpBuf, 10);
		button* buttons = new button[numSteps];
		for (int i = 0; i < numSteps; i++)
		{
			tmpBuf++;
			buttons[i].isBlue = (*tmpBuf == 'B');
			tmpBuf += 2;
			buttons[i].nextButton = strtol(tmpBuf, &tmpBuf, 10);
		}

		int nextBlue, nextOrange;
		int blueLoc = 1, orangeLoc = 1;
		int totalTime = 0;

		for (int i = 0; i < numSteps; i++)
		{
			nextIndices(buttons+i, numSteps-i, nextBlue, nextOrange);
			nextBlue += i;
			nextOrange += i;
			int diff = abs(buttons[i].nextButton - (buttons[i].isBlue ? blueLoc : orangeLoc)) + 1;
			int blueDiff = abs(buttons[nextBlue].nextButton - blueLoc);
			blueLoc += (blueLoc < buttons[nextBlue].nextButton ? 1 : -1) * min(diff, blueDiff);
			int orangeDiff = abs(buttons[nextOrange].nextButton - orangeLoc);
			orangeLoc += (orangeLoc < buttons[nextOrange].nextButton ? 1 : -1) * min(diff, orangeDiff);
			totalTime += diff;
		}

		printf("Case #%d: %d\n", test, totalTime);
		delete buttons;
	}
	delete buffer;
}
