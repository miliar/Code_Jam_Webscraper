#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, const char* argv)
{
	char dictionary[26];
	char buffer[120];
	char decodedBuffer[120];

	memset(dictionary, 0, 26);

	dictionary['y' - 'a'] = 'a';
	dictionary['e' - 'a'] = 'o';
	dictionary['q' - 'a'] = 'z';
	dictionary['z' - 'a'] = 'q';
	

	ifstream myfile ("D:\\work\\codejam\\2012\\Qualifications\\ProbA_SpeakingTongues\\test0.txt");
	ifstream myresfile ("D:\\work\\codejam\\2012\\Qualifications\\ProbA_SpeakingTongues\\decoding0.txt");



	if (myfile.is_open() && myresfile.is_open())
	{
		int T = 0;
		myfile >> T;
		myfile.getline(buffer, 100, '\n');
		for (int i = 0; i < T; ++i)
		{
			myfile.getline(buffer, 100, '\n');
			myresfile.getline(decodedBuffer, 100, '\n');
			
			for (unsigned int jj = 0; jj < strlen(decodedBuffer); ++jj)
			{
				if (decodedBuffer[jj] != ' ')
				{
					dictionary[buffer[jj] - 'a'] = decodedBuffer[jj];
				}
			}
		}
		myfile.close();
		myresfile.close();
	}
	else
	{
		cout << "Unable to open file"; 
	}

	ifstream smallfile ("D:\\work\\codejam\\2012\\Qualifications\\ProbA_SpeakingTongues\\A-small-attempt1.in");
	if (smallfile.is_open())
	{
		int T = 0;
		smallfile >> T;
		memset(buffer, 0, 101);
		memset(decodedBuffer, 0, 101);

		smallfile.getline(buffer, 100, '\n');
		for (int i = 0; i < T; ++i)
		{
			memset(buffer, 0, 120);
			memset(decodedBuffer, 0, 120);
			smallfile.getline(buffer, 120, '\n');
					
			for (size_t jj = 0; jj < strlen(buffer); ++jj)
			{
				if (buffer[jj] != ' ')
				{
					decodedBuffer[jj] = dictionary[buffer[jj] - 'a'];
				}
				else
				{
					decodedBuffer[jj] = ' ';
				}
			}
			cout << "Case #" << i + 1 << ": " << decodedBuffer << endl;
		}
		myfile.close();
		myresfile.close();
	}
	else
	{
		cout << "Unable to open file"; 
	}
  
	return 0;
}