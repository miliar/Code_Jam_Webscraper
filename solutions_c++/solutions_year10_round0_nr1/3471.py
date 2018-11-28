#include <iostream>
#include <math.h>
#include <stdio.h>
#include <string>
#include <time.h>
#include <windows.h>
using namespace std;

bool isLightOn(int lightCount, int snapCount);

int main(int argc, char** argv)
{
	if (argc < 2)
	{
		cout << "Please specify input file" << endl;
		return 1;
	}

	time_t timer = -time(NULL);

	FILE* inputFile;
	inputFile = fopen(argv[1], "r");
	if (inputFile == NULL) perror ("Error opening file");

	FILE* outputFile;
	outputFile = fopen("output.txt", "w");
	if (outputFile == NULL) perror ("Error opening file");

	int iterations, N, K;
	char buffer[15]; //Max line length is 14 characters
	string stringBuff;

	fgets(buffer, 14, inputFile);
	iterations = atoi(buffer);

	for (int i = 0; i < iterations; i++)
	{
		fgets(buffer, 22, inputFile);
		stringBuff.assign(buffer);
		N = atoi(stringBuff.substr(0, stringBuff.find_first_of(' ')).c_str());
		K = atoi(stringBuff.substr(stringBuff.find_first_of(' ') + 1).c_str());
		fprintf(outputFile, "Case #%d: ", i + 1);
		
		if (isLightOn(N, K))
			fprintf(outputFile, "ON\n");
		else
			fprintf(outputFile, "OFF\n");
	}

	fclose(inputFile);
	fclose(outputFile);
	
	timer += time(NULL);
	printf("Execution time: %d seconds\n", timer);
	Sleep(5000);
	return 0;
}

bool isLightOn(int lightCount, int snapCount)
{
	int comparison = (int)pow(2.0, (double)lightCount);
	if ((snapCount + 1) % comparison == 0)
		return true;
	else
		return false;
}