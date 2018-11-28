#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string.h>

using namespace std;

const char BASE[] = "welcome to code jam";

void calc(char *buf, int base_i, int buf_i, int &result, int buf_len );
int calc(char *);

int main()
{
	ifstream inStream;
	ofstream outStream("output9.txt", ios_base::out | ios_base::app);
	
	int testCases;
	char enter = '\n';
	
	inStream.open("C-small-attempt2.in");

	if (inStream.fail())
	{
		cerr << "Input file opening failed.\n";
		exit(1);
	}

	inStream >> testCases;
	
	for(int i = 0 ; i <= testCases; ++i)
	{
		char buf[512] = {0};
		inStream.getline(buf, 512 , enter);

		if(i == 0)
			continue;
		int result = 0;
		int buf_len = strlen(buf);
		calc(buf, 0, 0, result, buf_len );
	//	int result = calc(buf);


		cout << result << endl;
		//cout << result << endl;

		outStream << "Case #" << i  << ": ";
		if( result < 10)
			outStream << "000" << result << "\n";
		else if(result < 100)
			outStream << "00" <<  result << "\n";
		else if(result < 1000)
			outStream << "0" <<  result << "\n";
		else
			outStream << result << "\n";
	}

	inStream.close();
	outStream.close();


	return 0;
	
}

void calc(char *buf, int base_i, int buf_i, int &result, int buf_len )
{
	int i, j;

	for( i = buf_i ; i <  buf_len ; ++i)
	{
		if( buf[i] == BASE[base_i])
		{
			if(base_i+1 < strlen(BASE))
			{
				calc(buf, base_i+1 , i+1, result, buf_len );
			}
			if(base_i+1 == strlen(BASE))
			{
				result++;
			}
		}
	}
}
