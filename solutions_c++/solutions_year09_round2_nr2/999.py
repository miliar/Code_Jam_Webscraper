#include <windows.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <functional>


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

int min1(int* arr, int len, int lev, int** pt)
{
	int n = 10;
	for (int i = 0; i < len; i++)
		if (arr[i] < n && arr[i] > lev)
		{
			n = arr[i];
			if (pt)
				*pt = &arr[i];
		}
	return (n < 10 ? n : 0);
}

void srt(int* arr, int len)
{
	for (int i = 0; i < len - 1; i++)
		for (int k = i + 1; k < len; k++)
			if (arr[k] < arr[i])
			{
				int n = arr[k];
				arr[k] = arr[i];
				arr[i] = n;
			}
}

void find_next(int* decimal, int& len)
{
	for (int i = len - 2; i >= 0; i--)
	{
		int n = decimal[i];
		int* pt;
		int x = min1(decimal + i + 1, len - i - 1, n, &pt);
		if (x > 0)
		{
			decimal[i] = *pt;
			*pt = n;
			srt(decimal + i + 1, len - i - 1);
			return;
		}
	}
	int* pt;
	int n = min1(decimal, len, 0, &pt);
	*pt = 0;
	for (int i = len; i > 0; i--)
		decimal[i] = decimal[i - 1];
	decimal[0] = n;
	srt(decimal + 1, len);
	len++;
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

		int decimal[32];
		char* ps = g_Arg[0];
		int len = strlen(ps);
		for (UINT i = 0; i < len; i++)
			decimal[i] = ps[i] - '0';

		find_next(decimal, len);

		printf("Case #%d: ", numCase);
		for (int i = 0; i < len; i++)
			printf("%c", decimal[i] + '0');
		printf("\n", numCase);

		numCase++;
	}
	return 0;
}
