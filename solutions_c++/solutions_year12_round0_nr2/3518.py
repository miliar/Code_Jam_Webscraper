// GoogleLang.cpp : Defines the entry point for the console application.
//

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
		fb.open("B-large.in", ios::in);//Done & Correct
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

void ParseLine(char * Line, int &iNumberOfGooglers, int &iSurprisingScore, int &iPtMin, int *ptScoreSum)
{
	char * ptLineBeg = Line;

	iNumberOfGooglers = atoi(Line);
	while(*Line != ' '){Line++;}
	Line++;
	iSurprisingScore = atoi(Line);
	while(*Line != ' '){Line++;}
	Line++;
	iPtMin = atoi(Line);
	while(*Line != ' '){Line++;}
	Line++;
	for(int i = 0; i < iNumberOfGooglers; i++)
	{
		ptScoreSum[i] = atoi(Line);
		while(*Line != ' '){Line++;}
		Line++;
	}

	Line = ptLineBeg;
	return; 
}

short CreateOutput(int iNumberOfGooglers, int iSurprisingScores, int iPtMin, int * ptScoreSum ) 
{
	int iSupUsed = 0; 
	float fMed = 0; 
	short sRet = 0;
	for(int i = 0; i < iNumberOfGooglers; i++)
	{
		fMed = ptScoreSum[i] / 3.0;
		fMed = ceil(fMed);
		if(fMed >= iPtMin) sRet++; //if Med >= PtMin Googler is above min score
		else
		{
			if(fMed +1 >= iPtMin && ptScoreSum[i]%3 != 1 && ptScoreSum[i] >= iPtMin){
				if(iSupUsed < iSurprisingScores)
				{
					iSupUsed++; 
					sRet++;
				}
			}
		}
	}
	return sRet;
}

int main()
{
	char * Line; 
	int iCase = 1;
	short sOut = 0; 

	int iNumberOfGooglers = 0; 
	int iSurprisingScores = 0;
	int iPtMin = 0; 
	int * ptScoreSum;  
	
	do{
		Line = new char[CHAR_SIZE];
		ptScoreSum = new int[1000];
		ReadLineFromFile(Line);
		ParseLine(Line, iNumberOfGooglers, iSurprisingScores, iPtMin, ptScoreSum);
		sOut = CreateOutput(iNumberOfGooglers, iSurprisingScores, iPtMin, ptScoreSum);
		delete ptScoreSum;
		OutputData(iCase, sOut);
		iCase++;
		delete Line;
	}while (iCase <= iNumberOfTests);
	cin >> iPtMin;
	return 0;
}
