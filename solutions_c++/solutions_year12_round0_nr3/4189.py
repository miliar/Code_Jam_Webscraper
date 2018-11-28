#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <math.h>

using namespace std;

int numLength(int num)
{
	int result = 0;
	while(num>0)
	{
		num=num/10;
		result++;
	}
	return result;
 
}

string calculate (string str)
{
	int result = 0;
	char * num = strtok ((char *)str.c_str()," ");
	int min = atoi(num);
	num = strtok (NULL, " ");
	int max = atoi(num);
	for (int i = min; i <= max; i ++ )
	{
		map <int,int> myMap;

		int len = numLength(i);
		for (int j=1; j<len; j++)
		{
			int recycled = ((i % (int)pow(10,j)) * (pow(10,len-j))) + i/pow(10,j);
			if (recycled >=min && recycled <=max && recycled >i)
			{
				if (myMap.count(i) && myMap[i]==recycled)
				{
				}
				else
				{
					result ++;
					myMap[i]=recycled;
				}
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