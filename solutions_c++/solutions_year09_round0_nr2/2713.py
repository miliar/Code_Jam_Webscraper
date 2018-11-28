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

void removeNotMatch(set<string>& dictionary, int32 index, char *chars, int32 charSize)
{
	list<set<string>::iterator> removeIterators;

	for (set<string>::iterator it = dictionary.begin(); it != dictionary.end(); ++it)
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
			removeIterators.push_back(it);
		}
	}

	while (!removeIterators.empty())
	{
		dictionary.erase(removeIterators.back());
		removeIterators.pop_back();
	}
}

int32 getMin(int32 v1, int32 v2, int32 v3, int32 v4)
{
	int32 min = v1;

	if (v2 < min)
		min = v2;
	if (v3 < min)
		min = v3;
	if (v4 < min)
		min = v4;

	return min;
}

// Problem 2
int main()
{
	FILE *inputStream = freopen("B-small.in", "r", stdin);
	//FILE *inputStream = freopen("A-large.in", "r", stdin);
	assert(inputStream != NULL);
	FILE *outputStream = fopen("result.txt", "w");
	assert(outputStream != NULL);

	int32 mapCount = 0;
	scanf("%d", &mapCount);

	for (int32 i = 0; i < mapCount; ++i)
	{
		int32 mapHeight = 0, mapWidth = 0;
		scanf("%d %d", &mapHeight, &mapWidth);

		int32 map[100][100];
		char mapResult[100][100];
		memset(&map, 0, sizeof(int32) * 100 * 100);
		memset(&mapResult, 0, sizeof(char) * 100 * 100);
		
		for (int32 j = 0; j < mapHeight; ++j)
		{
			for (int32 k = 0; k < mapWidth; ++k)
			{
				scanf("%d", &map[j][k]);
			}
		}

		// DEBUG
		//for (int32 a = 0; a < mapHeight; ++a)
		//{
		//	for (int32 b = 0; b < mapWidth; ++b)
		//	{
		//		printf("%d ", map[a][b]);
		//	}
		//	printf("\r\n");
		//}

		const int32 BIGINT = 11000;

		//
		printf("Case #%d:\r\n", (i+1));
		fprintf(outputStream, "Case #%d:\r\n", (i+1));
		char nextLetter = 'b';
		mapResult[0][0] = 'a';

		bool reprocess = false;
		int32 preprocessCount = -1;

		do 
		{
			preprocessCount++;
			reprocess = false;

			for (int32 j = 0; j < mapHeight; ++j)
			{
				for (int32 k = 0; k < mapWidth; ++k)
				{
					int32 here = map[j][k];
					char& letterHere = mapResult[j][k];

					int32 north = BIGINT;
					int32 west = BIGINT;
					int32 east = BIGINT;
					int32 south = BIGINT;

					if (j > 0)
					{
						north = map[j-1][k];
					}
					if (j < (mapHeight - 1))
					{
						south = map[j+1][k];;
					}
					if (k > 0)
					{
						west = map[j][k-1];
					}
					if (k < (mapWidth - 1))
					{
						east = map[j][k+1];
					}

					int32 min = getMin(north, west, east, south);
					if (min < here)
					{
						if (north == min)
						{
							//if (mapResult[j-1][k] == 0)
							//{
							//	mapResult[j-1][k] = letterHere;
							//}
							//else
							if (letterHere != 0)
							{
								mapResult[j-1][k] = letterHere;
							}
							else
							{
								if (mapResult[j-1][k] != 0)
								{
									letterHere = mapResult[j-1][k];
								}
								else
								{
									reprocess = true;
								}
							}
						}
						else if (west == min)
						{
							//if (mapResult[j][k-1] == 0)
							//{
							//	mapResult[j][k-1] = letterHere;
							//}
							//else
							if (letterHere != 0)
							{
								mapResult[j][k-1] = letterHere;
							}
							else
							{
								if (mapResult[j][k-1] != 0)
								{
									letterHere = mapResult[j][k-1];
								}
								else
								{
									reprocess = true;
								}
							}
						}
						else if (east == min)
						{
							if (mapResult[j][k+1] == 0)
							{
								//if (letterHere == 0)
								//{
								//	letterHere = nextLetter++;
								//}

								//mapResult[j][k+1] = letterHere;
								if (letterHere != 0)
								{
									mapResult[j][k+1] = letterHere;
								}
								else if (mapResult[j][k+1] != 0)
								{
									letterHere = mapResult[j][k+1];
								}
								else
								{
									reprocess = true;
								}
							}
							else
							{
								letterHere = mapResult[j][k+1];
							}
						}
						else if (south == min)
						{
							//if (letterHere == 0)
							//{
							//	letterHere = nextLetter++;
							//}

							//mapResult[j+1][k] = letterHere;

							if (letterHere != 0)
							{
								mapResult[j+1][k] = letterHere;
							}
							else if (mapResult[j+1][k] != 0)
							{
								letterHere = mapResult[j+1][k];
							}
							else
							{
								reprocess = true;
							}
						}
					}
					else
					{
						if (letterHere == 0)
						{
							if (preprocessCount > 4)
							{
								letterHere = nextLetter++;
							}
							else
							{
								reprocess = true;
							}
						}
					}
				}
			} 
		} while (reprocess == true);

		for (int32 j = 0; j < mapHeight; ++j)
		{
			for (int32 k = 0; k < mapWidth; ++k)
			{
				printf("%c", mapResult[j][k]);
				fprintf(outputStream, "%c", mapResult[j][k]);

				if (k < (mapWidth - 1))
				{
					printf(" ");
					fprintf(outputStream, " ");
				}
			}

			printf("\r\n");
			fprintf(outputStream, "\r\n");
		}
	}

	fclose(inputStream );
	fclose(outputStream);

	return 0;
}