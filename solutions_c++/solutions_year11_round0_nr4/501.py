#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

#define INPUT_FILE "D-large.in"
#define OUTPUT_FILE "Goro.out"

int nTest;
ifstream input;	
ofstream output;

int nElement;
double result;
int list[1001];
int trace[1001];

int queue[1001];
int nqueue;

int GetAverage(int x)
{
	return (x-1)*2;
}

void Solve(int index)
{
	result = 0;
	input >> nElement;
	for (int i =1; i<= nElement ; i++)
	{
		input >> list[i];
		if (list[i] == i) trace[i] = 1;
		else
			trace[i] = 0;
	}
	int count = 0;
	for (int i = 1 ; i <=nElement ; i++)
		if (trace[i] == 0)
		{
			//bool endLine = false;
			//int current = list[i];
			//nqueue = 0;
			//queue[nqueue++] = list[i];
			//trace[i] = 1;
			//while (!endLine)
			//{
			//	trace[current] = 1;
			//	current = list[current];
			//	queue[nqueue++] = current;
			//	for (int j = 0; j< nqueue-1; j++)
			//		if (queue[j] == current)
			//		{
			//			endLine = true;
			//			break;
			//		}
			//}
			//result += GetAverage(nqueue-1);
			count ++;
		}
		//if (result == 0)
		//		output << "Case #" << index + 1 << ": 0.000000"<<endl;
		//else
		//output << "Case #" << index + 1 << ": " << result <<".000000" << endl;
		if (count >= 2)
			output << "Case #" << index + 1 << ": " << count <<".000000" << endl;
		else 
			output << "Case #" << index + 1 << ": 0.000000"<<endl;
}

void main()
{
	input.open(INPUT_FILE);
	output.open(OUTPUT_FILE);
	input >> nTest;
	for (int i =0; i < nTest; i++)
		Solve(i);		
	input.close();
	output.close();
}