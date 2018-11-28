#include <windows.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>

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
int pair(char low, char high)
{
	return (int)low + ((int)high << 8);
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

		typedef std::map<int,char> MAP;
		MAP mapCombine;
		MAP mapOpposite;

		int i = 0;
		int n = atoi(g_Arg[i++]);
		while (n-- > 0)
		{
			char* ps = g_Arg[i];
			mapCombine[pair(ps[0], ps[1])] = ps[2];
			mapCombine[pair(ps[1], ps[0])] = ps[2];
			i++;
		}
		n = atoi(g_Arg[i++]);
		while (n-- > 0)
		{
			char* ps = g_Arg[i];
			mapOpposite[pair(ps[0], ps[1])] = 0;
			mapOpposite[pair(ps[1], ps[0])] = 0;
			i++;
		}

		n = atoi(g_Arg[i++]);
		char* ps = g_Arg[i];

		char* buf = new char[n];
		i = 0;

		while (n-- > 0)
		{
			char c = *ps++;

			int k = i - 1;
			for (; k >= 0; k--)
			{
				int npair = pair(buf[k], c);
				if (k == i - 1)
				{
					MAP::iterator itr = mapCombine.find(npair);
					if (itr != mapCombine.end())
					{
						buf[k] = itr->second;
						break;
					}
				}
				if (mapOpposite.find(npair) != mapOpposite.end())
				{
					i = 0; //k
					break;
				}
			}
			if (k < 0)
			{
				buf[i++] = c;
			}
		}

		printf("Case #%d: [", numCase);
		for (int k = 0; k < i; k++)
		{
			if (k > 0)
				printf(", ");
			printf("%c", buf[k]);
		}
		printf("]\n");

		delete [] buf;

		numCase++;
	}
	return 0;
}
