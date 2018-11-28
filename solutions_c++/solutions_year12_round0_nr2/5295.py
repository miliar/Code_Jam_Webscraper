#include "Handler.h"
#include <sstream>

using namespace std;

struct r1prob1
{
	r1prob1() {};
	~r1prob1() {};

	vector<string>* split(string s)
	{
		stringstream ss(s);
		string sTmp;
		vector<string>* vect = new vector<string>();

		while (getline(ss, sTmp, ' ')) {
			vect->push_back(sTmp);
		}

		return vect;
	};
	
	int solve()
	{
		Handler myFiles;
		string lineIn;
		int numCases = 0;
		
		myFiles.openIn("r1prob1In.txt");
		myFiles.openOut("r1prob1Out.txt");
		
		//getline(myFiles.fileIn, lineIn);
		//numCases = atoi(lineIn.c_str());
		
		myFiles.fileIn >> numCases;
		
		int iDancers, iSurprises, iBest, iVal;
		int iTmp, iCount;
		vector<int> v;
		vector<int> poss;
		
		for(int i=0; i<numCases; i++)
		{
			myFiles.debugOut << "case " << (i+1) << "\r\n";
			iDancers = iSurprises = iBest = 0;
			iTmp = iCount = 0;
			v.clear();
			poss.clear();
			
			myFiles.fileIn >> iDancers;
			myFiles.fileIn >> iSurprises;
			myFiles.fileIn >> iBest;
					
			for(int j=0; j<iDancers; j++)
			{
				myFiles.fileIn >> iVal;
				v.push_back(iVal);
				poss.push_back(0);
			}
			
			iCount = 0;
			int iTmpSurp = 0;
			myFiles.debugOut << "iBest: " << iBest; // << "\r\n";
			myFiles.debugOut << "  iSurprise: " << iSurprises << "\r\n";
			for(int j=0; j<iDancers; j++)
			{
				iVal = v.at(j);
				myFiles.debugOut << "ival: " << iVal << "; ";
				iTmp = iVal - iBest;
				if(iTmp < 0 || iVal < iBest)
				{
					myFiles.debugOut << "no -- iVal: " << iVal << "; iBest: " << iBest;
				} else {
					iTmp = iTmp / 2;
					myFiles.debugOut << "itmp: " << iTmp << "; ";
					if(iTmp >= (iBest - 1)){
						poss.at(j) = 1;
						iCount++;
						myFiles.debugOut << "count";
					} else if(iTmp >= (iBest - 2)){
						poss.at(j) = 2;
						iTmpSurp++;
						myFiles.debugOut << "surprise";
					} else {
						poss.at(j) = 3;
						myFiles.debugOut << "other";
					}
				}
			}
			
			if(iTmpSurp > iSurprises)
				iTmpSurp = iSurprises;
			iCount += iTmpSurp;
			
			myFiles.debugOut << "\r\nCase #" << (i + 1) << ": " << iCount << "\r\n";
			myFiles.fileOut << "Case #" << (i + 1) << ": " << iCount << "\r\n";
			
			myFiles.debugOut << "\r\n";
		}
		
		myFiles.fileOut << "\r\n";
		
		myFiles.close();
		
		return 0;
	};
	

};
