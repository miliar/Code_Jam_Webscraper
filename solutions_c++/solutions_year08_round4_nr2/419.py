#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <math.h>

using namespace std;

#define PROB_LETTER "B"
#define INTYPE "small-attempt1"

#define SQR(x) ((x)*(x))

typedef long long lld;
typedef unsigned long long llu;

string readLine(FILE *inFile)
{
	static char inBuffer[1000000];
	fgets(inBuffer, 1000000, inFile);
	string result = inBuffer;
	if (result.empty())
		return result;
	if (result[result.size() - 1] == '\n')
		result.resize(result.size() - 1);
	return result;
}

string findResult(FILE *inFile)
{
	int width, height, targetArea;
	sscanf(readLine(inFile).c_str(), "%d %d %d", &width, &height, &targetArea);

	bool switched = false;

	if (width > height)
	{
		swap(width, height);
		switched = true;
	}

	for(int currentWidth = 1; currentWidth <= width; currentWidth++)
	{
		for(int currentHeight = 1; currentHeight <= height; currentHeight++)
		{
			for(int leftPoint = 0; leftPoint <= currentHeight; leftPoint++)
			{
				for(int bottomPoint = 0; bottomPoint <= currentWidth; bottomPoint++)
				{
					// Try normal triangle
					for(int rightPoint = 0; rightPoint <= currentHeight; rightPoint++)
					{
						lld x1 = 0,
							y1 = leftPoint,
							x2 = bottomPoint,
							y2 = 0,
							x3 = currentWidth,
							y3 = rightPoint;

						if (abs(int(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))) == targetArea)
						{
							stringstream ss;
							if (!switched)
								ss << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << " ";
							else
								ss << y1 << " " << x1 << " " << y2 << " " << x2 << " " << y3 << " " << x3 << " ";
							return ss.str();
						}
					}
				}
			}
		}
	}

	stringstream ss;
	ss << "IMPOSSIBLE";
	return ss.str();
}

int main()
{
	char *inFilename = PROB_LETTER "-" INTYPE ".in";
	char *outFilename = PROB_LETTER "-" INTYPE ".out";

	FILE *inFile = fopen(inFilename, "r");
	FILE *outFile = fopen(outFilename, "w");

	if (inFile == NULL)
	{
		printf("inFile does not exist!\n");
		system("PAUSE");
		return 1;
	}
	if (outFile == NULL)
	{
		printf("Failed to open outFile!\n");
		system("PAUSE");
		return 1;
	}

	char inBuffer[1000];
	fgets(inBuffer, 1000, inFile);

	int numCases;
	sscanf(inBuffer, "%d", &numCases);

	for(int i = 1; i <= numCases; i++)
	{
		string result = findResult(inFile);

		fprintf(outFile, "Case #%d: %s\n", i, result.c_str());
		printf("Done with case %d\n", i);
	}

	fclose(inFile);
	fclose(outFile);

	printf("Success!\n");
	system("PAUSE");
}