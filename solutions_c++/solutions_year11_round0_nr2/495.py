#include <stdlib.h>
#include <fstream>
#include <iostream>
using namespace std;

#define INPUT_FILE "B-large.in"
#define OUTPUT_FILE "Magicka.out"

int nTest;
ifstream input;	
ofstream output;

typedef struct combined 
{
	char element[2];
	char result;
};

typedef struct opposed
{
	char element[2];
};

char inputList[100];
int nInput;
int nOutput;
char outputList[100];
int nCombined;
combined combineRule[36];
int nOpposed;
opposed opposedRule[28];
char temp[3];
void Solve(int index)
{
	// read data
	nOutput = 0;
	input >> nCombined;
	for (int i = 0; i < nCombined; i++)
	{
		input >> temp;
		combineRule[i].element[0] = temp[0];
		combineRule[i].element[1] = temp[1];
		combineRule[i].result = temp[2];
	}

	input >> nOpposed;
	for (int i = 0; i < nOpposed; i++)
	{
		input >> temp;
		opposedRule[i].element[0] = temp[0];
		opposedRule[i].element[1] = temp[1];
	}
	input >> nInput >> inputList;
	
	for (int i = 0; i< nInput; i++)
	{
		bool hasCombine = false;
		bool hasOpposed = false;
		if (i!= 0)
		{
			
			for (int iCombine = 0; iCombine < nCombined; iCombine++)
				if ((inputList[i] == combineRule[iCombine].element[0] && outputList[nOutput -1] == combineRule[iCombine].element[1])
					|| (inputList[i] == combineRule[iCombine].element[1] && outputList[nOutput -1] == combineRule[iCombine].element[0]))
				{
					outputList[nOutput - 1] = combineRule[iCombine].result;
					hasCombine = true;
					break;
				}
			if (!hasCombine)
				for (int iOpposed = 0; iOpposed < nOpposed ; iOpposed ++ )
					if (inputList[i] == opposedRule[iOpposed].element[0] ||inputList[i] == opposedRule[iOpposed].element[1])
					{
						for (int iOpEle = 0; iOpEle < nOutput; iOpEle ++)
							if (outputList[iOpEle] != inputList[i] && (outputList[iOpEle] == opposedRule[iOpposed].element[0] || outputList[iOpEle] == opposedRule[iOpposed].element[1]))
							{
								hasOpposed = true;
								nOutput = 0;
								break;
							}
							if (hasOpposed)
								break;
					}
		}
		if (!hasCombine && !hasOpposed)
		{
			outputList[nOutput] = inputList[i];
			nOutput ++;
		}
	}
	


	//write out data
	output << "Case #" << index + 1 << ": [";
	for (int i = 0; i < nOutput; i++)
	{
		output << outputList[i] ;
		if (i != nOutput - 1)
			output << ", ";
	}
	output << "]" << endl;

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