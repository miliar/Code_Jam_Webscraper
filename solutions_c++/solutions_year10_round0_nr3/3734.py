#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;

int main()
{
	string inputFile;
	char datastring[11] = {'/0'};
	long int i = 0, j = 0, k = 0, limit = 0, a = 0, b = 0, x = 0, y = 0;
	double sum = 0, grandSum = 0;

	double rkn[3]={0}, N = 1;

	cout << " Enter the name of the file. " << endl;
	cin >> inputFile;

	ofstream output("output.txt");
	ifstream rdFile(inputFile.c_str());
	if(rdFile.fail())
	{
		cout << " The file failed to open. " << endl;
		exit(1);
	}
	else
	{
		rdFile >> datastring;
		limit = atoi(datastring);
		for(i = 0; i < limit; i++)
		{
			// R, k , N info for a test case
			for(j = 0; j < 3; j++)
			{
				rdFile >> datastring;
				rkn[j] = atof(datastring);
			}
			double*NPtr = new double[rkn[2]];
			// the groups of people
			for(k = 0; k < rkn[2]; k++)
			{
				rdFile >> datastring;
				NPtr[k] = atof(datastring);
			}
			grandSum = 0;
			
			// number of rounds
			for(a = 0; a < rkn[0]; a++)
			{
				sum = 0;
				b = 0;
				while((sum + NPtr[b] <= rkn[1]))
				{
					sum += NPtr[b];
					if((b + 1) < rkn[2])
						b++;
					else 
						break;
				}
				grandSum += sum;
				double*temp = new double[b];
				// copying front values of queue
				for(x = 0; x < b ; x++)
				{
					temp[x] = NPtr[x];
				}
				// adjusting queue, latter value coming to front
				for(x = b , y = 0; x < rkn[2]; x++, y++)
				{
					NPtr[y] = NPtr[x];
				}
				for(x = rkn[2] - b, y = 0; x < rkn[2]; x++, y++)
				{
					NPtr[x] = temp[y];
				}
				delete []temp;
				temp = 0;
			}
			output << "Case #" << N++ << ": " << grandSum << endl;
			delete []NPtr;
			NPtr = 0;
		}
	}
	output.close();
	return 0;
}