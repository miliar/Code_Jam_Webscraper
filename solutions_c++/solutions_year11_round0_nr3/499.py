#include <stdlib.h>
#include <fstream>
#include <iostream>
using namespace std;

#define INPUT_FILE "C-large.in"
#define OUTPUT_FILE "Candy.out"

int nTest;
ifstream input;	
ofstream output;

int temp;
int nBag;
int cmin;
int current;
int sum;
void Solve(int index)
{
	input	>> nBag;
	input >> current;
	cmin = current;
	sum = current;
	for (int i = 0; i< nBag -1 ; i++)
	{
		int temp;
		input >> temp;
		if (temp < cmin) cmin = temp;
		sum += temp;
		current = current ^ temp;
	}
	if (current == 0)
	{
		output << "Case #" << index+1 << ": " << sum - cmin << endl;
	}
	else
		output << "Case #" << index+1 << ": NO" << endl;
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