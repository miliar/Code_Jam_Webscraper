// RecycledNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <iostream>
#include <conio.h>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	string strInput, strOutput;
	ifstream ifile ;
	ifile.open("input.in");
	ofstream  ofile;
	ofile.open("output.txt");  

	if (!ifile.is_open())
		return 0;

	getline (ifile, strInput);
	int iTestCaseCount = atoi(strInput.c_str());
	if (iTestCaseCount<=1 || iTestCaseCount>50)
		return 0;

	char buff[256];
	memset(buff, 0, 256);

	for (int index=1; index<=iTestCaseCount; ++index)
	{
		strOutput = "Case #";
		char buff[256];
		memset(buff, 0, 256);
		_itoa(index, buff, 10);
		strOutput += buff;
		strOutput += ": ";

		getline (ifile, strInput);
		memcpy(buff, strInput.c_str(), strInput.length());
		char * pch = strtok(buff," ");

		int A = 0, B = 0, result = 0;
		int arr[2] = {0,0};
		for(int i=0; pch != NULL; ++i)
	    {
			arr[i] = atoi(pch);
			pch = strtok (NULL, " ");
	    }
		A = arr[0]; B = arr[1];

		int digits_in_n = floor( log10( abs((double) A ) ) ) + 1; 
		if (digits_in_n==1)
		{
			strOutput = "Case #";
			char buff[256];
			memset(buff, 0, 256);
			_itoa(index, buff, 10);
			strOutput += buff;
			strOutput += ": ";
			memset(buff, 0, 256);
			itoa(result, buff, 10);
			strOutput = strOutput + string(buff);

			ofile.write(strOutput.c_str(), strOutput.length());
			ofile.write("\n", 1);
			continue;
		}

		for (int n=A; n<B; n++)
		{
			int m_lower = n+1;
			int m_upper = B;
			
			memset(buff, 0, 256);
			itoa(n, buff, 10);
			string str1(buff);

			vector<string>vec;
			
			for (int index2=1; index2<digits_in_n; index2++)
			{
				str1 += str1.at(0);
				str1.erase(0, 1);
			
				int temp = atoi(str1.c_str());

				bool flag = (std::find(vec.begin(), vec.end(), str1)!=vec.end());
				if ( (temp>=m_lower) && (temp<=m_upper) && flag==false )
					result++;
				vec.push_back(str1);
			}	
		}

		memset(buff, 0, 256);
		itoa(result, buff, 10);
		strOutput = strOutput + string(buff);

		ofile.write(strOutput.c_str(), strOutput.length());
		ofile.write("\n", 1);
	}

	ifile.close();
	ofile.close();

	cout<<"\nDone";
	_getch();
	return 0;
}

