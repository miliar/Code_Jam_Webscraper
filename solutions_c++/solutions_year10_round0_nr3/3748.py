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

        __int64 R = _atoi64(g_Arg[0]);
        __int64 k = _atoi64(g_Arg[1]);
        int N = atoi(g_Arg[2]);

        ReadLine();

        typedef std::vector<__int64> GROUPS;
        GROUPS groups;

        for (int i = 0; i < N; i++)
        {
            groups.push_back(_atoi64(g_Arg[i]));
        }

        int n = 0;
        __int64 sum = 0;
        while (R > 0)
        {
            __int64 cap = 0;

            int pos = n;
            while (cap + groups[pos] <= k)
            {
                cap += groups[pos];
                pos++;
                if (pos >= N)
                    pos = 0;
                if (pos == n)
                    break;
            }

            sum += cap;
            R--;
            n = pos;
        }

		printf("Case #%d: %I64d\n", numCase, sum);

		numCase++;
	}
	return 0;
}
