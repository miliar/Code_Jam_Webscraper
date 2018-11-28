#include <windows.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>

#define MAX_BUFFER_LENGTH 65536
typedef std::vector<char*> ARG;
FILE* g_hFile;
ARG g_Arg;
char g_buf[MAX_BUFFER_LENGTH];

void ReadLine()
{
	g_Arg.clear();
	g_buf[0] = 0;
	fgets(g_buf, MAX_BUFFER_LENGTH, g_hFile);

	char* ps = g_buf;
	bool b = true;
	while (b)
	{
		while (*ps == '\t' || *ps == ' ')
			ps++;

		char* pStart = ps;

		while (*ps != '\r' && *ps != '\n' && *ps != '\0' && *ps != ' ')
			ps++;

		if (ps != pStart)
			g_Arg.push_back(pStart);

		b = (*ps == '\t' || *ps == ' ');
		*ps++ = 0;
	}
}

char getrobot(int btn)
{
	return (g_Arg[btn * 2 - 1])[0];
}

char getpos(int btn)
{
	return atoi(g_Arg[btn * 2]);
}

int nextpos(char cRobot, int curInd, int nButtons)
{
	for (int n = curInd + 1; n <= nButtons; n++)
	{
		if (getrobot(n) == cRobot)
			return n;
	}
	return curInd;
}

void move(int& pos, int nextpos)
{
	if (pos > nextpos)
		pos--;
	else if (pos < nextpos)
		pos++;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return 0;

	g_hFile = fopen(argv[1], "r");

	ReadLine();
	int nCount = atoi(g_Arg[0]);
	int numCase = 1;
	while (numCase <= nCount)
	{
		ReadLine();

		int nButtons = atoi(g_Arg[0]);

		int posO, posB;
		posO = posB = 1;

		int indO = nextpos('O', 0, nButtons);
		int indB = nextpos('B', 0, nButtons);

		int indBtn = 1;
		int sec = 0;

		while (indBtn <= nButtons)
		{
			bool pressO, pressB;
			pressO = pressB = false;

			if (getrobot(indBtn) == 'O')
			{
				if (posO == getpos(indBtn))
				{
					indBtn++;
					indO = nextpos('O', indO, nButtons);
					pressO = true;
				}
			}
			else // 'B'
			{
				if (posB == getpos(indBtn))
				{
					indBtn++;
					indB = nextpos('B', indB, nButtons);
					pressB = true;
				}
			}

			if (!pressO)
				move(posO, getpos(indO));
			if (!pressB)
				move(posB, getpos(indB));

			sec++;
		}
		printf("Case #%d: %d\n", numCase, sec);

		numCase++;
	}
	return 0;
}
