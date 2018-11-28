#include <iostream>
#include <queue>
#include <stdio.h>
#include <string>
#include <time.h>
#include <windows.h>
using namespace std;

int calcMoney(int runs, int seats, queue<int> *rideLine);

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

	int iterations, R, k, N, readCount, offset;
	char* buffer = new char[25];
	string stringBuff;
	queue<int> rideLine;


	fgets(buffer, 24, inputFile);
	iterations = atoi(buffer);

	for (int i = 0; i < iterations; i++)
	{
		fgets(buffer, 24, inputFile);
		stringBuff.assign(buffer);
		R = atoi(stringBuff.substr(0, stringBuff.find_first_of(' ')).c_str());
		stringBuff = stringBuff.substr(stringBuff.find_first_of(' ') + 1);
		k = atoi(stringBuff.substr(0, stringBuff.find_first_of(' ')).c_str());
		stringBuff = stringBuff.substr(stringBuff.find_first_of(' ') + 1);
		N = atoi(stringBuff.c_str());
		readCount = 0;
		offset = 0;

		while (readCount < N)
		{
			fgets(buffer + offset, 24 - offset, inputFile);
			stringBuff.assign(buffer);

			while (stringBuff.find_first_of(' ') != -1 || stringBuff.find_first_of("\n") != -1)
			{
				rideLine.push(atoi(stringBuff.substr(0, stringBuff.find_first_of(' ')).c_str()));
				stringBuff = stringBuff.substr(stringBuff.find_first_of(' ') + 1, stringBuff.find_last_of("\n"));
				readCount++;
			}

			memcpy(buffer, stringBuff.c_str(), stringBuff.length());
			offset = stringBuff.length();
		}

		fprintf(outputFile, "Case #%d: %d\n", i + 1, calcMoney(R, k, &rideLine));		
	}

	fclose(inputFile);
	fclose(outputFile);
	
	timer += time(NULL);
	printf("Execution time: %d seconds\n", timer);
	Sleep(5000);
	return 0;
}

int calcMoney(int runs, int seats, queue<int> *rideLine)
{
	int sum = 0, seatsRemaining;
	unsigned int count;
	for (int i = 0; i < runs; i++)
	{
		seatsRemaining = seats;
		count = 0;
		while (rideLine->front() <= seatsRemaining && count < rideLine->size())
		{
			sum += rideLine->front();
			seatsRemaining -= rideLine->front();
			rideLine->push(rideLine->front());
			rideLine->pop();
			count++;
		}
	}

	while(rideLine->size() > 0)
	{
		rideLine->pop();
	}
	return sum;
}