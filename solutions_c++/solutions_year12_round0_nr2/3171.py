#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	char inFilename[] = "G:\\B-large.in";
	char outFilename[] = "G:\\out.txt";
	ifstream inputFile(inFilename);
	ofstream outputFile(outFilename, ios::out);
	if(!inputFile || !outputFile)
	{
		cout << "File Operation Error!" <<endl;
		return 1;
	}

	int numQ = 0;
	inputFile >> numQ;

	for(int i = 0 ; i < numQ ; ++i)
	{
		cout << "Solving #" << i+1 << endl;
		outputFile << "Case #" << i+1 << ": ";
		//begin
		int numDancer, numSp, p;
		inputFile >> numDancer >> numSp >> p;
		int result = 0 , candicate = 0;
		for(int j = 0 ; j < numDancer ; ++j)
		{
			int t;
			inputFile >> t;
			if(t/3 >= p)
				++result;//got one definitely pass
			else if (t/3 == p-1 && t != 0)//0 can only be 0,0,0 and only pass when p = 0;
			{
				if(t%3 != 0)
					++result;//somehow pass
				else
					++candicate;//as below
			}
			else if (t/3 == p-2 && t%3 == 2)
				++candicate;//waiting for a SURPRISE!
		}
		result += candicate>=numSp? numSp : candicate;
		outputFile << result <<endl;
	}


	inputFile.close();
	outputFile.close();
	return 0;
}
