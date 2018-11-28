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
#endif

#define SAFE_DELETE(a) if ((a) != NULL) { delete a; a = NULL; }
#define SAFE_DELETE_ARRAY(a) if ((a) != NULL) { delete[] a; a = NULL; }

void removeNotMatch(list<string>& dictionary, int32 index, char *chars, int32 charSize)
{
	list<string> removeStrings;

	for (list<string>::iterator it = dictionary.begin(); it != dictionary.end(); ++it)
	{
		char testChar = (*it).at(index);
		bool removeEntry = true;

		for (int32 i = 0; i < charSize; ++i)
		{
			if (testChar == chars[i])
			{
				removeEntry = false;
				break;
			}
		}

		if (removeEntry)
		{
			removeStrings.push_back(*it);
		}
	}

	while (!removeStrings.empty())
	{
		dictionary.remove(removeStrings.back());
		removeStrings.pop_back();
	}
}

int main()
{
	FILE *inputStream = freopen("A-small.in", "r", stdin);
	assert(inputStream != NULL);
	FILE *outputStream = freopen("result.txt", "w", stdout);
	assert(outputStream != NULL);

	int32 L = 0, D = 0, N = 0;
	scanf("%d %d %d", &L, &D, &N);

	const int32 MAX_L = 30;
	const int32 MAX_BUFFER_SIZE = MAX_L * (MAX_L + 2);
	char buffer[MAX_BUFFER_SIZE];
	memset(buffer, 0, sizeof(char) * MAX_BUFFER_SIZE);

	char checkLetters[MAX_L];
	memset(&checkLetters, 0, sizeof(char) * MAX_L);

	// words
	list<string> dictionary;
	for (int32 i = 0; i < D; ++i)
	{
		scanf("%s", buffer);
		dictionary.push_back(buffer);
	}
	dictionary.sort();

	// tests
	for (int32 i = 0; i < N; ++i)
	{
		int32 bufferIndex = 0;
		list<string> localDictionary = dictionary;

		scanf("%s", buffer);

		// Check each letter on dictionary
		for (int32 j = 0; j < L; ++j)
		{
			int32 testsCount = 0;

			if (buffer[bufferIndex] == '(')
			{
				testsCount = 0;
				bufferIndex++;

				do
				{
					checkLetters[testsCount++] = buffer[bufferIndex++];
				} 
				while ( buffer[bufferIndex] != ')' );
			}
			else
			{
				testsCount = 1;
				checkLetters[0] = buffer[bufferIndex];
			}
			bufferIndex++;

			assert(testsCount <= MAX_L);
			removeNotMatch(localDictionary, j, checkLetters, testsCount);
		}
	
		fprintf(outputStream, "Case #%d: %d\r\n", (i + 1), localDictionary.size());
	}

	fclose(inputStream );
	fclose(outputStream);

	return 0;
}