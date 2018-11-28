////////////////////////////////////////////////////////
///////    Snapper Chain
///////    A empty win32 console project
///////    Language : C++
///////////////////////////////////////////////////////

///////////////////////////////////////////////////////
///////		Constant
///////////////////////////////////////////////////////
#define INPUT_PATH "SnapperChain.in"  // input file name
#define OUTPUT_PATH "SnapperChain.out" // output file name


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
int N,K; // data input


///////////////////////////////////////////////////////
///////		Main function
///////////////////////////////////////////////////////

void main()
{
	fileInput.open(INPUT_PATH);
	fileOutput.open(OUTPUT_PATH);
	fileInput >> numberCase;
	for (int i=0; i<numberCase; i++)
	{
		fileInput >> N >> K;
		while ((N--)>1)
		{
			if (K%2 == 0) break;
			K /= 2;
		}
		if (K%2 == 1)
		{
			fileOutput << "Case #" << i+1 << ": ON" << endl;	
		}
		else
		{
			fileOutput << "Case #" << i+1 << ": OFF" << endl;	
		}
	}
	fileInput.close();
	fileOutput.close();
}