#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt1.in");
	fout.open("A-small-attempt1.out");

	int nCaseNum;
	fin >> nCaseNum;
//	cout << nCaseNum << endl;

	const unsigned int codetable[26] = {25, 8, 5, 19, 15, 3, 22, 24, 4, 21, 9, 7, 12,
						2, 11, 18, 26, 20, 14, 23, 10, 16, 6, 13, 1, 17};
	//const char codetable[26] = {'y',''}

	char strInput[200];
	int nReadIdx;
	unsigned int nChIdx;
	fin.getline(strInput,201);
	for (nReadIdx=0;nReadIdx<nCaseNum;nReadIdx++)
	{
		fin.getline(strInput,201);
		//cout << strInput << endl;
		fout << "Case #" << nReadIdx+1 << ": ";
		for(nChIdx=0;nChIdx<strlen(strInput);nChIdx++)
		{
			if (strInput[nChIdx]==' ')
				fout << ' ';
			else
				fout << char('a'+codetable[strInput[nChIdx]-'a']-1);			
		}
		fout << endl;
	}
	/*
	int nPrintIdx;
	for (nPrintIdx=0;nPrintIdx<nCaseNum;nPrintIdx++)
	{
		fout << "Case #" << nPrintIdx+1 << ": ";
		fout << endl;
	}
*/
	fin.close();
	fout.close();
	return 0;
}