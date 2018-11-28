#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
using namespace std;

typedef signed char int8;
typedef unsigned char uint8;
typedef signed short int16;
typedef signed int int32;
typedef unsigned short uint16;
typedef unsigned int uint32;

#ifdef ASSERT_ENABLED
#define assert(a)	if (!(a)) { _asm { int 3h } }
#else
#define assert(a)
#endif

#define SAFE_DELETE(a) if ((a) != NULL) { delete a; a = NULL; }
#define SAFE_DELETE_ARRAY(a) if ((a) != NULL) { delete[] a; a = NULL; }

int32 LINE_SIZE;
char LINE[600];

const int32 PATTERN_SIZE = 19;
const char* PATTERN = "welcome to code jam";

int32 matchCount = 0;
void matchString(int32 lineIndex, int32 patternIndex)
{
	while (lineIndex < LINE_SIZE)
	{
		if (LINE[lineIndex] == PATTERN[patternIndex])
		{
			// Match
			if ((patternIndex + 1) < PATTERN_SIZE)
			{
				//matchCount += matchString(line, lineSize, lineIndex + 1, patternIndex + 1);
				matchString(lineIndex + 1, patternIndex + 1);
			}
			else
			{
				//return true;
				++matchCount;
				if (matchCount == 10000)
				{
					matchCount -= 10000;
				}
			}
		}
		//else
		//{
		//	++lineIndex;
		//}

		++lineIndex;
	}

	//return false;
}


bool matchString2(int32 lineIndex, int32 patternIndex)
{
	while (lineIndex < LINE_SIZE)
	{
		if (LINE[lineIndex] == PATTERN[patternIndex])
		{
			// Match
			if ((patternIndex + 1) < PATTERN_SIZE)
			{
				return matchString2(lineIndex + 1, patternIndex + 1);
			}
			else
			{
				return true;
			}
		}
		else
		{
			bool equalPreviousPattern = false;

			for (int32 i = 0; i < patternIndex; ++i)
			{
				if (LINE[lineIndex] == PATTERN[i])
				{
					equalPreviousPattern = true;
				}
			}

			if (!equalPreviousPattern)
			{
				LINE[lineIndex] = '7';
			}
		}
		//else
		//{
		//	++lineIndex;
		//}

		++lineIndex;
	}

	LINE[lineIndex] = '\0';

	return false;
}

void filterLine()
{
	char lineCopy[600];
	memcpy(lineCopy, LINE, 600);
	memset(LINE, 0, 600);

	bool foundW = false;

	int lineIndex = 0;
	for (int32 i = 0; i < 600; ++i)
	{
		if (foundW)
		{
			if (
				lineCopy[i] == '\0' ||
				lineCopy[i] == ' ' ||
				lineCopy[i] == 'w' ||
				lineCopy[i] == 'e' ||
				lineCopy[i] == 'l' ||
				lineCopy[i] == 'c' ||
				lineCopy[i] == 'o' ||
				lineCopy[i] == 'm' ||

				lineCopy[i] == 't' ||

				lineCopy[i] == 'c' ||
				lineCopy[i] == 'd' ||
				
				lineCopy[i] == 'j' ||
				lineCopy[i] == 'a' 
				)
			{
				LINE[lineIndex++] = lineCopy[i];
			}
		}
		else
		{
			if (lineCopy[i] == 'w')
			{
				foundW = true;
				LINE[lineIndex++] = lineCopy[i];
			}
		}
	}
}

// Problem 2
int main()
{
	FILE *inputStream = freopen("C-small.in", "r", stdin);
	assert(inputStream != NULL);
	FILE *outputStream = fopen("result.txt", "w");
	assert(outputStream != NULL);

	int32 testCount = 0;
	scanf("%d", &testCount);
	gets(LINE);
	
	for (int32 i = 0; i < testCount; ++i)
	{
		//scanf("%[^\r]", line);
		gets(LINE);
		LINE_SIZE = strlen(LINE);

		matchString2(0, 0);
		LINE_SIZE = strlen(LINE);

		filterLine();
		LINE_SIZE = strlen(LINE);

		matchCount = 0;
		matchString(0, 0);

		printf("Case #%d: %04d\r\n", (i + 1), matchCount);
		fprintf(outputStream, "Case #%d: %04d\r\n", (i + 1), matchCount);
	}


	fclose(inputStream );
	fclose(outputStream);

	return 0;
}