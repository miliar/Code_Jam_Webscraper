#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	char inFilename[] = "G:\\A-small-attempt0.in";
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

	char mapping[26] = // from G to E
	{
			'y', 'h', 'e', 's', 'o', 'c', 'v',//a~g
			'x', 'd', 'u', 'i', 'g', 'l', 'b',//h~n
			'k', 'r', 'z', 't', 'n', 'w',//o~t
			'j', 'p', 'f', 'm', 'a', 'q'//u~z
	};

	char c;
	inputFile.get(c);
	for(int i = 0 ; i < numQ ; ++i)
	{
		cout << "Solving #" << i+1 << endl;
		outputFile << "Case #" << i+1 << ": ";
		//begin

		while(!inputFile.eof() && (c=inputFile.get())!= '\n')
		{
			if(c != ' ')
				outputFile << mapping[c-'a'];
			else
				outputFile << ' ';
		}
		outputFile << endl;
	}


	inputFile.close();
	outputFile.close();
	return 0;
}
