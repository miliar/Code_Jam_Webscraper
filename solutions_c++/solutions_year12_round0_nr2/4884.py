#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <fstream>
#include <string>
#include <sstream>
#include <map>

using namespace std;


string calculate (string str)
{
	int result = 0;
	char * num = strtok ((char *)str.c_str()," ");
	int googlers = atoi(num);
	num = strtok (NULL, " ");
	int surprising = atoi(num);
	num = strtok (NULL, " ");
	int maxScore = atoi (num);

	for (int i = 0; i < googlers; i ++ )
	{
		num = strtok (NULL, " ");
		int score = atoi (num);
		if (score % 3 == 0)
		{
			if (score/3>=maxScore)
				result++;
			else if (score/3 + 1 >=maxScore && surprising > 0 && score/3 - 1 > 0)
			{
				result++;
				surprising--;
			}
		}
		else if (score % 3 == 1)
		{
			if((score/3)+1>=maxScore)
			{
				result ++;
			}
		}
		else 
		{
			if ((score/3)+1>=maxScore)
			{
				result++;
			}
			else if ((score/3) + 2 >=maxScore  && surprising > 0)
			{
				surprising--;
				result++;
			}
		}


	}
	stringstream s;
	s << result <<"\n";
	return s.str();
}

int main(int argc, char *argv[])
{

	ifstream inFile ("input.txt");
	ofstream  outFile ("output.txt");
	if (inFile.is_open() && outFile.is_open())
	{
		string line;
		getline (inFile,line);
		int inputSize = atoi(line.c_str());
		for (int i = 1; i <= inputSize; i++)
		{
			getline (inFile,line);


			
			
			string output = calculate(line);
			outFile << "Case #"<< i <<": " << output.c_str();
		}
		inFile.close();
		outFile.close();
	}



    return 0;
}