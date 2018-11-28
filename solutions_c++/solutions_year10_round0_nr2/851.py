////////////////////////////////////////////////////////
///////    Snapper Chain
///////    A empty win32 console project
///////    Language : C++
///////////////////////////////////////////////////////

///////////////////////////////////////////////////////
///////		Constant
///////////////////////////////////////////////////////
#define INPUT_PATH "FairWarning.in"  // input file name
#define OUTPUT_PATH "FairWarning.out" // output file name


///////////////////////////////////////////////////////
///////		Using library
///////////////////////////////////////////////////////
#include <iostream>
#include <fstream>
using namespace std;


///////////////////////////////////////////////////////
///////		Global variable
///////////////////////////////////////////////////////

ifstream fileInput; // input stream
ofstream fileOutput; // output stream
int numberCase; // number of test
int timeValues[3]; // data input
int numberEvent; // data input
int result; // result

///////////////////////////////////////////////////////
///////		Main function
///////////////////////////////////////////////////////

void main()
{
	fileInput.open(INPUT_PATH);
	fileOutput.open(OUTPUT_PATH);
	fileInput >> numberCase;
	for (int i = 0; i< numberCase; i++)
	{
		fileInput >> numberEvent;
		for (int j=0; j<numberEvent; j++)
			fileInput >> timeValues[j];
		switch (numberEvent)
		{
		case 2: 
			result = timeValues[1] - timeValues[0];
			if (result < 0)	result *= (-1);
			break;
		case 3:
			result = timeValues[1] - timeValues[0];
			if (result < 0)	result *= (-1);
			int temp = timeValues[2] - timeValues[1];
			if (temp < 0)temp *= (-1);
			if (temp == 0)break;
			if (result == 0) 
			{
				result = temp;
				break;
			}
			while (temp != result)
			{
				if (temp > result) temp -= result;
				else result -= temp;
			}
			break;
		}
		if (result != 0 && result != 1 && timeValues[0]%result!=0)		
			result -= (timeValues[0]%result);
		else result = 0;
		fileOutput << "Case #" << i+1 <<": "<< result << endl;
	}
	fileInput.close();
	fileOutput.close();
}