#include <windows.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

typedef vector<char*> DICTIONARY;
DICTIONARY dict;
struct SYMBOL
{
	char c;
	char* pChars;
};
typedef vector<SYMBOL> SYMBOLS;

int g_count;

#define MAX_BUFFER_LENGTH 65536
typedef std::vector<char*> ARG;
FILE* g_hFile;
ARG g_Arg;
char g_buf[MAX_BUFFER_LENGTH];

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

bool ulower(char* elem1, char* elem2)
{
	return strcmp(elem1, elem2) < 0;
}

bool compare(char* str, SYMBOLS& sym)
{
	for (UINT i = 0; i < sym.size(); i++)
	{
		if (sym[i].c > 0)
		{
			if (str[i] != sym[i].c)
				return false;
		}
		else
		{
			if (!strchr(sym[i].pChars, str[i]))
				return false;
		}
	}
	return true;
}

void scan(SYMBOLS& sym)
{
	for (UINT i = 0; i < dict.size(); i++)
	{
		if (compare(dict[i], sym))
			g_count++;
	}
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return 0;

	g_hFile = fopen(argv[1], "r");

	ReadLine();
	int nWordLen = atoi(g_Arg[0]);
	int nDictSize = atoi(g_Arg[1]);
	int nCount = atoi(g_Arg[2]);

	// Create dictionary
	for (int i = 0; i < nDictSize; i++)
	{
		ReadLine();
		int len = (int)strlen(g_Arg[0]);
		char* ps = new char[len+1];
		strcpy(ps, g_Arg[0]);
		dict.push_back(ps);
	}

	sort(dict.begin(), dict.end(), ulower);

	int numCase = 1;
	while (numCase <= nCount)
	{
		// Parse pattern
		ReadLine();

		SYMBOLS sym;

		char* ps = g_Arg[0];
		while (*ps)
		{
			SYMBOL symb;
			symb.c = 0;
			symb.pChars = NULL;

			if (*ps == '(')
			{
				symb.pChars = ++ps;
				while (*ps != ')')
					ps++;
				*ps++ = 0;
			}
			else
				symb.c = *ps++;

			sym.push_back(symb);
		}

		g_count = 0;
		scan(sym);

		printf("Case #%d: %d\n", numCase, g_count);

		numCase++;
	}

	for (UINT i = 0; i < dict.size(); i++)
		delete (dict[i]);

	return 0;
}
