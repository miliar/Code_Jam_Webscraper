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

int* g_pMatrix;
int* g_pLabel;
int g_width;
int g_height;
typedef std::vector<POINT> ROUTE;

void ReadLine()
{
	g_Arg.clear();
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

int get(int* pMatrix, int x, int y)
{
	return pMatrix[y * g_width + x];
}

void set(int* pMatrix, int x, int y, int c)
{
	pMatrix[y * g_width + x] = c;
}

void walk(int x, int y, int& label)
{
	ROUTE r;

	while(true)
	{
		POINT pt = {x, y};
		r.push_back(pt);

		int alt = get(g_pMatrix, x, y);
		int dx = 0, dy = 0;

		// Select direction
		if (y > 0 && get(g_pMatrix, x, y - 1) < alt)
		{
			dx = 0; dy = -1; alt = get(g_pMatrix, x, y - 1);
		}
		if (x > 0 && get(g_pMatrix, x - 1, y) < alt)
		{
			dx = -1; dy = 0; alt = get(g_pMatrix, x - 1, y);
		}
		if (x < g_width - 1 && get(g_pMatrix, x + 1, y) < alt)
		{
			dx = 1; dy = 0; alt = get(g_pMatrix, x + 1, y);
		}
		if (y < g_height - 1 && get(g_pMatrix, x, y + 1) < alt)
		{
			dx = 0; dy = 1; alt = get(g_pMatrix, x, y + 1);
		}

		if (dx == 0 && dy == 0)
		{
			// This is a sink, mark all items in the route with a new label
			label++;
			for (int i = 0; i < r.size(); i++)
				set(g_pLabel, r[i].x, r[i].y, label);
			return;
		}

		// Move to the next item
		x += dx; y += dy;

		int l = get(g_pLabel, x, y);
		if (l > 0)
		{
			// Next item is already labeled, use its label for the whole route
			for (int i = 0; i < r.size(); i++)
				set(g_pLabel, r[i].x, r[i].y, l);
			return;
		}
	}
}

void scan()
{
	int x = 0;
	int y = 0;
	int label = 'a' - 1;

	ZeroMemory(g_pLabel, g_width * g_height * sizeof(g_pLabel[0]));

	for (int y = 0; y < g_height; y++)
	{
		for (int x = 0; x < g_width; x++)
		{
			// If labeled - skip
			if (get(g_pLabel, x, y) > 0)
				continue;

			// If not labeled - scan route
			walk(x, y, label);
		}
	}

	for (int y = 0; y < g_height; y++)
		for (int x = 0; x < g_width; x++)
		{
			printf("%c", get(g_pLabel, x, y));
			if (x == g_width - 1)
				printf("\n");
			else
				printf(" ");
		}
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return 0;

	g_hFile = fopen(argv[1], "r");

	char result[MAX_BUFFER_LENGTH];

	ReadLine();
	int nCount = atoi(g_Arg[0]);
	int numCase = 1;
	while (numCase <= nCount)
	{
		ReadLine();
		g_height = atoi(g_Arg[0]);
		g_width = atoi(g_Arg[1]);

		g_pMatrix = new int[g_height * g_width];
		g_pLabel = new int[g_height * g_width];

		for (int y = 0; y < g_height; y++)
		{
			ReadLine();
			for (int x = 0; x < g_width; x++)
			{
				int n = atoi(g_Arg[x]);
				set(g_pMatrix, x, y, n);
			}
		}

		printf("Case #%d:\n", numCase);

		scan();

		delete [] g_pMatrix;
		delete [] g_pLabel;
		numCase++;
	}
	return 0;
}
