#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <map>

using namespace std;

#define CHAR_SIZE 36000

filebuf fb;
int iNumberOfTests = 0;
map<char, char> mpLetter;

void ReadLineFromFile(char *s)
{
	if(!fb.is_open())
	{
		fb.open("C-small-attempt0.in", ios::in);//Done & Correct
	}
	istream is(&fb);
	if(iNumberOfTests == 0)
	{
		is.getline(s, CHAR_SIZE);
		iNumberOfTests = ::atoi(s);
	}
	is.getline(s, CHAR_SIZE);
}

void OutputData(int iCase, short pLine)
{
#ifdef _DEBUG
	cout << "Case #"<<iCase<< ": " << pLine << "\r\n";
#endif

	ofstream outfile("google.txt", ios::out | ios::app);
	outfile << "Case #"<<iCase<< ": " << pLine << "\n";
	outfile.flush();
	if(iCase == (iNumberOfTests))
	{
		fb.close();
	}
}

void ParseLine(char * Line, int &iA, int &iB)
{
	char * ptLineBeg = Line;

	iA = atoi(Line);
	while(*Line != ' '){Line++;}
	Line++;
	iB = atoi(Line);


	Line = ptLineBeg;
	return; 
}

short CreateOutput(int iA, int iB) 
{
	short sRet = 0;
	int iCount = 0; 
	short iDigit = 1;
	string strN; 
	string strM; 
	char * cBuf; 
	cBuf = new char[7];

	if(iA >= 10)
		iDigit = 2;
	if(iA >= 100)
		iDigit = 3;
	if(iA >= 1000)
		iDigit = 4;
	if(iA >= 10000)
		iDigit = 5;
	if(iA >= 100000)
		iDigit = 6;
	if(iA >= 1000000)
		iDigit = 7;
	//remember A <= n < M <= B
	for(int n = iA; n < iB ; n++)
	{
		for(int m = n+1; m <= iB; m++) //so n must be < m, always!
		{
			itoa(n, cBuf, 10);
			strN.assign(cBuf, iDigit);
			itoa(m, cBuf, 10);
			strM.assign(cBuf, iDigit);
			while(iCount < strM.size())
			{
				if(strM.compare(strN) == 0)
				{
#ifdef _DEBUG
					ofstream outfile("google.txt", ios::out | ios::app);
					outfile << "(" << n << ", " << m << ")";
					outfile.flush();
#endif				
					sRet++;
				}
				//strN.append(strN[0]);
				//strN.push_back('');
				strN.insert(0, &strN[iDigit-1]);
				strN.erase(iDigit,1);
				iCount++;
			}
			iCount = 0;
		}
	}
	delete cBuf; 
	return sRet;
}

int main()
{
	char * Line; 
	int iCase = 1;
	short sOut = 0; 

	int iA= 0; 
	int iB= 0;

	do{
		Line = new char[CHAR_SIZE];
		ReadLineFromFile(Line);
		ParseLine(Line, iA, iB);
		sOut = CreateOutput(iA, iB);
		OutputData(iCase, sOut);
		iCase++;
		delete Line;
	}while (iCase <= iNumberOfTests);
	return 0;
}