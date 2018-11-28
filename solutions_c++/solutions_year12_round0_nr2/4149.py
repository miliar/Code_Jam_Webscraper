// DancingWithGooglers.cpp : Defines the entry point for the console application.
//


#include <stdio.h>
#include <map>
#include <iostream>
#include <fstream>

int Googlers[100];
using namespace std;

int getResult(char *inputline)
{
	int N, S, p;
	int result = 0;
	char *token = strtok(inputline, " ");
	N = atoi(token);
	token = strtok(NULL, " ");
	S = atoi(token);
	token = strtok(NULL, " ");
	p = atoi(token);
	int threshold = 3*p - 4;
	if(threshold < 2)
	{
		threshold = p;
	}
	for(int i = 0; i < N; i++)
	{
		token = strtok(NULL, " ");
		if(token == NULL)
			printf("\n error in parsing");
		else
			Googlers[i] = atoi(token);
		if(((threshold < 2) && (Googlers[i]>=threshold))||(Googlers[i] > threshold+1))
		{
			result++;
		}
		else if((Googlers[i] == threshold) || (Googlers[i] == threshold+1))
		{
			if(S>0)
			{
				result++;
				S--;
			}
		}
	}
	for(int i = 0; i < N; i++)
	{
		printf("\nGoogler[%d] = %d", i, Googlers[i]);
	}
	return result;
}
#define MAX_LINE_SIZE 1024
int main(int argc, char* argv[])
{

	if(argc < 2)
	{
		printf("\n Input file not specified");
		return -1;
	}

	int i = 0;
	char inputline[MAX_LINE_SIZE];
	char outputline[MAX_LINE_SIZE];
	ifstream infile(argv[1]);
	ofstream outfile("output.txt");
	infile.getline(inputline, MAX_LINE_SIZE, '\n');
	int numInputLines = atoi(inputline);
	while(i < numInputLines)
	{
		infile.getline(inputline, MAX_LINE_SIZE, '\n');
		outfile<<"Case #"<<i+1<<": "<<getResult(inputline)<<"\n";
		i++;
	}
	return 0;
}


