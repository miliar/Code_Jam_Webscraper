//---------------------------------------------------------------------------

#pragma hdrstop

#include <tchar.h>
//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
#include <stdlib>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	ifstream fin("A-large.in");
	ofstream fout("A.out");
	fin >> t;

	for (int i=0; i<t;i++)
	{
		long count = 0;
		int stO = 1;
		int clO = 0;
		int stB = 1;
		int clB = 0;
		char c;
		int s;
		long temp;
		int n;
		fin >> n;
		for (int j = 0; j< n; j++) {
			fin >> c >> s;
			switch (c) {
				case 'O':

					temp = (abs(s - stO) + 1) + clO;
					if (temp <= count) count++;
					else count = temp;
					clO = count;
					stO = s;
					break;
				case 'B':
					temp = (abs(s - stB) + 1) + clB;
					if (temp <= count) count++;
					else count = temp;
					clB = count;
					stB = s;
					break;
			}
        }
        fout << "Case #" << (i+1) << ": " << count << endl;


	}

	fin.close();

	return 0;
}
//---------------------------------------------------------------------------
